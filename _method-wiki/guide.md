# Guia de Navegação - accounting-ops

Este guia aponta para a base metodológica viva do `accounting-ops`.

Use por fase do trabalho ou por situação.

---

## Entrada 1 - Por fase do trabalho

### Fase 1 - Fechamento e qualidade do número

O que acontece aqui: revisar consistência do número, separar efeito operacional de efeito contábil e preparar leitura gerencial.

**Workflows:**

- `tracks/accounting/workflows/monthly-closing-and-number-quality.md`
- `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md`
- `tracks/accounting/workflows/inventory-and-valuation-review.md`

**Base metodológica relevante:**

- `concepts/number-quality-foundations.md`
- `concepts/working-capital-foundations.md`
- `checklists/monthly-closing-number-quality-checklist.md`
- `processes/monthly-closing-and-number-quality.md`

**Artefato esperado:** leitura gerencial do número com fatos, hipóteses, impactos e próximos passos.

---

### Fase 2 - Planejamento, forecast e outlook

O que acontece aqui: revisar orçamento, atualizar expectativas e testar premissas críticas.

**Workflows:**

- `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`
- `tracks/fpa/workflows/integrated-budget-and-driver-review.md`

**Base metodológica relevante:**

- `concepts/budget-vs-forecast-vs-operating-plan.md`
- `checklists/forecast-review-checklist.md`
- `processes/forecasting-and-business-outlook.md`
- `processes/dashboard-and-kpi-design.md`

**Artefato esperado:** outlook com cenário base, upside, downside, premissas e ações de monitoramento.

---

### Fase 3 - Receita, margem e drivers de performance

O que acontece aqui: explicar crescimento, queda de margem, preço, mix, custo e competitividade.

**Workflows:**

- `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md`
- `tracks/fpa/workflows/gross-margin-bridge.md`

**Base metodológica relevante:**

- `concepts/inventory-and-valuation-foundations.md`
- `heuristics/margin-erosion-signals.md`
- `patterns/gross-margin-bridge.md`
- `patterns/variance-analysis.md`

**Artefato esperado:** bridge de margem e narrativa executiva com causa, impacto, recorrência e ação.

---

## Entrada 2 - Por situação

### Preciso revisar um forecast

1. Comece pelo workflow `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`.
2. Use `checklists/forecast-review-checklist.md` para testar premissas, cenários e riscos.
3. Consulte `concepts/budget-vs-forecast-vs-operating-plan.md` se houver confusão entre budget, operating plan e forecast.

### Preciso revisar um orçamento

1. Comece por `tracks/fpa/workflows/integrated-budget-and-driver-review.md`.
2. Use `concepts/budget-vs-forecast-vs-operating-plan.md` para separar referência aprovada, plano de execução e visão atualizada.
3. Se o orçamento depender de caixa, estoque ou giro, consulte `concepts/working-capital-foundations.md`.

### Preciso desenhar ou revisar KPIs e dashboards

1. Comece por `processes/dashboard-and-kpi-design.md`.
2. Defina o objetivo gerencial antes de escolher métricas.
3. Separe resultado final, drivers, leading indicators, lagging indicators e alertas.
4. Teste efeito colateral, qualidade do dado e frequência de atualização.

### Preciso explicar queda de margem

1. Comece por `tracks/fpa/workflows/gross-margin-bridge.md`.
2. Use `patterns/gross-margin-bridge.md` como estrutura de decomposição.
3. Use `heuristics/margin-erosion-signals.md` para desafiar explicações fracas.
4. Consulte `concepts/pricing-strength-vs-operating-efficiency.md` se a margem alta parecer esconder ineficiência.

### Preciso revisar caixa e giro

1. Comece por `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md`.
2. Consulte `concepts/working-capital-foundations.md`.
3. Feche com impacto em liquidez, capital de giro e decisão gerencial.

### Preciso revisar estoque e valuation

1. Comece por `tracks/accounting/workflows/inventory-and-valuation-review.md`.
2. Consulte `concepts/inventory-and-valuation-foundations.md`.
3. Conecte quantidade, valuation, obsolescência, custo e margem.
4. Se houver impacto em margem, use `patterns/gross-margin-bridge.md`.

### Preciso explicar uma variação

1. Use `patterns/variance-analysis.md` para estruturar baseline, materialidade, quebra, driver, evidência, impacto e ação.
2. Se a variação envolver fechamento, consulte `concepts/number-quality-foundations.md`.
3. Se a explicação parecer frágil, use `skills/challenge-variance-explanation.md`.
