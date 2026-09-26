# Pattern: Variance Analysis

## Papel

Este pattern ajuda a escolher uma lente de decomposição para uma pergunta de
`Variance`. Ele é uma referência metodológica complementar; não é o contrato
canônico. O módulo canônico é
`skills/explain-variance/SKILL.md`. A decisão de baseline, materialidade, driver, evidência,
recorrência, confiança, reconciliação e ação pertence a
`skills/explain-variance/SKILL.md`.

## Costura de uso

1. Carregue `skills/explain-variance/SKILL.md` para construir uma
   `VarianceExplanation`.
2. Use as decomposições deste pattern para investigar a dimensão adequada ao
   domínio.
3. Encaminhe a decisão para challenge, one-pager ou narrativa somente depois
   que a explicação estiver registrada.

O pattern não deve ser carregado como uma fonte concorrente do modo de FP&A ou
dos adapters de saída. Ele oferece vocabulário e perguntas de decomposição;
não cria uma segunda regra para o mesmo número.

## Sinais para priorizar investigação

Estes sinais são candidatos para a avaliação de materialidade do módulo
canônico, não limiares adicionais:

- valor absoluto relevante;
- percentual relevante sobre a base;
- direção inesperada;
- impacto em margem, EBITDA, caixa ou covenant;
- recorrência acumulada;
- mudança nova em uma conta antes estável.

## Decomposições úteis

| Tipo de variação | Quebra recomendada |
|---|---|
| Receita | preço, volume, mix, câmbio, devoluções, timing |
| Custo industrial | volume, consumo, eficiência, preço de insumo, mix, absorção |
| Margem | preço/volume/mix, custo unitário, capacidade, sucata, frete |
| Pessoal | headcount, salário médio, horas extras, encargos, bônus |
| OPEX | categoria de gasto, fornecedor, timing, reclassificação, não recorrente |
| Câmbio | taxa, exposição, hedge, data de reconhecimento |

### Decomposição industrial por custo padrão

Quando existir standard costing, separar a investigação em:

| Componente | Rate ou preço | Uso, eficiência ou volume |
|---|---|---|
| Material | preço de compra | consumo, yield, scrap e qualidade |
| Mão de obra | taxa e mix de função | horas, setup, treinamento e downtime |
| Overhead variável | spending rate | eficiência da base de atividade |
| Overhead fixo | gasto contra orçamento | volume, capacidade e absorção |

Antes de comunicar a variância, validar no workflow industrial se o padrão é
atual, atingível e coerente com volume, equipamento, processo e condições de
compra.

Uma variância favorável não prova boa performance. Compra em excesso, produção
sem demanda ou postergação de manutenção podem melhorar o indicador e piorar a
economia total.

Se a decisão canônica classificar o efeito como `timing`, registrar o evento de
reversão. Se classificar como `one-off`, preservar a justificativa de não
recorrência na ação ou na evidência.

## Conexões operacionais

- Contrato canônico: `skills/explain-variance/SKILL.md`
- Modo de FP&A: `tracks/fpa/modes/variance-analysis.md`
- Workflow industrial: `tracks/accounting/workflows/standard-cost-and-industrial-variance-review.md`
- Challenge: `skills/challenge-variance-explanation/SKILL.md`
- Narrativa: `skills/number-to-management-story/SKILL.md`
