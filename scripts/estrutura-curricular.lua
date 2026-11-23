local function with_role(role, identifier, attributes)
  attributes = attributes or {}
  attributes.role = role
  return pandoc.Attr(identifier or "", {}, attributes)
end

local function header_cell(text)
  return pandoc.Cell({pandoc.Plain(text)}, "AlignDefault", 1, 1, with_role("columnheader", nil, {scope = "col"}))
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
    local title = pandoc.Cell(
      {pandoc.Plain(lesson.heading.content)}, "AlignDefault", 1, 1,
      with_role("rowheader", lesson.heading.identifier, {scope = "row"})
    )
    local description = pandoc.Cell(
      lesson.description, "AlignDefault", 1, 1, with_role("cell")
    )
    rows[#rows + 1] = pandoc.Row({title, description}, with_role("row"))
  end

  local headers = pandoc.Row({header_cell("Aula"), header_cell("Conteúdo e atividades")}, with_role("row"))
  content:insert(pandoc.Table(
    {long = {}},
    {{"AlignDefault", 0.36}, {"AlignDefault", 0.64}},
    pandoc.TableHead({headers}, with_role("rowgroup")),
    {{attr = with_role("rowgroup"), row_head_columns = 1, head = {}, body = rows}},
    pandoc.TableFoot({}),
    pandoc.Attr("", {"curriculum-table"}, {role = "table", ["aria-label"] = pandoc.utils.stringify(heading.content)})
  ))
  return pandoc.List({pandoc.Div(content, pandoc.Attr("", {"curriculum-module"}))})
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
    result:insert(pandoc.Div(
      {pandoc.Para(index_links)},
      pandoc.Attr("", {"curriculum-index"}, {role = "navigation", ["aria-label"] = "Módulos da estrutura curricular"})
    ))
    result:extend(modules)
    modules = pandoc.List()
    index_links = pandoc.List()
  end

  for _, block in ipairs(document.blocks) do
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
