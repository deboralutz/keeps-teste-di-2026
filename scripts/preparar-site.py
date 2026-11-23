#!/usr/bin/env python3
"""Monta os arquivos estáticos para revisão ou publicação autorizada."""

import argparse
from html import escape
from pathlib import Path
import re
import shutil
import subprocess
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
PDF = "05.1-boas-vindas-habilidades-do-futuro.pdf"
PDF_APRESENTACAO = "Debora-Lutz_Teste-Tecnico_Keeps-Learning_Identidade-Site.pdf"
PANORAMA = "05.2-video-panorama-atual.mp4"
PPTX = "05.3-globalizacao-habilidades-do-futuro.pptx"
CENA = "01-01-uma-situacao-comum-no-trabalho.mp4"
PROTOTIPO = "prototipo/aula-1-1-prumo-prototipo-v2.html"

LESSONS = [
    ("", "1.1", "Boas-vindas"),
    ("panorama/", "1.2", "Panorama atual"),
    ("globalizacao/", "1.3", "Globalização"),
]

RESPONSES = [
    ("briefing", "1. Briefing", "01-briefing.md"),
    ("ementa", "2. Ementa e cronograma", "02-ementa-cronograma.md"),
    ("reuniao", "3. Reunião com o cliente", "03-reuniao-com-cliente.md"),
]

SITE_FILES = [
    "index.html",
    "favicon.ico",
    "privacidade/index.html",
    "assets/entrega.css",
    "assets/prumo.css",
    "assets/panorama.js",
    "assets/slides.js",
    "midia/panorama-poster.webp",
    *(f"midia/globalizacao/{i}.webp" for i in range(1, 6)),
]

MATERIALS = {
    PDF: f"midia/{PDF}",
    PDF_APRESENTACAO: f"midia/{PDF_APRESENTACAO}",
    PANORAMA: f"midia/{PANORAMA}",
    PPTX: f"midia/{PPTX}",
    f"prototipo/midia/{CENA}": f"midia/{CENA}",
    "cliente/logo-prumo.png": "midia/logo-prumo.png",
}


def read(path):
    return path.read_text(encoding="utf-8")


def write(output, name, content):
    target = output / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8")


def copy(source, output, name):
    target = output / name
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)


def replace_once(content, before, after):
    if content.count(before) != 1:
        raise ValueError(f"A integração esperava uma ocorrência de {before!r}.")
    return content.replace(before, after, 1)


def course_navigation(active):
    relative = "../" if active else "./"
    to_delivery = "../../" if active else "../"
    items = []
    for route, number, title in LESSONS:
        current = ' aria-current="page"' if route == active else ""
        items.append(f'<li><a href="{relative}{route}"{current}><span>{number}</span> {title}</a></li>')
    links = "\n        ".join(items)
    return f"""<header class="module-header">
      <div class="module-brand">
        <img src="{to_delivery}midia/logo-prumo.png" alt="Prumo Gestão Integrada">
        <div><strong>O trabalho em transformação</strong><span>Habilidades do Futuro · Módulo 1 · Cenário fictício</span></div>
      </div>
      <a class="delivery-link" href="{to_delivery}">← Voltar ao manifesto</a>
    </header>
    <nav class="lesson-nav" aria-label="Aulas do Módulo 1">
      <ul>
        {links}
      </ul>
    </nav>"""


def integrate_v2():
    source = read(ROOT / PROTOTIPO)
    original_header = (
        '<header class="topbar"><div class="brand">Habilidades do Futuro</div>'
        '<div class="course">Módulo 1 · O trabalho em transformação</div></header>'
    )
    guide = f'../midia/{PDF}'
    guide_end = (
        f'<p><a href="{guide}" target="_blank" rel="noopener noreferrer">Abrir guia do curso (PDF, nova aba)</a>'
        f' · <a href="{guide}" download>Baixar PDF</a></p>'
        '<div class="nav"><button type="button" class="btn secondary" data-action="back">Voltar</button>'
        '<a class="btn" href="./panorama/">Aula 1.2 · Panorama atual →</a></div>'
    )
    changes = [
        ("</head>", '<link rel="stylesheet" href="../assets/prumo.css">\n</head>'),
        ('<body>', '<body class="lesson-v2">\n<a class="skip-link" href="#main-content">Ir para o conteúdo</a>'),
        ('\n</div>\n<script>', '\n<footer class="module-footer"><a href="../privacidade/">Privacidade</a></footer>\n</div>\n<script>'),
        (original_header, course_navigation("")),
        ('<main class="mainpanel" id="main-content" tabindex="-1" aria-live="off"></main>',
         '<main class="mainpanel" id="main-content" tabindex="-1"><noscript>'
         '<h1>Boas-vindas e apresentação do curso</h1>'
         '<p>Ative o JavaScript para percorrer a interação. Você também pode '
         f'<a href="{guide}">abrir o guia do curso (PDF)</a> ou '
         '<a href="./panorama/">seguir para a aula 1.2</a>.</p>'
         '</noscript></main>'),
        ('../cliente/logo-prumo.png', '../midia/logo-prumo.png'),
        (f'./midia/{CENA}', f'../midia/{CENA}'),
        ('O vídeo ainda não está disponível neste endereço. Consulte a transcrição a seguir. '
         'O arquivo MP4 deverá ser colocado na pasta <code>prototipo/midia/</code>.',
         'O vídeo não pôde ser carregado. Consulte a transcrição abaixo.'),
        (f'<p><a href="../{PDF}" target="_blank" rel="noopener noreferrer">Abrir guia do curso (PDF)</a></p>'
         "${nav('Voltar','Concluir esta experiência')}", guide_end),
        ('main.focus({preventScroll:true})', "main.querySelector('h1').focus()"),
        ('main.innerHTML=screens[current]();',
         "main.innerHTML=screens[current]();main.querySelector('h1').tabIndex=-1;"
         "main.querySelector('h1').setAttribute('aria-describedby','step-label');"),
        ('</fieldset><div id="feedback"',
         '</fieldset><p id="feedback-status" class="visually-hidden" role="status"></p><div id="feedback"'),
        ('role="status" aria-live="polite"><h2>Vamos examinar a mensagem', '><h2>Vamos examinar a mensagem'),
        ('selection=e.target.value;revealedFeedback=true;',
         "selection=e.target.value;if(!revealedFeedback){document.getElementById('feedback-status').textContent="
         "'Feedback disponível após as alternativas.';}revealedFeedback=true;"),
        ("if(current<4){current++;render();}else{current=1;selection='';revealedFeedback=false;render();"
         "main.querySelector('h1').textContent='Uma situação comum no trabalho';}", "if(current<4){current++;render();}"),
    ]
    for before, after in changes:
        source = replace_once(source, before, after)
    return source


def render_response(markdown, title, back_link=("../../#respostas", "← Voltar às respostas da entrega")):
    source_folder = "https://github.com/deboralutz/keeps-teste-di-2026/blob/main/cliente/"
    for filename in ("CENARIO_FICTICIO.md", "ANEXO_PRUMO_IDENTIDADE_INSTITUCIONAL.md"):
        markdown = markdown.replace(source_folder + filename, "../cenario-ficticio/")
    # Os demais links para anexos privados ficam como texto na versão para a banca.
    markdown = re.sub(
        r"\[([^\]\n]+)\]\(https://github\.com/deboralutz/keeps-teste-di-2026/[^)]+\)", r"\1", markdown
    )
    # Corrige apenas a sintaxe dos dois endereços públicos aninhados na ementa.
    markdown = re.sub(r"\]\(\[referencias/Artigo_0[23]\.md\]\((https://[^)]+)\)\)", r"](\1)", markdown)
    heading = "## Parte II — Anexo técnico: estrutura curricular detalhada"
    has_curriculum = heading in markdown
    if has_curriculum:
        markdown = replace_once(markdown, heading, heading + " {#estrutura-curricular}")
        part_one = "## Parte I — Apresentação do curso e cronograma"
        markdown = replace_once(markdown, part_one, part_one + " {#ementa-cronograma}")

    command = ["pandoc", "--from=markdown-raw_html", "--to=html5", "--wrap=none"]
    if has_curriculum:
        command.extend(("--lua-filter", str(ROOT / "scripts/estrutura-curricular.lua")))
    body = subprocess.run(
        command,
        input=markdown, capture_output=True, text=True, encoding="utf-8", check=True,
    ).stdout
    if has_curriculum:
        toc = ('<nav class="document-nav" aria-label="Partes do documento">'
               '<ul><li><a href="#ementa-cronograma">Parte I · Ementa e cronograma</a></li>'
               '<li><a href="#estrutura-curricular">Parte II · Estrutura curricular detalhada</a></li></ul></nav>')
        body = replace_once(body, "</h1>", f"</h1>\n{toc}\n")
    back_url, back_text = back_link
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)} | Habilidades do Futuro</title>
  <link rel="stylesheet" href="../../assets/entrega.css">
</head>
<body>
  <a class="skip-link" href="#conteudo">Ir para o conteúdo</a>
  <header class="top inner"><a class="signature" href="{escape(back_url)}">{escape(back_text)}</a></header>
  <main class="inner reading" id="conteudo" tabindex="-1">
{body}
  </main>
  <footer class="inner footer reading-footer"><a href="../../privacidade/">Privacidade</a></footer>
</body>
</html>
"""


def populate(output):
    for name in SITE_FILES:
        copy(SITE / name, output, name)
    for original, target in MATERIALS.items():
        copy(ROOT / original, output, target)

    write(output, "curso/index.html", integrate_v2())
    for route, _, _ in LESSONS[1:]:
        name = f"curso/{route}index.html"
        page = replace_once(read(SITE / name), "{{navegacao}}", course_navigation(route))
        if route == "panorama/":
            page = replace_once(page, "{{panorama-texto}}", read(SITE / "curso/panorama/texto.html").strip())
            page = replace_once(page, "{{legendas}}",
                                '<track kind="captions" label="Português (Brasil)" srclang="pt-BR" '
                                'src="../../midia/panorama.pt-BR.vtt">')
            copy(SITE / "midia/panorama.pt-BR.vtt", output, "midia/panorama.pt-BR.vtt")
        write(output, name, page)

    for slug, title, original in RESPONSES:
        write(output, f"respostas/{slug}/index.html", render_response(read(ROOT / original), title))
    scenario = render_response(
        read(SITE / "cenario-ficticio.md"),
        "Cenário fictício — Prumo Gestão Integrada",
        back_link=("../briefing/", "← Voltar ao briefing"),
    )
    write(output, "respostas/cenario-ficticio/index.html", scenario)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destino", type=Path, help="Diretório novo para os arquivos gerados")
    args = parser.parse_args()
    output = args.destino.resolve()
    if output.exists():
        parser.error("Escolha um diretório de destino que ainda não exista.")
    if not shutil.which("pandoc"):
        parser.error("Instale o Pandoc para preparar as três respostas escritas.")
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        with TemporaryDirectory(prefix=".preparar-keeps-", dir=output.parent) as temporary:
            prepared = Path(temporary) / "site"
            populate(prepared)
            prepared.rename(output)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Falha ao preparar o site: {error}\n")
    print(f"Site estático preparado em {output}")


if __name__ == "__main__":
    main()
