# Financial Statement Analysis Index

Mapa de destilação editorial de *Financial Statement Analysis* para o `accounting-ops`.

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
| 1 | The adversarial nature of financial reporting | `_method-wiki/heuristics/` + `tracks/accounting/playbooks/result-reading-and-number-quality.md` | `destilar` | Muito forte para ceticismo aplicado ao número, qualidade do lucro e leitura menos ingênua das demonstrações. |
| 2 | The balance sheet | `_method-wiki/concepts/` + `tracks/accounting/playbooks/result-reading-and-number-quality.md` | `destilar` | Pode fortalecer leitura crítica de balanço, qualidade dos ativos e interpretação de estrutura financeira. |
| 3 | The income statement | `_method-wiki/concepts/` + `tracks/accounting/playbooks/result-reading-and-number-quality.md` | `destilar` | Bom candidato para leitura crítica de DRE, recorrência do resultado e qualidade de margem. |
| 4 | The statement of cash flows | `_method-wiki/concepts/working-capital-foundations.md` + `tracks/accounting/playbooks/result-reading-and-number-quality.md` | `destilar` | Forte para conexão entre lucro, caixa e estrutura financeira, com implicações importantes para controladoria. |
| 5 | What is profit? | `_method-wiki/concepts/number-quality-foundations.md` | `parcialmente coberto` | Tema muito aderente à base viva atual, mas com espaço claro para aprofundar earnings quality e economicidade do resultado. |
| 6 | Revenue recognition | `tracks/accounting/workflows/` + `tracks/accounting/playbooks/` | `destilar` | Forte candidato para receita, cut-off, timing e challenge de qualidade do número. |
| 7 | Expense recognition | `tracks/accounting/workflows/` + `tracks/accounting/playbooks/` | `destilar` | Muito útil para provisões, competência, timing de despesa e leitura crítica do resultado. |
| 8 | The applications and limitations of EBITDA | `tracks/accounting/playbooks/` + `skills/number-to-management-story.md` | `destilar` | Muito aderente a tradução executiva, limites do EBITDA e challenge de narrativas simplificadas. |
| 9 | The reliability of disclosure and audits | `_method-wiki/heuristics/` + `tracks/accounting/playbooks/` | `descartar por enquanto` | Pode ser útil para confiabilidade do disclosure, mas é menos central do que os capítulos que atacam diretamente o número. |
| 10 | Mergers-and-acquisitions accounting | `_method-wiki/concepts/` | `descartar por enquanto` | Importante, mas menos prioritário para o estágio atual do produto e para as lacunas mais recorrentes. |
| 11 | Is fraud detectable? | `_method-wiki/heuristics/` + `skills/challenge-variance-explanation.md` | `destilar` | Tema promissor para red flags, challenge de narrativa e leitura mais cética de inconsistências. |
| 12 | Forecasting financial statements | `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md` + `tracks/fpa/workflows/` | `parcialmente coberto` | Já existe base relevante de forecast, mas o capítulo pode aprofundar projeção integrada de demonstrações. |
| 13 | Credit analysis | `tracks/accounting/playbooks/` + `tracks/fpa/playbooks/` | `destilar` | Pode render leitura prática de covenants, solvência, liquidez e risco de crédito. |
| 14 | Equity analysis | `tracks/fpa/playbooks/` | `descartar por enquanto` | Menos aderente ao foco inicial do produto, mais voltado a análise de equity do que a controladoria/FP&A operacional. |

## Prioridade futura de destilação

### Prioridade alta

- Cap. 1 — The Adversarial Nature of Financial Reporting
- Cap. 6 — Revenue Recognition
- Cap. 7 — Expense Recognition
- Cap. 12 — Forecasting Financial Statements
- Cap. 8 — The Applications and Limitations of EBITDA

### Prioridade média

- Cap. 2 — The Balance Sheet
- Cap. 3 — The Income Statement
- Cap. 4 — The Statement of Cash Flows
- Cap. 11 — Is Fraud Detectable?
- Cap. 13 — Credit Analysis

### Prioridade baixa por enquanto

- Cap. 9 — The Reliability of Disclosure and Audits
- Cap. 10 — Mergers-and-Acquisitions Accounting
- Cap. 14 — Equity Analysis

## Leituras que este índice sugere ao produto

- fortalecer a camada de leitura crítica das demonstrações
- aprofundar qualidade do lucro, recorrência e economicidade do resultado
- abrir workflows ou playbooks de reconhecimento de receita e despesa
- melhorar a tradução executiva de EBITDA e outras métricas simplificadoras
- reforçar projeções financeiras integradas e leitura de crédito

## Regra para sessões futuras

Ao abrir um capítulo:

1. confirmar se a lacuna no agente continua real
2. apontar o MD relacionado ou o destino mais provável antes de escrever
3. ler apenas o capítulo priorizado
4. decidir entre promover, aprofundar cobertura parcial ou descartar por enquanto
5. atualizar o status editorial no índice para evitar releitura e retrabalho
