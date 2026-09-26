# Arquitetura de conhecimento do accounting-ops

Glossário dos termos usados para organizar módulos, capacidades e instruções do produto.

## Estrutura

**Skill**:
Capacidade acionável e autocontida, carregada sob demanda para transformar uma entrada em uma saída com sequência, formato e guardrails definidos.
_Evitar_: tratar qualquer arquivo Markdown como skill.

**Pacote de skill**:
Pasta nomeada pelo slug da skill que contém o `SKILL.md` como contrato canônico e pode conter recursos auxiliares quando necessário.
_Evitar_: manter cópias concorrentes do mesmo contrato em arquivos planos.

**Investigação financeira**:
Capability transversal que transforma um sinal, uma discrepância, uma afirmação, uma anomalia ou uma decisão em uma investigação estruturada e sustentada por evidências. Devolve fatos, hipóteses, lacunas, fontes, testes, achados, impacto e ação; pode encaminhar a pergunta para workflows e playbooks especializados, mas não duplica seu conhecimento nem substitui a autoridade fiscal ou contábil responsável.
_Evitar_: tratá-la como sinônimo de explicação de `Variance` ou como autorização para concluir sozinha uma questão tributária.

**Ciclo investigativo**:
Sequência mínima que liga `Sinal`, `Hipótese`, `Evidência`, `Teste`, achado, impacto financeiro e ação ou pergunta pendente.
_Evitar_: saltar de uma hipótese para uma conclusão sem teste discriminante.

**Sinal**:
Observação inicial, pedido, afirmação, diferença, anomalia ou decisão que inicia uma investigação, mas ainda não prova sua causa ou tratamento.
_Evitar_: escrever o sinal como se já fosse um fato explicado.

**Hipótese**:
Explicação candidata que orienta a busca por evidência e pode ser confirmada, refutada ou permanecer inconclusiva.
_Evitar_: promovê-la a fato apenas porque é plausível ou foi declarada por uma área.

**Teste investigativo**:
Procedimento que usa uma evidência capaz de diferenciar hipóteses e produz um resultado classificável.
_Evitar_: chamar uma coleta ampla de documentos, sem critério de decisão, de teste.

**Achado investigativo**:
Resultado de um teste aplicado a uma hipótese. Deve ser classificado como `confirmado`, `refutado` ou `inconclusivo`, conforme a evidência disponível e o critério definido.
_Evitar_: usar `confirmado` para uma explicação apenas plausível ou usar `inconclusivo` sem declarar a evidência que falta.

**Fonte normativa**:
Lei, regulamento, orientação oficial ou outra autoridade aplicável que sustenta um tratamento normativo quando suas condições concretas forem verificadas.
_Evitar_: tratar comentário, prática histórica ou solicitação de fornecedor como fonte suficiente para concluir tratamento tributário.

**Roteamento investigativo**:
Classificação do sinal e seleção do menor conjunto de workflows, playbooks, contexto empresarial ou fontes normativas capaz de testar a hipótese.
_Evitar_: carregar a base inteira ou substituir módulos especializados por uma explicação genérica.

**Workflow**:
Sequência orientada a um problema recorrente de accounting, controladoria ou FP&A, normalmente ligada a uma trilha e a uma situação de trabalho.
_Evitar_: confundir workflow, que conduz um problema, com skill, que aplica uma transformação específica.

**Playbook**:
Orientação aprofundada para conduzir uma situação recorrente, combinando raciocínio, perguntas, critérios e possíveis artefatos de apoio.
_Evitar_: usar playbook como sinônimo de checklist ou de uma transformação curta.

**Conceito**:
Explicação estável de uma ideia de domínio ou de um mecanismo analítico que pode ser reutilizada por workflows, playbooks e skills.
_Evitar_: transformar conceito em roteiro operacional completo.

**Template**:
Formato reutilizável para organizar a saída de uma análise, comunicação ou decisão.
_Evitar_: colocar no template as instruções completas de raciocínio que pertencem a uma skill, workflow ou playbook.

**Decisão de promoção**:
Registro editorial que liga uma fonte a um candidato, destino provável, evidência, confiança, próximo teste e status. Um achado situado continua sendo contexto da empresa até existir uma decisão explícita de generalização.
_Evitar_: confundir a existência de uma boa observação local com método reutilizável já promovido.

**Method wiki**:
Base metodológica viva do produto, organizada em conceitos, processos, padrões, checklists e heurísticas.
_Evitar_: tratá-la como arquivo histórico ou como uma coleção de skills acionáveis.

**Roteador**:
Instrução ou índice que escolhe quais módulos devem ser carregados para uma pergunta. No produto, `CLAUDE.md` é o roteador operacional e `PRODUCT_INDEX.md` é o catálogo navegável.
_Evitar_: duplicar no roteador o conteúdo metodológico dos módulos.
