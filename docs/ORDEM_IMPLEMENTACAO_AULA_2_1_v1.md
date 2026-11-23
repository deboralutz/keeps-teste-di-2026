# Ordem de implementação — Aula 2.1

**Curso:** Habilidades do Futuro — Comunicação, inteligência artificial e adaptabilidade no trabalho  
**Módulo:** 2 — Comunicação no ambiente profissional  
**Data:** 23/11/2026  
**Decisão:** a responsável pelo projeto **aprovou o roteiro instrucional v1 para implementação**.  
**Status:** implementação **autorizada, mas ainda não executada** por esta ordem. A autorização **não equivale a aprovação de interface ou publicação**.

## Fonte de verdade e precedência

Ler, nesta ordem:

1. [Roteiro instrucional aprovado da aula 2.1 — v1](ROTEIRO_INSTRUCIONAL_AULA_2_1_v1.md): **textos, sequência e comportamentos pedagógicos autorizados**.
2. [Matriz de DI do Módulo 2 — v1](MATRIZ_DI_MODULO_2_v1.md): objetivo, escopo, continuidade e limite estimado de cinco minutos.
3. [Ficha curricular da aula 2.1](../curso/modulo-02-comunicacao-no-ambiente-profissional/aula-2-1-comunicacao-e-colaboracao-entre-equipes.md).
4. [AGENTS.md](../AGENTS.md): regras operacionais, proteção de arquivos e rastreabilidade.
5. [Padrões visuais do site](../site/assets/prumo.css) e código de interface já existente, **somente como referência visual**, não para copiar o exercício da aula 1.1.

A ementa `02-ementa-cronograma.md` continua sendo a fonte curricular. O Módulo 1 e os materiais da avaliação já entregue devem ser preservados.

## Escopo autorizado para o Codex

Implementar **uma prévia funcional e isolada** da aula 2.1, para avaliação humana antes da integração ao percurso. Sugestão de arquivo novo: `prototipo/aula-2-1-prumo-prototipo-v1.html`. Se necessário, criar arquivos CSS ou JavaScript próprios, mantendo links relativos corretos. Não substituir o protótipo 1.1, não editar os três objetos obrigatórios e **não realizar deploy ou alterar a navegação publicada**.

Implementar os seis blocos previstos, com início, conteúdo principal, uma atividade e encerramento. O formato não precisa forçar uma tela por bloco: usar a segmentação que facilite a leitura e o acompanhamento do participante, preservando sequência e conteúdo. Não acrescentar questões, pontuação, conteúdo novo, mídia paga, vídeo, narração ou outros recursos não previstos.

**Visual:** seguir uma identidade editorial sóbria e compatível com a Prumo, aproveitando apenas estilos e recursos já disponíveis ou implementando equivalentes simples. Priorizar legibilidade e espaço útil; não reproduzir artificialmente a estrutura visual antiga da aula 1.1 se ela não atender ao novo roteiro.

**Interação obrigatória:**

- Apresentar alternativas A, B e C exatamente como definidas no roteiro, sem seleção prévia.
- Após a escolha, o botão **“Conferir análise”** revela **somente o feedback da alternativa selecionada**, seguido do mesmo exemplo explicativo do bloco 04.
- O feedback **não deve aparecer antes** da ação de conferir; uma troca de alternativa permite nova conferência, sem exibir feedback desatualizado.
- Permitir retornar, rever e prosseguir sem perder desnecessariamente o contexto.
- Não chamar nenhuma alternativa de “errada”, não atribuir nota, não bloquear a progressão por ter escolhido A ou C.
- A síntese dos três critérios do bloco 05 é **conteúdo**, não um novo quiz.

**Navegação:** quando a aula 2.2 ainda não existir como experiência funcional, o encerramento **não** deve apresentar botão que finja iniciar 2.2 nem link quebrado. Pode anunciar a próxima aula sem controle de avanço e oferecer um retorno válido ao início da prévia ou ao índice acessível, conforme o ambiente local. Só integrar a rota real da 2.2 quando ela estiver disponível e tiver sido autorizada.

## Regras técnicas e de acessibilidade

- Interface em português brasileiro; conteúdo textual disponibilizado sem áudio obrigatório.
- Diagrama **Processos → Projetos → Cliente** com alternativa textual integral, mesma ordem e informação, inclusive em tela pequena.
- Cabeçalhos semânticos, `fieldset`/`legend` ou equivalente para a pergunta, botões com nomes acessíveis, foco visível e navegação por teclado e toque.
- Feedback dinâmico identificado para tecnologias assistivas sem deslocamentos inesperados de foco; evitar dependência exclusiva de cor ou ícones.
- Layout responsivo, preferencialmente funcional em 320, 390, 768 e 1440 px; não introduzir rolagem horizontal.
- Sem cookies opcionais, rastreamento, envio remoto de escolhas, `localStorage` ou serviços externos apenas para essa atividade.
- Prever leitura de conteúdo essencial mesmo se o JavaScript falhar, quando viável; evitar controles sem ação.
- Preservar recursos existentes e não alterar `scripts/preparar-site.py` para adicionar a aula à entrega antes de aprovação específica.

## Critérios de verificação após implementar

1. Os seis blocos previstos estão presentes e mantêm o mesmo objetivo.
2. A aula analisa **dependência entre equipes**, sem simplesmente reproduzir a pergunta da 1.1.
3. Não se atribui a Lucas autoridade de aprovação, nem se inventa que a proposta foi liberada.
4. A alternativa B é a melhor sustentada pelo cenário; os três feedbacks são individuais, contextuais e não punitivos.
5. A explicação posterior distingue arquivo atualizado, revisão final pendente e liberação ainda não confirmada.
6. Seleção, troca de alternativa, botão de conferência e retorno funcionam por teclado, mouse e toque.
7. Os links e ações levam a destinos existentes; a 2.2 permanece anunciada como próxima aula, se ainda não produzida.
8. Layout móvel/desktop e foco foram verificados em condições efetivamente testadas.
9. Medir o tempo de leitura e interação para verificar a hipótese de **cinco minutos**; propor ajuste editorial se a execução for muito maior, sem suprimir a atividade por conveniência.
10. Nenhum arquivo de produção do teste entregue, publicação remota ou roteiro curricular foi modificado incidentalmente.

## Entrega técnica esperada

Ao concluir a implementação, retornar com: caminhos dos arquivos criados/alterados; link ou instruções para abrir a prévia local; descrição do fluxo; resultados dos testes realmente executados; evidências do tempo aferido, se houver; problemas observados; e itens que dependem de aprovação da responsável.

**Não marcar a aula como validada, publicada ou concluída no checklist antes de inspeção humana da prévia.** Esta ordem autoriza **construir e testar**; a liberação para publicação exigirá decisão posterior.
