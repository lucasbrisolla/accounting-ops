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
- `tracks/accounting/workflows/account-reconciliation-review.md`
- `tracks/accounting/workflows/working-capital-and-cash-conversion-review.md`
- `tracks/accounting/workflows/inventory-and-valuation-review.md`

**Base metodológica relevante:**

- `concepts/number-quality-foundations.md`
- `concepts/working-capital-foundations.md`
- `checklists/working-capital-driver-checklist.md`
- `checklists/monthly-closing-number-quality-checklist.md`
- `processes/account-reconciliation-and-open-items.md`
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
- `checklists/financial-projection-quality-checklist.md`
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
- `checklists/revenue-and-gross-margin-driver-checklist.md`
- `heuristics/margin-erosion-signals.md`
- `patterns/gross-margin-bridge.md`
- `patterns/variance-analysis.md`

**Artefato esperado:** bridge de margem e narrativa executiva com causa, impacto, recorrência e ação.

---

### Fase 4 - Performance management e reporting gerencial

O que acontece aqui: criar contexto antes de medir, ligar estratégia a drivers e desenhar reporting que gere ação.

**Base metodológica relevante:**

- `processes/performance-management-framework.md`
- `concepts/value-driver-framework.md`
- `patterns/goal-to-driver-cascade.md`
- `processes/management-reporting-and-report-governance.md`
- `patterns/responsibility-reporting.md`
- `heuristics/when-not-to-report-a-variance.md`

**Playbooks relevantes:**

- `tracks/fpa/playbooks/creating-context-for-performance-measures.md`
- `tracks/fpa/playbooks/flash-report-design.md`
- `tracks/fpa/playbooks/margin-reporting-without-bad-allocations.md`

**Artefato esperado:** mapa coerente entre objetivo, driver, métrica, owner, report e ação.

---

### Fase 5 - Capital de longo prazo e disciplina de CAPEX

O que acontece aqui: revisar intensidade de capital, uso de ativos, CAPEX, caixa excedente e retorno do capital alocado.

**Base metodológica relevante:**

- `concepts/capital-intensity-foundations.md`
- `processes/long-term-capital-management.md`
- `checklists/capital-investment-postaudit-checklist.md`
- `concepts/excess-cash-and-capital-drag.md`
- `concepts/intangible-assets-and-goodwill-signals.md`

**Playbook relevante:**

- `tracks/fpa/playbooks/asset-utilization-and-capital-discipline.md`

**Artefato esperado:** leitura de capital de longo prazo com tese, risco, retorno e ação de disciplina.

---

## Entrada 2 - Por situação

### Preciso revisar um forecast

1. Comece pelo workflow `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`.
2. Use `checklists/forecast-review-checklist.md` para testar premissas, cenários e riscos.
3. Use `checklists/financial-projection-quality-checklist.md` se a revisão envolver tendência histórica, sensibilidade, caixa, capital de giro, covenants ou decisão relevante.
4. Consulte `concepts/budget-vs-forecast-vs-operating-plan.md` se houver confusão entre budget, operating plan e forecast.

### Preciso revisar uma projeção financeira

1. Comece por `processes/forecasting-and-business-outlook.md`.
2. Use `checklists/financial-projection-quality-checklist.md` para testar ownership, tendência, premissas, cenários, riscos, upsides e visão financeira completa.
3. Se a projeção for um forecast recorrente, aplique também `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`.

### Preciso revisar um orçamento

1. Comece por `tracks/fpa/workflows/integrated-budget-and-driver-review.md`.
2. Use `concepts/budget-vs-forecast-vs-operating-plan.md` para separar referência aprovada, plano de execução e visão atualizada.
3. Se o orçamento depender de caixa, estoque ou giro, consulte `concepts/working-capital-foundations.md`.

### Preciso desenhar ou revisar KPIs e dashboards

1. Comece por `processes/dashboard-and-kpi-design.md`.
2. Defina o objetivo gerencial antes de escolher métricas.
3. Separe resultado final, drivers, leading indicators, lagging indicators e alertas.
4. Teste efeito colateral, qualidade do dado e frequência de atualização.

### Preciso estruturar performance management antes de escolher KPIs

1. Comece por `processes/performance-management-framework.md`.
2. Use `tracks/fpa/playbooks/creating-context-for-performance-measures.md` para construir contexto antes da métrica.
3. Consulte `concepts/value-driver-framework.md` para organizar os drivers de valor.
4. Use `patterns/goal-to-driver-cascade.md` para ligar objetivo, driver, KPI, meta e owner.

### Preciso desenhar ou revisar reporting gerencial

1. Comece por `processes/management-reporting-and-report-governance.md`.
2. Use `patterns/responsibility-reporting.md` para ajustar granularidade e ownership.
3. Consulte `heuristics/when-not-to-report-a-variance.md` se o report estiver cheio de desvios pouco úteis.
4. Se a necessidade for curtíssimo prazo, use `tracks/fpa/playbooks/flash-report-design.md` e `templates/flash-report.md`.

### Preciso revisar um report de margem

1. Use `tracks/fpa/playbooks/margin-reporting-without-bad-allocations.md`.
2. Teste se os custos usados desaparecem de fato com o objeto analisado.
3. Se a pergunta for sobre variação de margem, complemente com `patterns/gross-margin-bridge.md`.

### Preciso explicar queda de margem

1. Comece por `tracks/fpa/workflows/gross-margin-bridge.md`.
2. Use `patterns/gross-margin-bridge.md` como estrutura de decomposição.
3. Use `heuristics/margin-erosion-signals.md` para desafiar explicações fracas.
4. Consulte `concepts/pricing-strength-vs-operating-efficiency.md` se a margem alta parecer esconder ineficiência.

### Preciso revisar receita, forecast comercial ou pricing

1. Comece por `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md`.
2. Use `checklists/revenue-and-gross-margin-driver-checklist.md` para testar mercado, share, preço, mix, descontos, pipeline, pedidos perdidos e margem.
3. Consulte `concepts/pricing-strength-vs-operating-efficiency.md` se a margem depender de prêmio de preço.
4. Use `processes/dashboard-and-kpi-design.md` se a saída esperada for dashboard de receita ou pricing strength.

### Preciso revisar caixa e giro

1. Comece por `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md`.
2. Consulte `concepts/working-capital-foundations.md`.
3. Use `tracks/accounting/workflows/working-capital-and-cash-conversion-review.md` se a pergunta envolver DSO, estoque, payables, capital preso ou conversão de caixa.
4. Feche com impacto em liquidez, capital de giro e decisão gerencial.

### Preciso revisar uma conciliação contábil

1. Comece por `processes/account-reconciliation-and-open-items.md`.
2. Use `tracks/accounting/workflows/account-reconciliation-review.md` para revisar saldo, fonte, diferença e open items.
3. Se houver ajuste necessário, use `skills/prepare-journal-entry-support.md` para preparar suporte do lançamento.
4. Feche com status da conta: reconciliada, reconciliada com pendências monitoradas ou não reconciliada.

### Preciso revisar capital de longo prazo, CAPEX ou uso de ativos

1. Comece por `processes/long-term-capital-management.md`.
2. Consulte `concepts/capital-intensity-foundations.md`.
3. Use `tracks/fpa/playbooks/asset-utilization-and-capital-discipline.md` se a discussão envolver ativo subutilizado, venda, consolidação ou terceirização.
4. Aplique `checklists/capital-investment-postaudit-checklist.md` se o projeto já foi implementado.

### Preciso ler business model além da DRE

1. Comece por `concepts/business-model-foundations.md`.
2. Use `concepts/analytical-tools-foundations.md` para escolher a ferramenta analítica certa.
3. Use `patterns/performance-tree.md` se precisar decompor o KPI principal em drivers acionáveis.

### Preciso revisar capital de giro operacional

1. Comece por `tracks/accounting/workflows/working-capital-and-cash-conversion-review.md`.
2. Use `checklists/working-capital-driver-checklist.md` para testar DSO, BPDSO, past due, estoque, E&O, purchase commitments e payables.
3. Consulte `concepts/working-capital-foundations.md` para separar saldo contábil, processo operacional e efeito em caixa.

### Preciso revisar estoque e valuation

1. Comece por `tracks/accounting/workflows/inventory-and-valuation-review.md`.
2. Consulte `concepts/inventory-and-valuation-foundations.md`.
3. Conecte quantidade, valuation, obsolescência, custo e margem.
4. Se houver impacto em margem, use `patterns/gross-margin-bridge.md`.

### Preciso explicar uma variação

1. Use `patterns/variance-analysis.md` para estruturar baseline, materialidade, quebra, driver, evidência, impacto e ação.
2. Se a variação envolver fechamento, consulte `concepts/number-quality-foundations.md`.
3. Se a explicação parecer frágil, use `skills/challenge-variance-explanation.md`.
