# Modo: Análise de Variações

## Papel do modo

Este modo aplica a lente de FP&A a uma pergunta de `Variance`: budget vs.
actual, forecast vs. actual, bridge de resultado e persistência do efeito.

O contrato analítico está em
`skills/explain-variance/SKILL.md`. Este modo não é o contrato canônico e não
substitui o módulo canônico nem redefine baseline, materialidade, driver, evidência, impacto, recorrência,
confiança, reconciliação ou ação.

## Sequência de roteamento

1. Carregue `skills/explain-variance/SKILL.md` para construir a decisão
   canônica.
2. Use a lente de FP&A deste modo para qualificar expectativa, persistência,
   outlook e relevância para performance.
3. Se necessário, carregue um adapter de challenge ou de formato depois que a
   decisão existir.

## Lente específica de FP&A

Perguntas adicionais, sem substituir o contrato canônico:

- O desvio contra Budget muda a leitura de execução ou apenas o ponto de
  partida do plano?
- O desvio contra Forecast exige revisar premissa, run rate ou outlook?
- O efeito é transitório, recorrente ou acumulado o suficiente para mudar a
  decisão do trimestre?
- A leitura financeira está conectada a volume, preço, mix, custo, capacidade,
  produtividade, caixa ou outra alavanca operacional?
- Qual acompanhamento de performance deve permanecer ativo após o fechamento?

### Vocabulário de drivers

Use estes termos como candidatos de domínio para a investigação canônica, não
como uma lista fechada nem como uma segunda classificação:

- volume, preço, mix e desconto;
- custo unitário, frete e eficiência operacional;
- preço de material e purchase price variance;
- uso, yield, scrap e qualidade;
- labor rate, labor efficiency e overhead;
- estoque, timing contábil, one-off e premissa de forecast;
- reclassificação.

## Saída

O formato é escolhido somente após a decisão:

- use `skills/number-to-management-story/SKILL.md` para uma leitura estruturada
  ou narrativa executiva;
- use `skills/challenge-variance-explanation/SKILL.md` quando a leitura precisar
  ser pressionada antes da comunicação.

Todos esses callers são adapters. Eles preservam a decisão canônica e mudam
apenas formato, audiência, canal ou densidade.

## Qualidade específica de FP&A

A decisão canônica precisa declarar a qualidade do número. Esta lente adiciona
as perguntas de gestão:

- a variação era esperada no plano ou no forecast?
- ela continua nos próximos meses?
- qual decisão, alerta ou monitoramento decorre dela?

Quando houver custo padrão, use o workflow industrial aplicável para validar
se o standard é atual e atingível. Uma variância favorável pode esconder compra
excessiva, produção sem demanda ou outro comportamento que piora a economia
total.

## Conexões

- Contrato: `skills/explain-variance/SKILL.md`
- Pattern complementar: `_method-wiki/patterns/variance-analysis.md`
- Workflow industrial: `tracks/accounting/workflows/standard-cost-and-industrial-variance-review.md`
- Narrativa: `skills/number-to-management-story/SKILL.md`
