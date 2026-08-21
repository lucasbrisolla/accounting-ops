# Arquitetura de conhecimento do accounting-ops

Glossário dos termos usados para organizar módulos, capacidades e instruções do produto.

## Estrutura

**Skill**:
Capacidade acionável e autocontida, carregada sob demanda para transformar uma entrada em uma saída com sequência, formato e guardrails definidos.
_Evitar_: tratar qualquer arquivo Markdown como skill.

**Pacote de skill**:
Pasta nomeada pelo slug da skill que contém o `SKILL.md` como contrato canônico e pode conter recursos auxiliares quando necessário.
_Evitar_: manter cópias concorrentes do mesmo contrato em arquivos planos.

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

**Method wiki**:
Base metodológica viva do produto, organizada em conceitos, processos, padrões, checklists e heurísticas.
_Evitar_: tratá-la como arquivo histórico ou como uma coleção de skills acionáveis.

**Roteador**:
Instrução ou índice que escolhe quais módulos devem ser carregados para uma pergunta. No produto, `CLAUDE.md` é o roteador operacional e `PRODUCT_INDEX.md` é o catálogo navegável.
_Evitar_: duplicar no roteador o conteúdo metodológico dos módulos.
