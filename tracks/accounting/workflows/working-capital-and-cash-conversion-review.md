# Workflow -- Capital de Giro Operacional e Conversão de Caixa

## Quando usar

Use este workflow quando o usuário pedir:

- revisão de capital de giro operacional
- análise de DSO, recebíveis, estoque, payables ou cash conversion
- explicação de lucro crescendo com caixa piorando
- leitura de capital preso em contas a receber ou estoque
- revisão de forecast de capital de giro e fluxo de caixa operacional
- diagnóstico de eficiência de processos que aparecem no balanço

## Objetivo

Transformar capital de giro em leitura de processo, caixa e risco.

O workflow existe para responder, em ordem:

1. quanto capital está preso na operação?
2. quais processos explicam recebíveis, estoque e payables?
3. onde há oportunidade real de liberar caixa sem destruir relação comercial ou operação?
4. quais indicadores líderes mostram se o caixa vai melhorar ou piorar?

## Princípio central

O balanço é um retrato de transações em processo.

Recebíveis altos, estoque excessivo e payables alongados não são apenas saldos contábeis. Eles revelam qualidade de previsão, faturamento, cobrança, entrega, produção, compras, desenho de produto, relação com clientes e fornecedores.

## Entradas esperadas

Sempre que possível, trabalhar com algum destes insumos:

- balanço e DRE por mês
- fluxo de caixa ou forecast de caixa
- contas a receber por aging, cliente e vencimento
- DSO, BPDSO, past due e padrão de faturamento
- estoque por categoria, aging, giro, DSI, E&O e top itens
- contas a pagar, prazos com fornecedores e purchase commitments
- forecast de receita, produção, compras e COGS
- indicadores de qualidade, devoluções, pedidos em atraso e forecast accuracy

## Sequência de trabalho

### 1. Definir o capital operacional

Separar:

- contas a receber
- estoque
- contas a pagar
- accrued liabilities operacionais

Tratar caixa e dívida de curto prazo como financiamento/liquidez, não como operação, quando o objetivo for medir operating capital.

### 2. Medir materialidade e tendência

Começar por:

- operating capital como % da receita
- giro de capital operacional
- DSO
- inventory turns e DSI
- DPO ou days payable
- variação de recebíveis, estoque e payables contra receita, COGS e compras

Capital de giro deve ser lido junto com crescimento. Receita maior pode exigir mais capital, mas aumento desproporcional geralmente aponta problema de processo.

### 3. Revisar recebíveis como processo de receita

Para contas a receber, testar:

- termos de crédito por cliente, canal, região ou produto
- BPDSO, ou DSO possível se todos pagassem no prazo contratual
- diferença entre DSO real e BPDSO
- past due por cliente, idade e causa
- qualidade de faturamento, pedido, entrega e documentação
- devoluções, disputas e problemas de qualidade
- concentração de faturamento no fim do mês ou trimestre
- cash management lag do cliente

DSO alto não é sempre cobrança fraca. Pode ser contrato, erro de faturamento, problema de produto, documentação incompleta, revenue hockey stick ou cliente segurando caixa.

### 4. Revisar estoque como processo de demanda, compras e produção

Para estoque, testar:

- giro e DSI por categoria relevante
- excesso e obsolescência
- root cause de E&O: forecast, qualidade, end-of-life, novo produto ou outro
- forecast accuracy e mix vendido contra mix produzido
- lead time, cycle time e flexibilidade produtiva
- supplier quality e entregas atrasadas
- número de SKUs ou partes únicas
- past-due customer orders
- compromissos de compra já assumidos
- top 20-50 itens que concentram valor

Estoque alto pode vir de demanda superestimada, mix errado, baixa flexibilidade, design ruim, qualidade fraca, excesso de variedade ou má gestão de fim de vida.

### 5. Revisar payables sem romantizar alongamento

Para contas a pagar, testar:

- prazo médio de pagamento
- mudança de prazo versus contrato
- concentração de pagamentos futuros
- dependência de atraso com fornecedor para sustentar caixa
- custo implícito de alongar pagamento: preço, serviço, prioridade, qualidade ou relação

Alongar fornecedor pode melhorar caixa no curto prazo, mas pode destruir valor se gerar preço maior, pior serviço ou perda de parceria.

### 6. Fazer roll-forward operacional

Quando o problema for forecast ou explicação de variação, montar roll-forward:

- recebíveis: saldo inicial + vendas - recebimentos - write-offs/ajustes
- estoque: saldo inicial + compras/produção + overhead aplicado - COGS - perdas/write-offs
- payables: saldo inicial + compras/faturas - pagamentos

O roll-forward ajuda a separar crescimento normal, erro de previsão, atraso operacional e decisão de gestão.

### 7. Fechar oportunidade e risco

Responder:

- quanto caixa poderia ser liberado por redução de DSO, estoque ou melhoria de giro
- quais ações são operacionais versus financeiras
- qual risco de write-off, obsolescência, inadimplência ou ruptura
- quais indicadores devem entrar no dashboard
- quem é dono de cada driver, não apenas do saldo final

## Estrutura de saída sugerida

1. Resumo executivo do capital de giro.
2. Operating capital por componente e tendência.
3. Recebíveis: DSO, BPDSO, past due e causas.
4. Estoque: DSI, E&O, forecast, supply chain e top itens.
5. Payables: prazo, sustentabilidade e trade-off com fornecedores.
6. Caixa preso, oportunidade de liberação e riscos.
7. Ações, responsáveis e indicadores líderes.

## Red flags

- lucro crescendo com caixa operacional piorando
- DSO subindo sem bridge entre BPDSO, past due e revenue linearity
- past due tratado como problema de cobrança sem root cause
- estoque subindo por mix errado, forecast fraco ou produtos em fim de vida
- E&O crescendo sem análise de causa
- payables alongados para esconder pressão de liquidez
- capital de giro sem ownership fora de Finance
- dashboard olhando só saldo contábil e não drivers de processo

## Guardrails

- Não tratar recebíveis como problema apenas de cobrança.
- Não tratar estoque como problema apenas de armazém ou valuation.
- Não vender alongamento de fornecedor como melhoria estrutural sem avaliar custo e relação.
- Não avaliar caixa operacional só pelo saldo bancário.
- Se faltar aging, roll-forward, termos comerciais ou dados operacionais, declarar a limitação.

## Módulos relacionados

- Conceito: `_method-wiki/concepts/working-capital-foundations.md`
- Checklist: `_method-wiki/checklists/working-capital-driver-checklist.md`
- Workflow: `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md`
- Workflow: `tracks/accounting/workflows/inventory-and-valuation-review.md`
- Processo: `_method-wiki/processes/dashboard-and-kpi-design.md`
