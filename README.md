# Avaliação técnica — Design Instrucional | Keeps

**Projeto:** Habilidades do Futuro — Comunicação, inteligência artificial e adaptabilidade no trabalho.  
**Situação:** avaliação técnica **entregue em 23/11/2026**, conforme informado pela autora. A documentação segue disponível para consulta e para o planejamento posterior das aulas.  
**Cenário didático:** Prumo Gestão Integrada, organização fictícia; não houve diagnóstico aplicado a um cliente real.

> **Estado do GitHub em 23/11/2026:** a branch `main` contém o protótipo **v2** da aula 1.1, com quatro telas, referenciado por `scripts/preparar-site.py`. A autora informa que o Codex realizou nova revisão da progressão pedagógica, mas essa versão **ainda não foi localizada na branch `main`** durante a revisão documental. Não confundir a entrega já realizada com a sincronização posterior do código. Consulte [o checklist](checklist.md).

## Entrega realizada

O exercício abrange as respostas às etapas **1, 2 e 3** e três objetos do Módulo 1, especificados na etapa **5** do enunciado original. A numeração é a do teste; não há uma etapa 4 adicional. O enunciado foi recebido externamente e **não está versionado neste repositório**.

### Respostas escritas

- [1 — Briefing](01-briefing.md): organização da demanda, lacunas e primeiros passos.
- [2 — Ementa e cronograma](02-ementa-cronograma.md): seis módulos, 28 unidades planejadas, três horas estimadas e cronograma preliminar de produção.
- [3 — Reunião com o cliente](03-reuniao-com-cliente.md): análise de alterações solicitadas, diálogo consultivo e impactos sobre escopo e prazo.
- [PDF de apresentação consolidado](Debora-Lutz_Teste-Tecnico_Keeps-Learning_Identidade-Site.pdf): documento de apresentação disponibilizado para a entrega.

### Objetos obrigatórios — Módulo 1

| Objeto | Arquivo | Situação no repositório |
| --- | --- | --- |
| 5.1 — Boas-vindas | [PDF](05.1-boas-vindas-habilidades-do-futuro.pdf) | Arquivo disponível, uma página |
| 5.2 — Panorama atual | [Vídeo MP4](05.2-video-panorama-atual.mp4) | Arquivo disponível; reprodução e legendas relatadas na [auditoria de montagem](docs/PAGINA_ENTREGA.md) |
| 5.3 — Globalização | [PPTX](05.3-globalizacao-habilidades-do-futuro.pptx) | Arquivo disponível, cinco slides, incluindo a síntese |

O item curricular **1.4 — Competências para o futuro** é a síntese integrada ao último slide de Globalização, **não** um quarto objeto obrigatório. Os relatórios técnicos registram testes realizados nas versões inspecionadas; não constituem validação de revisões posteriores.

### Apresentação digital e complemento

- [Página de entrega](https://keeps.deboralutz.com.br/) — manifesto e acesso aos materiais.
- [Protótipo do Módulo 1](https://keeps.deboralutz.com.br/curso/) — demonstração adicional, não substitui os três objetos.
- [Código-fonte do protótipo v2](prototipo/aula-1-1-prumo-prototipo-v2.html) — versão atualmente registrada na `main`; [v1 histórica](prototipo/aula-1-1-prumo-prototipo-v1.html).
- [Documentação da montagem e dos testes](docs/PAGINA_ENTREGA.md) e [auditoria de privacidade](docs/AUDITORIA_PRIVACIDADE.md).

A página publicada não é um LMS nem representa o curso completo em operação.

## Organização para continuidade

- [curso/](curso/README.md): seis módulos e 28 fichas de aula. **Módulos 2 a 6 estão planejados; não são aulas integralmente produzidas.** É o ponto de partida para a próxima fase de roteirização.
- [Ementa vigente](02-ementa-cronograma.md): fonte principal de objetivos, conteúdos, ordem e duração.
- [Matriz do Módulo 1](docs/MATRIZ_DI_MODULO_1_v1_1.md): matriz da fase de produção do teste; verificar futura revisão da interface antes de tomá-la como retrato da experiência atual.
- [docs/](docs/): storyboards, decisões metodológicas, notas de produção e relatórios. Versões anteriores são preservadas como **histórico**, não como instruções vigentes.
- [cliente/](cliente/CENARIO_FICTICIO.md): informações sobre a Prumo, cenário simulado.
- [referencias/](referencias/LEIA-ME.md): bibliografia de estudo e consultas; [cautelas de curadoria](links-e-notas.md).
- [checklist.md](checklist.md): separa a entrega encerrada das verificações e do planejamento futuro.
- [AGENTS.md](AGENTS.md): limites operacionais para eventuais trabalhos com Codex.

O [espelho curricular](referencias/estrutura_curricular.md) é auxiliar; em divergências, prevalece a Parte II da ementa. Os documentos históricos v1/v2 não devem ser confundidos com uma eventual versão mais recente ainda não sincronizada.

## Montagem do site

A versão versionada em `main` é montada com Python e Pandoc:

```sh
python3 scripts/preparar-site.py ../site-keeps
python3 -m http.server 8000 --bind 127.0.0.1 --directory ../site-keeps
```

Utilize um diretório de saída novo. O processo gera a página com os materiais disponíveis e **não publica automaticamente em produção**. Procedimentos e ressalvas: [docs/PAGINA_ENTREGA.md](docs/PAGINA_ENTREGA.md).

## Próxima fase: planejamento das aulas

Retomar as fichas do diretório `curso/` e alinhar objetivos, exemplos, prática, feedback e recursos antes de solicitar implementação. As condições do público, o escopo completo e a carga horária ainda são **premissas da proposta**, não validações de um cliente real.

**Nota de conservação:** versões históricas de interface, matrizes e storyboards permanecem no repositório para rastreabilidade. O template inicial de slides, sem conteúdo aprovado, e a duplicata binária do PDF de apresentação foram retirados da árvore corrente na limpeza documental de 23/11; seu histórico continua disponível no Git.
