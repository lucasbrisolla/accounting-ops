# FP&A Performance Management Index

Mapa de destilação editorial de *Financial Planning, Analysis, and Performance Management* para o `accounting-ops`.

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

| Capítulo | Tema principal                                       | MD relacionado ou destino mais provável                                                                                                                                                        | Status                   | Observação                                                                                             |
| -------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------ |
| 1        | FP&A and business performance management             | `tracks/fpa/modes/fpa-learning.md`                                                                                                                                                             | `parcialmente coberto`   | Bom framing da trilha `fpa`, mas ainda pode reforçar a visão sistêmica de performance management.      |
| 2        | Fundamentals of finance                              | `domain.md` + `_method-wiki/concepts/`                                                                                                                                                         | `parcialmente coberto`   | Base conceitual relevante, mas o destino ainda depende de onde a lacuna aparecer com mais clareza.     |
| 3        | Analytical tools and concepts                        | `_method-wiki/concepts/` + `tracks/fpa/playbooks/`                                                                                                                                             | `destilar`               | Tem potencial para fortalecer ferramental analítico e leitura de modelo de negócio.                    |
| 4        | Predictive and analytical models                     | `tracks/fpa/workflows/`                                                                                                                                                                        | `destilar`               | Forte candidato para modelagem, projeções e raciocínio prospectivo.                                    |
| 5        | Building analytical capability                       | `tracks/fpa/playbooks/`                                                                                                                                                                        | `descartar por enquanto` | Tema mais organizacional; útil, mas não resolve a lacuna mais urgente do produto agora.                |
| 6        | Communicating and presenting financial information   | `tracks/fpa/playbooks/financial-information-communication.md` + `skills/number-to-management-story.md`                                                                                         | `já coberto`             | Destilado para playbook de comunicação financeira e reforço do skill de mensagem executiva.            |
| 7        | Business performance management                      | `tracks/fpa/modes/fpa-learning.md` + `tracks/fpa/playbooks/`                                                                                                                                   | `destilar`               | Pode estruturar melhor a camada de performance management, hoje ainda implícita em vários artefatos.   |
| 8        | Dashboards and KPIs                                  | `_method-wiki/processes/dashboard-and-kpi-design.md`                                                                                                                                           | `já coberto`             | Destilado para processo metodológico de dashboards, KPIs, alertas e indicadores de performance.        |
| 9        | Institutionalizing performance management            | `tracks/fpa/playbooks/`                                                                                                                                                                        | `descartar por enquanto` | Importante para maturidade de gestão, mas menos atômico e menos urgente na fase atual.                 |
| 10       | Measuring and driving what’s important               | `tracks/fpa/playbooks/`                                                                                                                                                                        | `descartar por enquanto` | Bloco potencialmente útil, mas com aderência menos direta às lacunas operacionais atuais.              |
| 11       | The external view                                    | `tracks/fpa/playbooks/`                                                                                                                                                                        | `descartar por enquanto` | Benchmarking e análise externa podem ter valor depois, mas não são centrais para o estágio atual.      |
| 12       | Business projections and plans                       | `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`                                                                                                                                | `parcialmente coberto`   | Já existe workflow aderente, mas o capítulo pode aprofundar melhores práticas de projeções e planning. |
| 13       | Budgets, operating plans, and forecasts              | `_method-wiki/concepts/budget-vs-forecast-vs-operating-plan.md` + `_method-wiki/processes/forecasting-and-business-outlook.md` + `tracks/fpa/workflows/integrated-budget-and-driver-review.md` | `já coberto`             | Destilado para conceito, processo de forecast/business outlook e workflow de orçamento integrado.      |
| 14       | Long-term projections                                | `tracks/fpa/workflows/` + `tracks/fpa/playbooks/`                                                                                                                                              | `destilar`               | Bom candidato para projeções de longo prazo, cenários e apresentação executiva.                        |
| 15       | Revenue and gross margins                            | `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md` + `tracks/fpa/workflows/gross-margin-bridge.md`                                                                               | `parcialmente coberto`   | Tema já bem conectado ao produto, mas pode render refinamento de drivers e leitura gerencial.          |
| 16       | Operating expenses and effectiveness                 | `tracks/fpa/playbooks/` + `_method-wiki/concepts/`                                                                                                                                             | `destilar`               | Há espaço para melhorar a leitura de despesas, eficiência e alavancas operacionais.                    |
| 17       | Capital management and cash flow                     | `_method-wiki/concepts/working-capital-foundations.md` + `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md`                                                              | `parcialmente coberto`   | Forte aderência a capital de giro e caixa; a base existe, mas ainda pode ser aprofundada.              |
| 18       | Capital management and cash flow (capital intensity) | `tracks/fpa/workflows/` + `tracks/fpa/playbooks/`                                                                                                                                              | `destilar`               | Muito promissor para CAPEX, intensidade de capital e leitura de ativos de longo prazo.                 |
| 19       | Risk, uncertainty, and the cost of capital           | `_method-wiki/concepts/` + `tracks/fpa/playbooks/`                                                                                                                                             | `descartar por enquanto` | Importante, mas mais avançado e menos crítico para o estágio atual do produto.                         |

## Prioridade futura de destilação

### Prioridade alta

- Cap. 13 — Budgets, Operating Plans, and Forecasts
- Cap. 8 — Dashboards and KPIs
- Cap. 12 — Business Projections and Plans
- Cap. 15 — Revenue and Gross Margins
- Cap. 17 — Capital Management and Cash Flow

### Prioridade média

- Cap. 6 — Communicating and Presenting Financial Information
- Cap. 18 — Capital Management and Cash Flow / Capital Intensity
- Cap. 7 — Business Performance Management
- Cap. 16 — Operating Expenses and Effectiveness
- Cap. 14 — Long-Term Projections

### Prioridade baixa por enquanto

- Cap. 5 — Building Analytical Capability
- Cap. 9 — Institutionalizing Performance Management
- Cap. 10 — Measuring and Driving What’s Important
- Cap. 11 — The External View
- Cap. 19 — Risk, Uncertainty, and the Cost of Capital

## Leituras que este índice sugere ao produto

- aprofundar orçamento, operating plan e forecast sobre a base já criada
- abrir um workflow ou processo mais explícito para dashboards e KPIs
- reforçar projeções financeiras de médio e longo prazo
- melhorar a camada de comunicação financeira e narrativa executiva
- aprofundar capital de giro, caixa e capital intensity

## Regra para sessões futuras

Ao abrir um capítulo:

1. confirmar se a lacuna no agente continua real
2. apontar o MD relacionado ou o destino mais provável antes de escrever
3. ler apenas o capítulo priorizado
4. decidir entre promover, aprofundar cobertura parcial ou descartar por enquanto
5. atualizar o status editorial no índice para evitar releitura e retrabalho
