# skill: prepare-journal-entry-support

## Goal

Preparar suporte para lançamento contábil manual com racional, débito/crédito, documentação, reversão e pontos de revisão.

Esta skill não substitui julgamento técnico-contábil nem aprovação formal. Ela organiza a evidência e pressiona a qualidade do lançamento antes de ele virar parte do fechamento.

## Use When

- preparar accrual de despesa ou receita
- registrar amortização de prepaid
- registrar depreciação ou amortização
- estruturar ajuste de reconciliação
- documentar lançamento manual relevante
- revisar se um lançamento tem suporte suficiente

## Quando NÃO usar

- quando a pergunta é só narrativa executiva do resultado
- quando a regra contábil aplicável ainda não foi definida
- quando não há valor, conta, período ou evento minimamente identificado

## Tipos recorrentes de lançamento

### Accrual de AP ou despesa

Uso: bens ou serviços recebidos, mas ainda não faturados.

Estrutura típica:

- débito: despesa ou ativo, se capitalizável
- crédito: provisões ou obrigações acumuladas

Pontos de revisão:

- base do cálculo
- competência
- reversão no período seguinte
- comparação com histórico ou contrato

### Prepaid

Uso: despesa paga antecipadamente e reconhecida ao longo do período de benefício.

Estrutura típica:

- débito: despesa
- crédito: despesa antecipada

Pontos de revisão:

- início e fim do benefício
- cronograma de amortização
- cancelamentos ou aceleração de despesa

### Depreciação e amortização

Uso: reconhecimento periódico de consumo de ativo.

Estrutura típica:

- débito: depreciação ou amortização
- crédito: depreciação ou amortização acumulada

Pontos de revisão:

- base do ativo
- vida útil
- método
- entrada, baixa ou impairment
- centro de custo ou unidade

### Payroll e benefícios

Uso: folha, bônus, encargos e benefícios incorridos no período.

Pontos de revisão:

- dias trabalhados não pagos
- plano de bônus
- encargos patronais
- férias ou PTO, quando aplicável
- competência versus pagamento

### Ajuste de reconciliação

Uso: diferença conciliatória que exige correção contábil.

Pontos de revisão:

- origem da diferença
- evidência de suporte
- conta correta
- impacto em resultado, caixa ou balanço
- se o ajuste corrige causa raiz ou apenas limpa saldo

## Sequência

### 1. Definir o evento

Identificar:

- o que aconteceu
- período de competência
- entidade ou unidade
- valor
- origem do dado

### 2. Determinar o racional

Explicar:

- por que o lançamento é necessário
- qual conta deve ser debitada
- qual conta deve ser creditada
- se o efeito é resultado, balanço, caixa indireto ou reclassificação

### 3. Organizar o suporte

Listar:

- cálculo
- contrato, pedido, nota, relatório ou memória
- comparação com período anterior, se relevante
- premissas e estimativas

### 4. Testar qualidade

Verificar:

- débitos igualam créditos
- período está correto
- conta e centro de custo fazem sentido
- valor é suportado
- descrição é auditável
- tratamento é consistente com períodos anteriores
- duplicidade foi descartada
- reversão foi definida quando aplicável

### 5. Preparar saída

Produzir:

- tabela do lançamento
- memo curto
- suporte necessário
- pontos de revisão
- efeito gerencial

## Formato sugerido

```markdown
## Lançamento Proposto

| Linha | Conta | Débito | Crédito | Centro/Unidade | Memo |
|---|---|---:|---:|---|---|
| 1 | [conta] | [valor] |  | [centro] | [memo] |
| 2 | [conta] |  | [valor] | [centro] | [memo] |

## Racional

[por que o lançamento é necessário]

## Suporte

- [documento, relatório ou cálculo]

## Reversão

[sim/não, período e motivo]

## Pontos de Revisão

- [ponto 1]
- [ponto 2]

## Efeito Gerencial

[impacto em resultado, balanço, caixa, margem ou apenas classificação]
```

## Red flags

- valor redondo sem memória de cálculo
- accrual sem reversão definida
- lançamento manual em conta controle sem justificativa
- ajuste recorrente que deveria virar correção de processo
- descrição genérica demais para revisão futura
- lançamento que melhora resultado sem evidência operacional

## Guardrails

- Não inventar conta contábil específica se o plano de contas não foi fornecido.
- Não afirmar tratamento técnico definitivo sem política ou evidência.
- Separar efeito contábil de melhoria econômica real.
- Se faltar suporte, dizer exatamente o que falta.
