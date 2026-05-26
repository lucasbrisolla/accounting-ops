# accounting-ops

Agente para accounting, controladoria, FP&A e análise de performance, com arquitetura modular para manter trilhas técnicas separáveis no futuro.

## Papel

O `accounting-ops` ajuda a desenvolver raciocínio sobre qualidade do número, fechamento, performance, orçamento, forecast e suporte à decisão.

Ele existe para transformar conhecimento contábil e raciocínio financeiro em pensamento de negócio:

- fechamento e leitura de resultado
- explicação gerencial de número
- análise de orçado vs. realizado
- explicação de variações
- margem e drivers de performance
- forecast, budget e cenários
- report executivo

## Estado Atual

Fase 1: transição estrutural para produto unificado.

Objetivo imediato: preservar a base já construída em FP&A e abrir a trilha `accounting/controladoria` sem perder modularidade.

## Entrada Principal

Use `CLAUDE.md` como porta de entrada operacional.

Use `INDEX.md` quando quiser uma visão rápida da arquitetura do produto.

## Fontes de Verdade

1. `CLAUDE.md`: roteamento, guardrails e trilhas ativas.
2. `domain.md`: mapa central de conceitos e vocabulário de negócio, controladoria e FP&A.
3. `_method-wiki/`: base metodológica viva.
4. `PRODUCT_INDEX.md`: inventário operacional da estrutura atual.
5. `tracks/`: trilhas específicas por domínio.
6. `templates/`: formatos reutilizáveis de análise e treino.
7. `skills/`: transformações atômicas sob demanda.
8. `Agent Products/_backlog/backlog-accounting-ops.md`: evolução planejada do produto.

## Method Wiki

- `_method-wiki/README.md`: papel e regra editorial da base metodológica.
- `_method-wiki/index.md`: inventário navegável de concepts, heuristics, checklists, patterns e processes.
- `_method-wiki/guide.md`: navegação por fase do trabalho e por situação.
- `_method-wiki/processes/dashboard-and-kpi-design.md`: desenho de dashboards, KPIs, alertas e indicadores de performance.

## Trilhas Ativas

### `tracks/fpa/`

- `tracks/fpa/modes/variance-analysis.md`: analisar variações entre orçado, realizado e forecast.
- `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`: atualizar outlook, drivers, premissas e cenários de forecast.
- `tracks/fpa/workflows/integrated-budget-and-driver-review.md`: revisar orçamento com foco em drivers, premissas e conexão entre resultado, caixa e operação.
- `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md`: revisar receita, preço, mix, market share e drivers de margem bruta.
- `tracks/fpa/workflows/gross-margin-bridge.md`: explicar expansão ou erosão de margem bruta em formato de bridge gerencial.
- `tracks/fpa/playbooks/financial-information-communication.md`: transformar análise financeira em mensagem executiva, apresentação ou report de gestão.
- `tracks/fpa/playbooks/pricing-strength-vs-operating-efficiency.md`: diferenciar margem forte por pricing de margem forte por eficiência real.

### `tracks/accounting/`

- `tracks/accounting/modes/accounting-closing-and-quality.md`: fechamento, qualidade do número e leitura gerencial.
- `tracks/accounting/modes/accounting-technical-application.md`: contabilidade técnica aplicada ao número gerencial.
- `tracks/accounting/workflows/monthly-closing-and-number-quality.md`: workflow de fechamento mensal com foco em consistência, leitura e mensagem executiva.
- `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md`: workflow de caixa, bancos, reconciliação e leitura de liquidez de curto prazo.
- `tracks/accounting/workflows/inventory-and-valuation-review.md`: workflow de estoque, valuation, obsolescência e impacto em custo, margem e resultado.
- `tracks/accounting/playbooks/result-reading-and-number-quality.md`: leitura de resultado com foco em confiabilidade e mensagem executiva.
- `tracks/accounting/playbooks/cpc-ifrs-impact-on-management-number.md`: efeito de CPC/IFRS sobre margem, resultado, estoque e narrativa.

## Templates Ativos

- `templates/variance-analysis-one-pager.md`: estrutura curta para explicar desvios.
## Skills Ativas

- `skills/cpc-impact-translation.md`: traduz efeito técnico-contábil para impacto gerencial.
- `skills/challenge-variance-explanation.md`: pressiona uma explicação de variação antes que ela vire narrativa final.
- `skills/number-to-management-story.md`: transforma leitura de número em headline, mensagem executiva curta ou fala de reunião.

## Guardrails

- Separar experiência direta, exposição por auditoria e inferência.
- Não vender como experiência hands-on aquilo que foi revisão crítica.
- Traduzir auditoria para linguagem de negócio: margem, resultado, driver, impacto e decisão.
- Sempre explicar variação com causa, efeito financeiro e próximo passo.
- Quando faltar dado, declarar a lacuna antes de concluir.
