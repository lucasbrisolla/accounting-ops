# Budgeting Index

Mapa de destilação editorial de *Budgeting* para o `accounting-ops`.

Critério desta nota:

- leitura atual limitada ao sumário
- sem destilação de capítulos ainda
- classificação editorial preliminar por capítulo
- foco em apontar destino provável, status e aderência ao produto

## Legenda de status

- `já coberto`: o capítulo parece bem representado por artefatos já existentes
- `parcialmente coberto`: já existe cobertura parcial, mas ainda pode haver ganho de destilação
- `destilar`: lacuna real ou provável; candidato de trabalho futuro
- `descartar por enquanto`: baixa aderência ao foco atual do produto

## Mapa por capítulo

| Capítulo | Tema principal | MD relacionado ou destino mais provável | Status | Observação |
|---|---|---|---|---|
| 1 | Introduction to Budgeting | `_method-wiki/concepts/budget-vs-forecast-vs-operating-plan.md` + `tracks/fpa/modes/fpa-learning.md` | `parcialmente coberto` | Bom framing do sistema orçamentário e dos trade-offs do processo, mas ainda pode refinar a base conceitual. |
| 2 | Cost-Volume-Profit Analysis | `_method-wiki/concepts/` + `tracks/fpa/playbooks/` | `destilar` | Forte candidato para CVP, contribuição, breakeven e sensibilidade de margem. |
| 3 | The System of Budgets | `tracks/fpa/workflows/integrated-budget-and-driver-review.md` + `_method-wiki/processes/` | `parcialmente coberto` | Capítulo-base para o sistema orçamentário; já há base viva, mas ainda com espaço para estruturar melhor o processo. |
| 4 | The Revenue Budget | `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md` + `tracks/fpa/workflows/integrated-budget-and-driver-review.md` | `parcialmente coberto` | Forte aderência à trilha `fpa`, com potencial para aprofundar a construção do orçamento de receita. |
| 5 | Ending Finished Goods Inventory Budget | `tracks/accounting/workflows/inventory-and-valuation-review.md` + `tracks/fpa/workflows/integrated-budget-and-driver-review.md` | `destilar` | Bom elo entre orçamento, estoque, produção e capital de giro. |
| 6 | The Production Budget | `tracks/fpa/workflows/` + `_method-wiki/processes/` | `destilar` | Muito aderente a ambiente industrial e à ligação entre demanda, capacidade e produção. |
| 7 | The Direct Materials Budget | `tracks/fpa/workflows/` + `_method-wiki/processes/` | `destilar` | Forte para materiais, consumo, compras e pressão em custo. |
| 8 | The Direct Labor Budget | `tracks/fpa/workflows/` + `_method-wiki/processes/` | `destilar` | Pode ajudar a ligar capacidade, volume, produtividade e custo de mão de obra. |
| 9 | The Manufacturing Overhead Budget | `tracks/fpa/workflows/` + `tracks/fpa/playbooks/` | `destilar` | Importante para overhead industrial, alocação e leitura de eficiência fabril. |
| 10 | The Cost of Goods Sold Budget | `tracks/fpa/workflows/` + `tracks/accounting/playbooks/` | `destilar` | Útil para conectar orçamento com custo, margem e resultado. |
| 11 | The Sales and Marketing Budget | `tracks/fpa/workflows/` + `tracks/fpa/playbooks/` | `destilar` | Bom para despesas comerciais, crescimento e retorno sobre investimento comercial. |
| 12 | The Research and Development Budget | `tracks/fpa/playbooks/` | `descartar por enquanto` | Tema válido, mas menos central para as lacunas mais recorrentes do produto agora. |
| 13 | The Administration Budget | `tracks/fpa/workflows/` + `tracks/fpa/playbooks/` | `destilar` | Pode fortalecer leitura de SG&A, despesas fixas e alavancas de eficiência administrativa. |
| 14 | The Capital Budget | `tracks/fpa/workflows/` + `tracks/fpa/playbooks/` | `destilar` | Muito promissor para CAPEX, business case e decisões de investimento. |
| 15 | The Compensation Budget | `tracks/fpa/workflows/` + `tracks/accounting/workflows/` | `destilar` | Útil para orçamento de pessoas, folha, encargos e provisões associadas. |
| 16 | The Master Budget | `tracks/fpa/workflows/integrated-budget-and-driver-review.md` | `parcialmente coberto` | Capítulo central; já existe workflow aderente, mas ainda há espaço para consolidar melhor a visão integrada. |
| 17 | Nonprofit Budgeting | `tracks/fpa/playbooks/` | `descartar por enquanto` | Pouco aderente ao foco atual do produto. |
| 18 | Flexible Budgeting | `_method-wiki/patterns/` + `tracks/fpa/modes/variance-analysis.md` + `tracks/fpa/workflows/` | `destilar` | Muito forte para análise de variações, orçamento adaptativo e leitura gerencial mais robusta. |

## Prioridade futura de destilação

### Prioridade alta

- Cap. 16 — The Master Budget
- Cap. 3 — The System of Budgets
- Cap. 18 — Flexible Budgeting
- Cap. 4 — The Revenue Budget
- Cap. 14 — The Capital Budget

### Prioridade média

- Cap. 10 — The Cost of Goods Sold Budget
- Cap. 6 — The Production Budget
- Cap. 7 — The Direct Materials Budget
- Cap. 9 — The Manufacturing Overhead Budget
- Cap. 13 — The Administration Budget

### Prioridade baixa por enquanto

- Cap. 12 — The Research and Development Budget
- Cap. 15 — The Compensation Budget
- Cap. 17 — Nonprofit Budgeting

## Leituras que este índice sugere ao produto

- aprofundar o sistema orçamentário e a visão de master budget
- abrir ou reforçar workflows de orçamento industrial
- fortalecer CVP, contribuição e alavancas de margem
- melhorar a camada de CAPEX e decisões de investimento
- consolidar flexible budgeting como ponte entre orçamento e variance analysis

## Regra para sessões futuras

Ao abrir um capítulo:

1. confirmar se a lacuna no agente continua real
2. apontar o MD relacionado ou o destino mais provável antes de escrever
3. ler apenas o capítulo priorizado
4. decidir entre promover, aprofundar cobertura parcial ou descartar por enquanto
5. atualizar o status editorial no índice para evitar releitura e retrabalho
