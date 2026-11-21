# Storyboard de interface — Aula 1.1: O que foi dito? O que foi compreendido?

**Projeto:** Avaliação técnica — Designer Instrucional | Keeps  
**Curso:** Habilidades do Futuro — Comunicação, inteligência artificial e adaptabilidade no trabalho  
**Módulo:** 1 — O trabalho em transformação  
**Unidade:** 1.1 — Boas-vindas e apresentação do curso  
**Objeto:** protótipo **complementar**, web, autoinstrucional e interativo  
**Versão:** 1.0 — 21/11/2026  
**Status:** **roteiro e sequência aprovados pela responsável pelo DI para prototipação**; a validação visual, a usabilidade, a adequação do ritmo e possíveis revisões editoriais ocorrerão após a primeira implementação. **Nenhum protótipo funcional ou teste de usuário é declarado concluído por este registro.**  
**Escopo:** quatro telas. O documento autoriza usar o roteiro na prototipação da interface, **não** autoriza publicação, contratação, geração de mídia paga ou substituição de objeto obrigatório.

## 1. Função instrucional e alinhamento

**Função:** iniciar a experiência com uma situação profissional de comunicação ambígua, na qual uma informação explícita permite inferências diferentes. Convidar o participante a interpretar a mensagem antes de conhecer sua consequência, reconhecer a necessidade de confirmação e situar o percurso do curso.

**Intenção pedagógica da interação:** distinguir, em nível introdutório, o que foi explicitamente comunicado, o que se inferiu e o que ainda precisava ser confirmado. A interação **não comprova domínio da competência de comunicação**.

**Referenciais adotados:**
- ADDIE iterativo para o desenvolvimento e revisão;
- Primeiros Princípios de Instrução de Merrill: problema significativo e ativação dos conhecimentos prévios, com retomadas possíveis ao longo do curso;
- 6Ds como perspectiva de aplicação no trabalho, sem alegar transferência comprovada;
- LXD e aprendizagem baseada em cenário profissional recorrente (*scenario-based learning*) para o desenho da experiência.

**Cenário:** Prumo Gestão Integrada, empresa **fictícia** de gestão, estruturação e melhoria de processos empresariais. Marina trabalha em Projetos; Lucas, em Processos. A situação é uma simulação criada para fins de avaliação técnica.

**Relação com as entregas obrigatórias:** o **PDF de boas-vindas continua sendo o Objeto 1 exigido** (preferencialmente uma página, máximo duas). Este protótipo web é uma demonstração adicional da aula 1.1, que não substitui o PDF nem altera sua redação. O vídeo 1.2, *Panorama atual*, e o PPT 1.3, *Globalização*, também permanecem independentes. Não criar quarto objeto obrigatório.

## 2. Direção de experiência e interface

- **Abordagem visual:** editorial contemporânea, sóbria, com conversa profissional legível e revelação progressiva. Manter coerência geral com a identidade já adotada no PDF e na apresentação, sem reconstruir esses arquivos.
- **Sem gamificação:** sem pontos, medalhas, cronômetros, rankings, moedas, vidas, avatares de jogo ou mensagens de vitória/fracasso. “Tela 1 de 4” é apenas orientação de navegação, não pontuação.
- **Interação formativa:** uma escolha interpretativa, seguida de feedback explicativo não punitivo; nenhuma nota, classificação ou coleta obrigatória de dados pessoais.
- **Tecnologia:** interface web responsiva, independente de LMS/LXP/SCORM, sem integração externa obrigatória.
- **Áudio:** **não incluir nesta versão inicial**. A possibilidade de falas sintetizadas com HeyGen será analisada depois da revisão visual; se adotada, deverá ser opcional, sem reprodução automática e com texto integral preservado.
- **Movimento:** se houver, usar transições discretas, respeitar preferência por redução de movimento e nunca depender de animação para comunicar informação essencial.

## 3. Mapa da sequência

**Tela 1 — observar a conversa** → **Tela 2 — interpretar e ler o feedback** → **Tela 3 — conhecer o desdobramento** → **Tela 4 — refletir e seguir para o panorama**.

O desfecho **não pode aparecer antes** de o participante fazer sua interpretação na Tela 2. O feedback dessa tela pode explicar o limite da informação, mas não deve antecipar que Marina enviou o documento nem que havia revisão pendente.

### Tela 1 — Apresentação do diálogo

**Título exibido:** Uma situação comum no trabalho

**Texto exibido:**

> Na Prumo Gestão Integrada, a equipe está preparando uma proposta para um cliente.
>
> **Marina — Projetos**  
> Já podemos enviar a proposta revisada ao cliente?
>
> **Lucas — Processos**  
> Coloquei a versão atualizada na plataforma ontem.

**Propósito:** apresentar contexto e conversa sem comentar ainda sua ambiguidade nem atribuir erro a alguém.

**Composição de interface:** cabeçalho discreto “Habilidades do Futuro · Módulo 1”; bloco de contexto; duas mensagens claramente identificadas por nome e área; espaçamento confortável. Não depender da posição ou da cor dos balões para identificar quem fala.

**Ação primária:** botão **Continuar**.

**Comportamento:** só avança para a Tela 2 por ação do participante; nenhuma revelação automática.

### Tela 2 — Pergunta ao participante

**Título exibido:** O que a resposta de Lucas permite concluir?

**Enunciado exibido:** Escolha a alternativa que melhor representa sua interpretação da mensagem.

**Alternativas exibidas, em seleção única:**

- **A.** A proposta já está pronta para ser enviada ao cliente.
- **B.** Lucas informou que atualizou um arquivo, mas isso não confirma que a proposta esteja pronta para envio.
- **C.** Não é possível compreender nada a partir da resposta de Lucas.

**Tratamento pedagógico:** a alternativa **B** é a interpretação mais bem sustentada pela mensagem. A infere uma aprovação que não foi afirmada; C desconsidera a informação explícita sobre a atualização do arquivo. **Não exibir “certo/errado”, nota, pontuação ou ranking.** Essa distinção orienta a revisão editorial do feedback, não uma avaliação formal.

**Feedback comum aprovado, exibido após a escolha:**

> A resposta de Lucas informa que uma versão atualizada foi colocada na plataforma. Mas ela não confirma, por si só, que a proposta já esteja pronta para envio.
>
> Em situações de trabalho, decisões podem ser tomadas a partir de interpretações que parecem óbvias, mas que ainda precisariam de confirmação.

**Ação primária, após seleção e feedback:** botão **Ver o que aconteceu**.

**Comportamento da interface:**
1. Nenhuma alternativa pré-selecionada.
2. O participante escolhe A, B ou C; a seleção fica visível e o feedback surge abaixo das alternativas.
3. A mesma explicação formativa aparece para todas as escolhas nesta versão, sem corrigir a pessoa de forma punitiva.
4. O botão para avançar só fica disponível depois de uma escolha; não bloquear a leitura das alternativas ou o retorno à Tela 1.
5. Alterar a escolha atualiza o estado de seleção, sem duplicar feedback nem navegar automaticamente.
6. A consequência do caso fica reservada à Tela 3.

### Tela 3 — Revelação da consequência

**Título exibido:** O que aconteceu depois

**Texto exibido:**

> Marina interpretou que a proposta já poderia ser enviada e encaminhou o arquivo ao cliente.
>
> Mais tarde, Lucas esclareceu que a versão atualizada ainda precisava de uma revisão final antes do envio.
>
> O problema não surgiu, necessariamente, por falta de esforço ou de boa vontade. Ele surgiu porque a mensagem permitiu uma inferência que não foi confirmada.

**Propósito:** revelar uma consequência possível da inferência, sem transformar Marina ou Lucas em personagens culpados.

**Composição de interface:** continuidade visual da conversa e indicação temporal discreta, por exemplo, um documento enviado e uma indicação textual “revisão final pendente”. A sequência precisa ser compreensível somente pela leitura, sem setas/ícones indispensáveis.

**Ação primária:** botão **Refletir sobre a situação**.

**Comportamento:** a tela é acessada apenas depois da interpretação na Tela 2. Não adicionar perguntas avaliativas ou um segundo desafio.

### Tela 4 — Reflexão final e transição

**Título exibido:** Por que começar por essa situação?

**Texto exibido:**

> No trabalho, mensagens, documentos, processos e ferramentas digitais estão constantemente se cruzando.
>
> Uma informação pode parecer suficiente e, ainda assim, gerar interpretações diferentes.
>
> Ao longo deste curso, vamos ampliar esse olhar para compreender:
>
> - como a **comunicação** influencia o entendimento entre pessoas;
> - como **tecnologias e inteligência artificial** participam dos processos de trabalho;
> - como a **organização da informação** ajuda a reduzir ambiguidades;
> - e por que a **adaptabilidade** se torna cada vez mais importante.
>
> **A seguir, vamos ampliar essa situação e observar como o trabalho está se transformando.**

**Propósito:** fechar o caso e mostrar a relação com os próximos conteúdos, sem apresentar todas as explicações do curso.

**Ação primária prevista:** botão **Ir para Panorama atual**.

**Regra para a implementação:** usar essa ação somente quando existir destino funcional confirmado para o vídeo/objeto 1.2. Enquanto esse destino não estiver integrado, manter a tela de encerramento e oferecer uma ação real de **Concluir esta experiência**, sem criar link falso ou botão sem função. A alternativa de integração **não altera o texto pedagógico aprovado**.

## 4. Requisitos de interação e acessibilidade para Codex

1. Implementar **exatamente quatro telas**, com transições acionadas pelo participante. Não acrescentar quiz, pontuação, cadastro, medalha, ranking ou atividade extra.
2. Usar controles semânticos, navegação por teclado, foco visível, estados discerníveis e rótulos acessíveis. A seleção pode ser feita por um grupo de opções do tipo radio.
3. Exibir o feedback como texto no fluxo da leitura; sinalizar sua inserção adequadamente a tecnologias assistivas, sem deslocar o foco de forma inesperada.
4. Manter hierarquia de títulos, ordem de leitura, contraste legível e largura confortável para desktop e celular; não cortar mensagens nem opções.
5. Não transmitir identidade de falante, seleção ou estado apenas por cor, animação ou som.
6. O protótipo deve permitir revisão visual posterior: textos e estilos preferencialmente editáveis, componentes simples e alterações rastreáveis.
7. Não coletar nem enviar respostas do participante a servidores. O estado de seleção pode permanecer apenas na sessão da interface. Não declarar medição ou armazenamento de aprendizagem.
8. Se oferecer navegação de retorno, preservar a escolha da Tela 2 durante a sessão e não mostrar o desfecho antes do primeiro avanço legítimo; não exigir que o participante refaça a seleção ao voltar.
9. Nenhuma dependência de geração de áudio, vídeo, voz sintética, plataformas pagas, domínio público, SCORM ou LMS para a primeira versão.
10. Não usar logomarca da Keeps nem presumir identidade oficial da empresa fictícia. Conferir licenças de qualquer recurso incorporado.
11. Não alterar automaticamente textos aprovados. Divergência de conteúdo ou de escopo deve ser apontada antes de implementar.

## 5. Critérios de aceite do protótipo (a verificar, ainda não realizados)

- [ ] As quatro telas seguem a ordem e exibem os textos definidos neste storyboard.
- [ ] A consequência permanece oculta até depois da interpretação.
- [ ] A seleção única funciona sem pré-seleção; o feedback aparece apenas após escolha.
- [ ] O feedback é compreensível para A, B e C, sem mensagem punitiva, nota ou correção automática.
- [ ] Os botões avançam para destinos reais; o último não aponta para endereço inexistente.
- [ ] Layout e leitura funcionam em viewport móvel e desktop.
- [ ] Navegação por teclado, foco visível, nomes de controles e feedback textual foram inspecionados.
- [ ] Não existe autoplay, consumo de créditos, envio de respostas ou dependência de mídia gerada.
- [ ] O protótipo e o PDF obrigatório permanecem arquivos distintos.
- [ ] Revisão humana observa clareza da narrativa e ritmo de leitura antes de aprovar uma versão final.

## 6. Orientação de implementação e versionamento

**Entradas para o Codex:** este storyboard; `AGENTS.md`; `docs/DECISAO_ESTRATEGIA_AULA_1_1_MULTIMIDIA_v1.md`; `docs/REGISTRO_DECISAO_METODOLOGICA.md`; `docs/MATRIZ_DI_MODULO_1_v1_1.md`; `docs/GUIA_DI_KEEPS.md`.

**Proteger sem alterações:** `docs/STORYBOARD_PDF_BOAS_VINDAS_v1.md`, o PDF já produzido, `docs/STORYBOARD_VIDEO_PANORAMA_ATUAL_v1.md`, o PPT de Globalização e a estrutura curricular. **Não iniciar a implementação apenas por existir este arquivo**; a execução será solicitada em tarefa específica.

**Status de aprovação:** aprovado para construir e inspecionar um **protótipo v1**. Isso **não equivale** à aprovação final de interface, acessibilidade ou publicação. Após visualizar o funcionamento, a responsável pelo DI poderá solicitar ajustes de redação, feedback, layout ou fluxo; registrar mudanças como revisão v1.1 ou posterior, sem sobrescrever silenciosamente o roteiro aprovado.

**Próxima decisão multimídia:** somente depois de examinar o protótipo textual, decidir se áudio sintético de HeyGen acrescenta valor e como testá-lo sem induzir a interpretação; nenhuma voz ou crédito está aprovado para geração nesta etapa.

**Relatório esperado do Codex ao implementar:** arquivos criados/alterados; testes efetivos e resultados; eventuais divergências; limitações de acessibilidade; pendências de aprovação humana. Não inventar validações.
