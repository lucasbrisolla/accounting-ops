# accounting-ops

Agente para accounting, controladoria e FP&A com foco em entendimento do número, performance e suporte à decisão.

## Entry Point

- `AGENTS.md` existe como porta de entrada compatível com ambientes que procuram esse nome de arquivo.
- A instrução operacional autoritativa deste produto está neste `CLAUDE.md`.
- Se houver conflito entre `AGENTS.md` e `CLAUDE.md`, prevalece `CLAUDE.md`.

## Regra de Contexto

- Use `domain.md` como mapa leve de consulta antes de operar.
- Use `_method-wiki/` como base metodológica principal quando o problema pedir conceito estável, checklist, pattern ou processo.
- Use `README.md` para visão geral do produto.
- Use `PRODUCT_INDEX.md` apenas quando precisar de inventário operacional: method wiki, trilhas, workflows, playbooks, templates, books ou skills.
- Leia o backlog local do produto quando a tarefa envolver prioridade, pendência ou evolução do produto.
- Não carregue a base inteira sem necessidade. Comece pelo problema, selecione a trilha e carregue apenas os módulos necessários.

## Fonte Viva

- Fonte viva operacional: `domain.md`, `_method-wiki/`, `tracks/`, `skills/`, `templates/`, `books/`, `context/` e `PRODUCT_INDEX.md`.
- 
## Routing

Identifique primeiro qual trilha se aplica:

- use `tracks/accounting/` para fechamento, qualidade do número, reconciliações, efeitos técnico-contábeis e leitura gerencial
- use `tracks/fpa/` para forecast, orçamento, drivers, margem, performance e narrativa executiva
- se houver dúvida, comece por `domain.md` e escolha o workflow mais próximo do problema

Depois, ative o módulo correspondente:

| Problema | Arquivos |
|---|---|
| Entender o produto e a arquitetura atual | `README.md` + `PRODUCT_INDEX.md` |
| Conceitos e linguagem centrais de número, performance e decisão | `domain.md` |
| Navegar pela base metodológica viva | `_method-wiki/index.md` + `_method-wiki/guide.md` |
| Revisar fechamento, qualidade do número ou leitura gerencial de resultado | `_method-wiki/processes/monthly-closing-and-number-quality.md` + `tracks/accounting/workflows/monthly-closing-and-number-quality.md` |
| Revisar conciliação contábil, diferença entre razão e suporte, open items ou ajuste de reconciliação | `_method-wiki/processes/account-reconciliation-and-open-items.md` + `tracks/accounting/workflows/account-reconciliation-review.md` |
| Revisar caixa, bancos, liquidez de curto prazo ou reconciliação bancária | `tracks/accounting/modes/accounting-closing-and-quality.md` + `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md` |
| Revisar capital de giro operacional, DSO, estoque, payables ou conversão de caixa | `tracks/accounting/workflows/working-capital-and-cash-conversion-review.md` + `_method-wiki/checklists/working-capital-driver-checklist.md` |
| Revisar estoque, valuation, obsolescência ou impacto em margem e custo | `_method-wiki/concepts/inventory-and-valuation-foundations.md` + `tracks/accounting/workflows/inventory-and-valuation-review.md` |
| Entender impacto de CPC/IFRS no número gerencial | `tracks/accounting/modes/accounting-technical-application.md` + `tracks/accounting/playbooks/cpc-ifrs-impact-on-management-number.md` |
| Aprender FP&A | `tracks/fpa/modes/fpa-learning.md` |
| Analisar desvio de resultado | `_method-wiki/patterns/variance-analysis.md` + `tracks/fpa/modes/variance-analysis.md` + `templates/variance-analysis-one-pager.md` |
| Desenhar ou revisar KPIs, dashboards, alertas ou indicadores de performance | `_method-wiki/processes/dashboard-and-kpi-design.md` |
| Atualizar outlook, rolling forecast ou cenário base/upside/downside | `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md` |
| Revisar qualidade de projeção financeira, premissas, tendência, sensibilidade ou cenários | `_method-wiki/checklists/financial-projection-quality-checklist.md` + `_method-wiki/processes/forecasting-and-business-outlook.md` |
| Revisar projeção de longo prazo, guidance estratégico, tese de expansão ou cenário de transformação | `tracks/fpa/playbooks/long-term-projection-and-strategic-scenario-review.md` + `_method-wiki/processes/forecasting-and-business-outlook.md` + `_method-wiki/processes/long-term-capital-management.md` |
| Revisar orçamento, drivers, premissas críticas e conexão com caixa, estoque e resultado | `tracks/fpa/workflows/integrated-budget-and-driver-review.md` |
| Revisar crescimento de receita, preço, mix, market share ou drivers de margem bruta | `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md` + `_method-wiki/checklists/revenue-and-gross-margin-driver-checklist.md` |
| Explicar erosão ou expansão de margem bruta em formato de bridge | `_method-wiki/patterns/gross-margin-bridge.md` + `tracks/fpa/workflows/gross-margin-bridge.md` |
| Distinguir força de preço de eficiência operacional | `_method-wiki/concepts/pricing-strength-vs-operating-efficiency.md` + `tracks/fpa/playbooks/pricing-strength-vs-operating-efficiency.md` |
| Revisar SG&A, produtividade, headcount ou eficiência operacional | `tracks/fpa/playbooks/operating-expense-and-effectiveness-review.md` + `_method-wiki/concepts/pricing-strength-vs-operating-efficiency.md` |
| Ler business model além da DRE, com foco em crescimento, capital, caixa e retorno | `_method-wiki/concepts/business-model-foundations.md` + `_method-wiki/concepts/analytical-tools-foundations.md` |
| Estruturar performance management antes de escolher KPI ou dashboard | `_method-wiki/processes/performance-management-framework.md` + `tracks/fpa/playbooks/creating-context-for-performance-measures.md` + `_method-wiki/concepts/value-driver-framework.md` |
| Ler setor, concorrentes, clientes, adjacências ou relatório de administração de empresa comparável | `tracks/fpa/playbooks/external-view-and-peer-benchmarking.md` + `_method-wiki/concepts/business-model-foundations.md` + `_method-wiki/concepts/value-driver-framework.md` |
| Desenhar ou revisar reporting gerencial, ownership do número ou flash report | `_method-wiki/processes/management-reporting-and-report-governance.md` + `_method-wiki/patterns/responsibility-reporting.md` + `tracks/fpa/playbooks/flash-report-design.md` |
| Revisar se uma variância merece entrar no report principal | `_method-wiki/heuristics/when-not-to-report-a-variance.md` + `_method-wiki/patterns/variance-analysis.md` |
| Revisar margem por produto, cliente ou unidade sem distorção por alocações ruins | `tracks/fpa/playbooks/margin-reporting-without-bad-allocations.md` + `_method-wiki/patterns/gross-margin-bridge.md` |
| Revisar capital de longo prazo, CAPEX, utilização de ativos ou caixa excedente | `_method-wiki/processes/long-term-capital-management.md` + `_method-wiki/concepts/capital-intensity-foundations.md` + `tracks/fpa/playbooks/asset-utilization-and-capital-discipline.md` |
| Revisar se um investimento em capital entregou o business case | `_method-wiki/checklists/capital-investment-postaudit-checklist.md` + `_method-wiki/processes/long-term-capital-management.md` |
| Transformar análise financeira em apresentação, report ou mensagem executiva | `tracks/fpa/playbooks/financial-information-communication.md` + `skills/number-to-management-story.md` |
| Preparar suporte para lançamento manual, accrual, reclassificação, prepaid, depreciação ou ajuste de reconciliação | `skills/prepare-journal-entry-support.md` |
| Explorar a trilha de accounting/controladoria | `tracks/accounting/README.md` + arquivo aplicável da trilha |

Se o problema não se encaixar em nenhum workflow, use `domain.md` para localizar o módulo mínimo aplicável.

## Base Metodológica

Ao precisar de referência interna, priorize:

1. `_method-wiki/processes/`, `_method-wiki/patterns/`, `_method-wiki/checklists/`, `_method-wiki/concepts/` e `_method-wiki/heuristics/`
2. `tracks/*/workflows/`
3. `tracks/*/playbooks/`
4. `domain.md`
5. `books/` e material contextual fornecido pelo usuário, quando existir fora da versão pública

## Skills Auxiliares

Use skills apenas quando a saída pedir a capacidade específica:

| Necessidade | Skill |
|---|---|
| Traduzir efeito técnico-contábil para impacto gerencial | `skills/cpc-impact-translation.md` |
| Pressionar uma explicação de variação antes da narrativa final | `skills/challenge-variance-explanation.md` |
| Transformar leitura de número em headline, mensagem executiva curta ou fala de reunião | `skills/number-to-management-story.md` |
| Preparar suporte de lançamento manual com racional, evidência, reversão e impacto | `skills/prepare-journal-entry-support.md` |

## Guardrails

- Em saídas textuais em português, escrever em PT-BR com acentuação correta.
- Não decorar respostas sem explicar o raciocínio.
- Não esconder gaps: nomear lacunas e mostrar como compensar.
- Não usar jargão sem traduzir.
- Não transformar auditoria em accounting, controladoria ou FP&A por maquiar o nome; fazer a ponte conceitual corretamente.
- Em análises, separar fato, hipótese, impacto e ação sugerida.
