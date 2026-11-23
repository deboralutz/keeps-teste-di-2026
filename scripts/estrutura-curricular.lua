local function with_role(role, identifier, attributes)
  attributes = attributes or {}
  attributes.role = role
  return pandoc.Attr(identifier or "", {}, attributes)
end

local function header_cell(text)
  return pandoc.Cell({pandoc.Plain(text)}, "AlignDefault", 1, 1, with_role("columnheader", nil, {scope = "col"}))
end

local function table_row(title, description, identifier)
  return pandoc.Row({
    pandoc.Cell({pandoc.Plain(title)}, "AlignDefault", 1, 1, with_role("rowheader", identifier, {scope = "row"})),
    pandoc.Cell(description, "AlignDefault", 1, 1, with_role("cell")),
  }, with_role("row"))
end

local function document_table(label, columns, rows)
  local headers = pandoc.Row({header_cell(columns[1]), header_cell(columns[2])}, with_role("row"))
  return pandoc.Table(
    {long = {}},
    {{"AlignDefault", 0.36}, {"AlignDefault", 0.64}},
    pandoc.TableHead({headers}, with_role("rowgroup")),
    {{attr = with_role("rowgroup"), row_head_columns = 1, head = {}, body = rows}},
    pandoc.TableFoot({}),
    pandoc.Attr("", {"curriculum-table"}, {role = "table", ["aria-label"] = label})
  )
end

local function section_index(links, class, label)
  return pandoc.Div(
    {pandoc.Para(links)},
    pandoc.Attr("", {class}, {role = "navigation", ["aria-label"] = label})
  )
end

local function module_section(blocks)
  local heading = blocks[1]
  local content = pandoc.List({heading})
  local lessons = {}

  for i = 2, #blocks do
    local block = blocks[i]
    if block.tag == "Header" and block.level == 4 then
      lessons[#lessons + 1] = {heading = block, description = pandoc.List()}
    elseif #lessons > 0 then
      lessons[#lessons].description:insert(block)
    else
      content:insert(block)
    end
  end

  if #lessons == 0 then
    return content
  end

  local rows = {}
  for _, lesson in ipairs(lessons) do
    rows[#rows + 1] = table_row(lesson.heading.content, lesson.description, lesson.heading.identifier)
  end

  content:insert(document_table(pandoc.utils.stringify(heading.content), {"Aula", "Conteúdo e atividades"}, rows))
  return pandoc.List({pandoc.Div(content, pandoc.Attr("", {"curriculum-module"}))})
end

local function schedule_table(list, label)
  local rows = {}
  for _, item in ipairs(list.content) do
    local first = item[1]
    local inlines = first and first.content
    if not first or (first.tag ~= "Plain" and first.tag ~= "Para")
      or not inlines[1] or inlines[1].tag ~= "Strong" or not inlines[2] or inlines[2].tag ~= "Space" then
      return list
    end
    local description = pandoc.List({pandoc.Plain({table.unpack(inlines, 3)})})
    description:extend({table.unpack(item, 2)})
    rows[#rows + 1] = table_row(inlines[1].content, description)
  end
  return document_table(label, {"Período e etapa", "Atividades previstas"}, rows)
end

local function format_proposal(blocks)
  local result = pandoc.List()
  local links = pandoc.List()
  local section
  local navigation_position
  local in_proposal = false
  local module_open = false

  local function close_module()
    if module_open then
      result:insert(pandoc.RawBlock("html", "</details>"))
      module_open = false
    end
  end

  for _, block in ipairs(blocks) do
    if block.tag == "Header" and block.level <= 2 then
      close_module()
      in_proposal = block.identifier == "ementa-cronograma"
      section = nil
      if in_proposal then navigation_position = #result + 2 end
    elseif in_proposal and block.tag == "Header" and block.level == 3 then
      close_module()
      section = block
      if #links > 0 then links:insert(pandoc.Space()) end
      links:insert(pandoc.Link(block.content, "#" .. block.identifier))
    end

    local section_id = section and section.identifier
    if section_id == "percurso-formativo" and block.tag == "Header" and block.level == 4 then
      close_module()
      local id = block.identifier:gsub("&", "&amp;"):gsub('"', "&quot;"):gsub("<", "&lt;")
      result:insert(pandoc.RawBlock("html", '<details class="proposal-module" id="' .. id .. '"><summary>'))
      result:insert(pandoc.Header(4, block.content))
      result:insert(pandoc.RawBlock("html", "</summary>"))
      module_open = true
    elseif section_id == "percurso-formativo" and block.tag == "Para"
      and pandoc.utils.stringify(block):match("^Carga horária total estimada:") then
      close_module()
      result:insert(pandoc.Div({block}, pandoc.Attr("", {"proposal-total"})))
    elseif section_id == "visão-geral" and block.tag == "BulletList" then
      result:insert(pandoc.Div({block}, pandoc.Attr("", {"proposal-facts"})))
    elseif section_id == "objetivos-de-aprendizagem" and block.tag == "OrderedList" then
      result:insert(pandoc.Div({block}, pandoc.Attr("", {"proposal-objectives"})))
    elseif section_id and section_id:match("^cronograma%-preliminar") and block.tag == "BulletList" then
      result:insert(schedule_table(block, pandoc.utils.stringify(section.content)))
    else
      result:insert(block)
    end
  end

  close_module()
  if navigation_position and #links > 0 then
    result:insert(navigation_position, section_index(links, "proposal-index", "Seções da Parte I"))
  end
  return result
end

function Pandoc(document)
  local result = pandoc.List()
  local modules = pandoc.List()
  local index_links = pandoc.List()
  local in_curriculum = false
  local current_module

  local function finish_module()
    if current_module then
      modules:extend(module_section(current_module))
      current_module = nil
    end
  end

  local function insert_modules()
    finish_module()
    if #index_links == 0 then
      return
    end
    result:insert(section_index(index_links, "curriculum-index", "Módulos da estrutura curricular"))
    result:extend(modules)
    modules = pandoc.List()
    index_links = pandoc.List()
  end

  for _, block in ipairs(format_proposal(document.blocks)) do
    if block.tag == "Header" and block.level <= 2 then
      insert_modules()
      in_curriculum = block.identifier == "estrutura-curricular"
    end

    local module_label
    if in_curriculum and block.tag == "Header" and block.level == 3 then
      finish_module()
      module_label = pandoc.utils.stringify(block.content):match("^Módulo %d+")
      if not module_label then
        insert_modules()
      end
    end

    if module_label then
      current_module = pandoc.List({block})
      if #index_links > 0 then
        index_links:insert(pandoc.Space())
      end
      index_links:insert(pandoc.Link(module_label, "#" .. block.identifier))
    elseif current_module then
      current_module:insert(block)
    else
      result:insert(block)
    end
  end

  insert_modules()
  document.blocks = result
  return document
end
