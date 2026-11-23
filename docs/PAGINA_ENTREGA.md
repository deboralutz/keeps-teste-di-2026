# Página de entrega e protótipo do Módulo 1

> **Registro pós-entrega (23/11/2026):** a autora informou que a avaliação já foi enviada. Este documento descreve a montagem e os testes realizados na versão então inspecionada, não uma nova homologação da revisão de progressão mencionada após a entrega. A branch `main` ainda usa o protótipo v2 no script de montagem; verificar a sincronização antes de novos deploys.

O manifesto reúne as respostas das etapas 1, 2 e 3 e os três objetos obrigatórios. A área `/curso/` apresenta o Módulo 1 da Prumo Gestão Integrada, cenário fictício da avaliação técnica. O percurso curricular de referência tem seis módulos e três horas estimadas.

## Executar localmente

Com Python 3.8 ou superior e Pandoc instalados, execute na raiz do repositório:

```sh
python3 scripts/preparar-site.py ../site-keeps
python3 -m http.server 8000 --bind 127.0.0.1 --directory ../site-keeps
```

Abra [o manifesto](http://127.0.0.1:8000/) ou [o início do Módulo 1](http://127.0.0.1:8000/curso/). Use um diretório de destino novo para cada montagem. O servidor usa somente a pasta gerada.

Na versão registrada em `main` em 23/11, a montagem deriva a aula 1.1 do HTML v2 e converte as três respostas Markdown em HTML. Os links do briefing e da ementa para a Prumo apontam para `/respostas/cenario-ficticio/`, uma síntese pública de seu perfil, identidade institucional e papel no curso. Os demais links para anexos internos ficam como texto. Duas referências públicas da ementa tiveram a sintaxe de link normalizada na renderização. O script copia os objetos em seus formatos originais e inclui somente os arquivos necessários ao site. A pasta gerada roda em um servidor estático, sem dependências de execução no servidor ou no navegador.

## Fontes e conferência

Foram conferidos `AGENTS.md`, `README.md`, `checklist.md`, o guia de DI, a ementa, seu espelho curricular, a matriz v1.1 e os storyboards de Boas-vindas, Panorama atual e interface v2. Para Globalização, a referência implementada foi o PPTX existente. O esquema preliminar na matriz é histórico. O antigo template `03-slides-globalizacao.md` foi retirado da árvore corrente por estar ultrapassado; seu conteúdo continua no histórico do Git.

| Critério | Resultado e evidência |
| --- | --- |
| Comparação com o enunciado original | Não verificável. O arquivo `avaliacao-tecnica-keeps.pdf` citado no projeto não está no repositório. A numeração 1, 2, 3 e 5 segue o README. |
| Currículo e Boas-vindas | A ementa vigente soma 180 minutos em seis módulos. A edição v2 do PDF foi preparada a partir do arquivo exportado e mantém uma página A4. O segundo parágrafo inclui análise e melhoria de processos, e a lista segue os seis módulos da ementa. A pergunta de abertura foi preservada. O arquivo anterior foi conservado no repositório e o site usa a nova edição no mesmo endereço. |
| Aula 1.1 | O MP4 já está versionado no caminho indicado no storyboard, apesar da pendência de upload registrada. Duração técnica de 16,60 s, vídeo H.264 e áudio AAC. A página integrada preserva transcrição, pergunta, feedback, desfecho e reflexão. |
| Panorama atual | O arquivo de referência e a cópia com dupla extensão têm o mesmo blob. A cópia utilizada tem 44,97 s, vídeo H.264 e áudio AAC. A narração difere do storyboard proposto e o MP4 inclui marca e tela final do Pictory. A alternativa textual e as legendas da página foram preparadas a partir do vídeo existente. |
| Globalização | O PPTX tem cinco slides. A síntese 1.4 está no quinto, com quatro cartões e a pergunta sobre uma entrega que envolve diferentes países. Foram encontrados quatro hyperlinks nos slides 2, 3 e 4. A página usa imagens exportadas com Inter e Montserrat em LibreOffice, oferece texto e links de referência e disponibiliza o PPTX original. |

## Verificação técnica

- **Montagem e escopo.** Oito páginas HTML e 24 arquivos no total. As três peças obrigatórias, o vídeo complementar e o logotipo da Prumo conferem por SHA-256 com os respectivos arquivos-fonte. A montagem recusou um diretório já existente.
- **HTTP e layout.** 40 URLs locais distintas, incluindo links com fragmentos, responderam com HTTP 200 e os alvos de âncora foram conferidos. As sete páginas foram testadas em Chromium nas larguras de 320, 390, 768 e 1.440 px, sem rolagem horizontal. O manifesto, o protótipo e as prévias dos materiais foram inspecionados visualmente.
- **Teclado e fluxo.** Foram verificadas a navegação por Tab, Enter, Espaço e setas, a indicação da aula atual, o foco na mudança de tela ou slide, a seleção sem resposta predefinida, a retenção da escolha ao voltar e a revelação do desfecho somente após escolher uma interpretação. A síntese abre pelo endereço `/curso/globalizacao/#sintese`. Os cinco slides e seus textos ficam disponíveis mesmo com JavaScript desativado.
- **Mídia e downloads.** Os dois MP4 carregaram, pausaram, aceitaram busca e reproduziram até o fim em Chromium com velocidade acelerada. O navegador reconheceu a faixa WebVTT de Panorama atual e seus dez trechos. Ambos os vídeos foram decodificados integralmente com FFmpeg. Com os MP4 bloqueados no navegador, as alternativas textuais abriram automaticamente. Os downloads de PDF e PPTX foram comparados com os arquivos originais.

## Verificações anotadas antes da entrega — histórico

Os pontos abaixo foram registrados durante a revisão anterior ao envio. Permanecem como ressalvas de qualidade para eventual reuso, **não como tarefas que impeçam ou reabram a entrega realizada**.

- A responsável pelo DI deve conferir a versão escrita consolidada externa e decidir como disponibilizá-la. O manifesto usa as três respostas atualmente versionadas.
- Conferir a acessibilidade do PDF de Boas-vindas com tecnologia assistiva. A edição v2 mantém texto selecionável e a ordem de leitura, e o arquivo segue sem marcação estrutural.
- Revisar a locução e a sincronização das legendas com escuta humana em velocidade normal. Conferir acessibilidade do PPTX no PowerPoint e das páginas com tecnologia assistiva e em navegador móvel real.
- Confirmar a liberação dos materiais e definir domínio e permissões de acesso à banca. Após publicação autorizada, validar a experiência no endereço definitivo e nas condições de acesso dos avaliadores.

## Cloudflare Pages com domínio personalizado — procedimento de publicação registrado

O endereço da entrega foi informado como já utilizado. O roteiro abaixo é histórico e pode ser consultado se houver necessidade de nova publicação, após conferir a versão do código:


1. Gere a pasta estática e confira os arquivos localmente. Use como origem de upload somente a pasta gerada, com `index.html` na raiz.
2. No painel da Cloudflare, abra **Workers & Pages**, crie um projeto **Pages** por **Direct Upload** e envie a pasta gerada. Essa modalidade usa os arquivos já preparados e não exige integração com o GitHub. A URL `<projeto>.pages.dev` passa a servir o pacote após o deploy. [Documentação de Direct Upload](https://developers.cloudflare.com/pages/get-started/direct-upload/)
3. No projeto, abra **Custom domains → Set up a domain** e associe primeiro o domínio ou subdomínio escolhido. Para um subdomínio em DNS externo, crie um registro **CNAME** para `<projeto>.pages.dev` após a associação. Se o DNS do domínio estiver na Cloudflare, confirme o registro proposto pelo painel. Para usar o domínio raiz, a zona deve estar na mesma conta e usar os nameservers da Cloudflare. [Documentação de domínios personalizados](https://developers.cloudflare.com/pages/configuration/custom-domains/)
4. Aguarde a ativação do domínio e do HTTPS. Verifique o manifesto, as três respostas, `/curso/`, os dois vídeos, a síntese 1.4 e os downloads. Confirme o acesso da banca em uma janela sem sua sessão e, se a entrega for restrita, aplique o controle de acesso também aos endereços Pages usados para servir o projeto.
