# Instruções para o Codex — Projeto Keeps | Habilidades do Futuro

> **Status pós-entrega (23/11/2026):** a avaliação técnica foi enviada, conforme informado pela autora. O objetivo das próximas tarefas é manter a documentação e planejar as aulas, não reabrir o teste. Em `main`, a versão da interface ainda é `prototipo/aula-1-1-prumo-prototipo-v2.html`, integrada por `scripts/preparar-site.py`. Uma revisão posterior de progressão foi relatada, mas **não foi localizada nesta branch**. Verificar antes de editar, reverter ou publicar. Consulte `README.md` e `checklist.md`.

## Papel
Atuar como apoio técnico à produção do projeto. Implementar artefatos definidos e revisados pelo responsável pelo Design Instrucional. Não substituir decisões pedagógicas, editoriais ou de escopo.

## Antes de qualquer implementação
1. Ler `AGENTS.md`, `checklist.md`, `docs/GUIA_DI_KEEPS.md` e o enunciado original fornecido pela autora, quando acessível. O PDF do enunciado não está versionado neste repositório. `checklist.md` e `README.md` são retratos de andamento e podem estar desatualizados; confrontar com os arquivos existentes.
2. Identificar a versão em uso da estrutura curricular, da matriz de alinhamento e do roteiro do objeto solicitado.
3. Se houver conflito entre versões ou lacunas materiais, registrar a divergência e pedir decisão antes de alterar o conteúdo.
4. Tratar público-alvo, empresa fictícia e necessidades organizacionais como premissas/simulação, exceto quando houver registro explícito de aprovação.
5. Antes de editar, conferir `git status --short`, declarar os arquivos de entrada e os arquivos a preservar e identificar se a tarefa pede análise, proposta ou implementação. Não iniciar trabalho adicional automaticamente.

## Restrições incontornáveis do teste
- Objeto 1: PDF de boas-vindas — no máximo 2 páginas, preferir 1.
- Objeto 2: vídeo Panorama atual — no máximo 1 minuto, preferir 30 segundos.
- Objeto 3: PPT Globalização — no máximo 5 slides contando capa inicial e final, ou 3 sem capas.
- O módulo 1 inclui uma síntese integradora de competências para o futuro, mas isso não autoriza criar automaticamente um quarto objeto.
- Na etapa de ementa, o enunciado não exige critérios de avaliação nem de certificação.

## Decisões pedagógicas e histórico

- **Currículo proposto vigente:** `02-ementa-cronograma.md`, seis módulos, 28 unidades e três horas estimadas; não equivale a curso completo ou diagnóstico real. `referencias/estrutura_curricular.md` é espelho auxiliar.
- **Módulo 1:** três objetos obrigatórios entregues: PDF de Boas-vindas, MP4 Panorama atual e PPTX Globalização; a síntese 1.4 integra o último slide.
- **Protótipo da Prumo:** demonstração adicional da aula 1.1, com Marina e Lucas. Preservar o cenário e a leitura sem julgamento, sem pontuação ou coleta de respostas. O MP4 complementar já está versionado em `prototipo/midia/`.
- **Referenciais:** ADDIE iterativo, Primeiros Princípios de Merrill como orientação para cenários e 6Ds como perspectiva de aplicação; não alegar transferência, avaliação com público real ou conformidade de acessibilidade não testada.
- **Histórico instrucional:** `docs/REGISTRO_DECISAO_METODOLOGICA.md`, `docs/MATRIZ_DI_MODULO_1_v1_1.md` e `docs/STORYBOARD_INTERFACE_AULA_1_1_v2.md`. Essas versões retratam fases anteriores. Ao localizar eventual revisão mais recente, comparar conteúdos e atualizar os documentos de controle em tarefa específica.
- **Uso de IA:** apoio técnico e editorial, sem substituir decisões pedagógicas da autora; não gerar mídia paga nem alterar escopo sem autorização.

## O que pode fazer
- Transformar roteiro validado em HTML/CSS/JavaScript e componentes reutilizáveis, quando solicitado.
- Preparar estruturas, templates, assets técnicos e scripts de validação.
- Executar checagens de acessibilidade, consistência visual e funcionamento.
- Sinalizar informação faltante, estimativas incertas e problemas de rastreabilidade.

## O que não pode fazer sem aprovação
- Acrescentar módulos, objetos, exercícios ou avaliações não solicitados.
- Alterar objetivos de aprendizagem, hierarquia, público-alvo, conteúdo ou carga horária.
- Inventar estatísticas, pesquisas, fontes, avaliações realizadas ou resultados de aprendizagem.
- Assumir que dados simulados são resultados reais.
- Publicar, excluir ou substituir materiais aprovados sem instrução específica.
- Consumir créditos em plataformas externas, disparar renderização paga, contratar serviços, expor dados privados ou publicar artefatos sem autorização específica.
- Alterar arquivos de um objeto obrigatório por causa de uma proposta ainda não validada de protótipo complementar.

## Critérios de qualidade
- Alinhamento entre objetivo, conteúdo, meio e sequência.
- Linguagem clara e adequada ao público proposto.
- Coerência multimídia: foco, sinalização e pouca informação irrelevante.
- Acessibilidade: bom contraste, alternativas textuais, legendas/transcrição para vídeo, e navegação por teclado quando houver interface web.
- Preservação da fonte e da data para afirmações relevantes.
- Para PPTX/PDF/vídeo, conferir o arquivo efetivo e não somente o roteiro; informar separadamente validações automáticas, revisão visual, testes de reprodução e verificações ainda pendentes.
- Em interface web, prever foco visível, teclado, estados e feedback textuais; em áudio/vídeo, manter alternativas em texto e controle do usuário conforme o recurso.

## Relatório de conclusão de cada tarefa
Informar: (a) arquivos criados/alterados; (b) requisitos atendidos; (c) testes executados e seus resultados; (d) pontos que exigem revisão humana. Não declarar testes ou validações que não tenham sido feitos.

## Referências operacionais após a entrega

1. Ler a ementa (`02-ementa-cronograma.md`) antes de desenvolver aulas. As fichas de `curso/` são **planejamento**, não implementação concluída.
2. Conferir a branch, o commit e os arquivos de entrada. A versão em `main` do protótipo é v2, com montagem via `scripts/preparar-site.py`; não inferir que uma revisão local, não versionada, já está publicada.
3. Preservar os três objetos obrigatórios e o PDF consolidado. A versão inicial da interface, a matriz v1 e os storyboards anteriores são históricos válidos.
4. Para a próxima fase, desenhar objetivo, conteúdo, exemplo, atividade, feedback e requisitos de acessibilidade por aula. Não converter um esqueleto de ficha em conteúdo aprovado.
5. A Prumo é fictícia. Não apresentar participantes, necessidades, aprovação de cliente ou desempenho como reais.
6. Não presumir acesso do Codex a Notion, Figma, Pictory ou outras ferramentas; verificar integrações e permissões.
7. O enunciado original não consta na árvore Git. Caso seja necessário relê-lo, utilizar a cópia fornecida pela autora, sem inventar um caminho local inexistente.

## Hierarquia de decisões

Prevalece o enunciado do exercício para a avaliação já realizada. Para planejamento futuro, partir da ementa vigente e dos objetivos registrados; usar matriz, storyboards e registros de decisão apenas dentro de seus escopos e versões. Em divergência, explicar o conflito em vez de reconciliar silenciosamente. O `checklist.md` distingue pendências técnicas pós-entrega de novas atividades de desenvolvimento.

**Antes de atuar:** verificar status e diff, delimitar os arquivos afetados e preservar os materiais publicados. **Depois:** informar o que mudou, testes realmente executados, limitações e itens que dependem de revisão humana.
