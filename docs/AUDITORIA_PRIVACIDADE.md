# Auditoria de privacidade da entrega Keeps

O escopo inclui o manifesto, as respostas, o cenário fictício, as três páginas do protótipo e os materiais servidos pelo site. A apresentação é pública, autoral e demonstrativa. A Prumo é fictícia e a Keeps Learning é a destinatária da avaliação técnica.

## Evidências

| Área | Código e pacote estático | Site publicado e infraestrutura |
| --- | --- | --- |
| Cookies e armazenamento | Não há lógica de cookies, `localStorage`, `sessionStorage`, IndexedDB, Cache Storage ou service worker. | Em dois perfis novos de Chromium, nas larguras de 390 e 1.440 px, nenhuma das oito páginas anteriores ao aviso enviou cabeçalho `Set-Cookie`. Os perfis permaneceram sem cookies, entradas de armazenamento ou service workers. A observação cobre o fluxo testado e não determina o comportamento da infraestrutura em toda condição de tráfego. |
| Analytics, publicidade e requisições | Não há scripts de análise ou publicidade, pixels, iframes, fontes remotas ou chamadas da aplicação a APIs externas. Vídeos, imagens, legendas e materiais são locais. A tipografia usa fontes do sistema. | Na navegação testada, o navegador fez apenas requisições GET ao próprio domínio. O projeto Pages não tem tag ou token de Web Analytics configurado, e a consulta de sites de Web Analytics na conta não retornou registros. |
| Campos e respostas | A atividade 1.1 usa três opções de rádio. A escolha fica em variáveis JavaScript da página para renderizar o feedback. A estrutura não inclui cadastro nem formulário. | A seleção das três alternativas, a abertura do desfecho e a reflexão não geraram requisições de rede. |
| Referências externas | Há hyperlinks nas respostas, nos slides e em materiais para download. Eles são acionados pelo visitante. | Nenhum destino externo foi carregado automaticamente durante a navegação testada. |
| Hospedagem | A montagem usa apenas arquivos estáticos, sem Pages Functions, integração de dados ou armazenamento de visitas no código do site. | Cloudflare Pages confirmado. O acesso envolve dados técnicos de conexão e requisição. O painel consultado não permitiu confirmar se há conservação de registros pelo provedor, sua duração ou o local de cada operação de processamento. |

## Decisões e bases legais

- **Aviso de Privacidade em `/privacidade/`.** Identifica a responsável, descreve a finalidade, o tratamento técnico e a atividade local. Inclui o canal autorizado pela responsável para exercício de direitos. As páginas de entrada do site têm um link no rodapé.
- **Sem banner de consentimento.** A inspeção não encontrou cookies opcionais ou tecnologias que precisassem ser interrompidas até o consentimento. Se novas ferramentas de análise, publicidade ou incorporação forem adotadas, refazer a auditoria antes de ativá-las.
- **Sem página de Termos de Uso.** O conteúdo disponível é demonstrativo e não há cadastro, contratação, pagamentos ou publicação de conteúdo por visitantes. A identificação do projeto e do cenário fictício já aparece na página.
- **Entrega e proteção técnica.** A avaliação de legítimo interesse considera a finalidade específica de servir e proteger a apresentação, a necessidade dos dados de conexão e de requisição para atender ao pedido do visitante e a expectativa comum de que a infraestrutura receba esses dados. As salvaguardas verificadas são a ausência de perfil publicitário ou analítico no site, as escolhas do protótipo em memória, a transparência e o canal de contato. Base adotada para esse tratamento técnico, arts. 7º, IX, e 10 da LGPD.
- **Exercício de direitos.** O atendimento a pedidos LGPD recebidos pelo canal autorizado se apoia no cumprimento das obrigações legais pertinentes, incluindo os arts. 7º, II, e 18.

## Pontos para validação humana

- Confirmar com o provedor as condições de eventual conservação de registros técnicos e os mecanismos contratuais aplicáveis ao processamento internacional. O aviso informa a possibilidade de processamento fora do Brasil e remete às informações do provedor. Não declara prazo nem mecanismo não confirmado.
- Rever a avaliação de legítimo interesse e o texto do aviso se mudarem o público, a infraestrutura, as finalidades ou o uso de dados. Confirmar internamente o procedimento para pedidos de titulares e a conservação das mensagens, sem presumir um prazo.

## Verificação da versão com o aviso

A montagem gerou nove páginas. Em Chromium a 320, 390, 768 e 1.440 px, os links do rodapé abriram o aviso por teclado com foco visível. A página do aviso passou nas verificações automatizadas executadas com axe. A comparação da montagem preservou o conteúdo e os links existentes, e os materiais e scripts do protótipo conferiram byte a byte.

O fluxo de teste com o aviso percorreu as nove páginas, iniciou os dois vídeos e acionou as três respostas da aula 1.1. Não foram observados erros no console, chamadas externas automáticas ou envio das escolhas. Requisições de mídia foram canceladas em navegação, com a reprodução iniciada nos dois players.

## Referências

- [Lei nº 13.709/2018, texto atualizado na Câmara dos Deputados](https://www2.camara.leg.br/legin/fed/lei/2018/lei-13709-14-agosto-2018-787077-normaatualizada-pl.html)
- [ANPD, guia de cookies e proteção de dados pessoais](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia-orientativo-cookies-e-protecao-de-dados-pessoais.pdf/@@download/file)
- [ANPD, guia sobre legítimo interesse](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_legitimo_interesse.pdf/@@download/file)
- [Cloudflare, aviso de privacidade](https://www.cloudflare.com/privacypolicy/) · [Cloudflare, documentação de cookies](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/)
