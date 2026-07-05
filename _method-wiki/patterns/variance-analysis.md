# Pattern: Variance Analysis

## Papel

Estrutura recorrente para explicar variações entre actual, budget, forecast ou períodos comparativos.

## Estrutura base

1. Baseline.
2. Materialidade.
3. Quebra.
4. Driver.
5. Evidência.
6. Impacto.
7. Ação.

## Perguntas por etapa

| Etapa | Pergunta |
|---|---|
| Baseline | A comparação é contra budget, forecast, mês anterior ou ano anterior? |
| Materialidade | A variação é relevante em valor, percentual ou risco decisório? |
| Quebra | A variação está em qual linha, unidade, produto, cliente, projeto ou centro de custo? |
| Driver | A causa é volume, preço, mix, custo, eficiência, timing, estoque ou reclassificação? |
| Evidência | Qual dado suporta a explicação? |
| Impacto | O efeito atinge margem, EBITDA, caixa, forecast ou decisão? |
| Ação | O que monitorar, corrigir, comunicar ou validar com a área? |

## Gatilhos de materialidade

Investigue uma variação quando ela for relevante por:

- valor absoluto
- percentual sobre a base
- direção inesperada
- impacto em margem, EBITDA, caixa ou covenant
- recorrência acumulada
- mudança nova em uma conta antes estável

## Decomposições úteis

Antes de aceitar a narrativa, quebre a variação quando possível:

| Tipo de variação | Quebra recomendada |
|---|---|
| Receita | preço, volume, mix, câmbio, devoluções, timing |
| Custo industrial | volume, consumo, eficiência, preço de insumo, mix, absorção |
| Margem | preço/volume/mix, custo unitário, capacidade, sucata, frete |
| Pessoal | headcount, salário médio, horas extras, encargos, bônus |
| Opex | categoria de gasto, fornecedor, timing, reclassificação, não recorrente |
| Câmbio | taxa, exposição, hedge, data de reconhecimento |

### Decomposição industrial por custo padrão

Quando existir standard costing, separar:

| Componente | Rate ou preço | Uso, eficiência ou volume |
|---|---|---|
| Material | preço de compra | consumo, yield, scrap e qualidade |
| Mão de obra | taxa e mix de função | horas, setup, treinamento e downtime |
| Overhead variável | spending rate | eficiência da base de atividade |
| Overhead fixo | gasto contra orçamento | volume, capacidade e absorção |

Antes de explicar a variância, testar se o padrão é atual, atingível e coerente com volume, equipamento, processo e condições de compra.

Uma variância favorável não prova boa performance. Compra em excesso, produção sem demanda ou postergação de manutenção podem melhorar o indicador e piorar a economia total.

Se a explicação for "timing", ela deve indicar quando o efeito reverte. Se for "one-time", deve explicar por que não se repete.

## Regra de qualidade

Uma boa explicação de variação não termina em "a conta aumentou".

Ela precisa dizer:

- por que aumentou
- se era esperado
- se continua nos próximos meses
- qual decisão ou alerta decorre disso

## Conexões operacionais

- Modo: `tracks/fpa/modes/variance-analysis.md`
- Workflow: `tracks/accounting/workflows/standard-cost-and-industrial-variance-review.md`
- Template: `templates/variance-analysis-one-pager.md`
- Skill: `skills/challenge-variance-explanation.md`

## Fonte adicional

- Steven Bragg, *Cost Accounting Fundamentals*, Cap. 7 — Standard Costing.
