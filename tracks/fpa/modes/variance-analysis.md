# Modo: Análise de Variações

## Nota Editorial

Escrever sempre em PT-BR, com acentuação correta e linguagem natural.

Use para analisar desvios entre actual, budget, forecast ou períodos comparativos.

## Framework

1. `Baseline`: comparação usada, como actual vs. budget.
2. `Materialidade`: valor, percentual e relevância para resultado.
3. `Quebra`: linha da DRE, unidade, produto, cliente, projeto ou centro de custo.
4. `Driver`: causa provável da variação.
5. `Evidência`: dado que suporta a explicação.
6. `Impacto`: efeito em margem, EBITDA, caixa ou forecast.
7. `Ação`: recomendação, follow-up ou pergunta para a área.

## Drivers Frequentes

- volume
- preço
- mix
- custo unitário
- frete
- eficiência operacional
- preço de material e purchase price variance
- uso, yield, scrap e qualidade
- labor rate e labor efficiency
- overhead spending, eficiência e absorção
- estoque
- timing contábil
- one-off
- premissa de forecast
- reclassificação

## Saída Recomendada

Use `templates/variance-analysis-one-pager.md`.

## Regra de Qualidade

Uma boa explicação de variação não termina em "a conta aumentou".

Ela precisa dizer:

- por que aumentou
- se era esperado
- se continua nos próximos meses
- qual decisão ou alerta decorre disso

Quando houver custo padrão, validar primeiro se o standard é atual e atingível. Uma variância favorável pode esconder compra excessiva, produção sem demanda ou outro comportamento que piora o resultado econômico.

Para revisão industrial completa, usar `tracks/accounting/workflows/standard-cost-and-industrial-variance-review.md`.
