# Checklist de Drivers de Capital de Giro

Checklist para revisar capital de giro operacional, DSO, estoque, payables e conversão de caixa.

Fonte principal: Jack Alexander, *Financial Planning, Analysis, and Performance Management*, Cap. 17.

## Quando Usar

- análise de capital de giro operacional
- revisão de recebíveis, DSO ou past due
- revisão de estoque, giro, DSI, excesso ou obsolescência
- leitura de contas a pagar como financiamento operacional
- forecast de caixa ou de working capital
- diagnóstico de capital preso na operação

## Checklist

### 1. Contexto e Materialidade

- [ ] Capital de giro foi separado entre operacional e financiamento/liquidez.
- [ ] Operating capital foi calculado como % da receita.
- [ ] Giro de capital operacional foi acompanhado.
- [ ] Recebíveis, estoque e payables foram analisados separadamente.
- [ ] A análise considera o modelo de negócio e a indústria.
- [ ] A variação foi comparada com receita, COGS, compras e crescimento.

### 2. Accountability e Processo

- [ ] O dono de cada driver foi identificado.
- [ ] Recebíveis não foram atribuídos apenas a Finance.
- [ ] Estoque não foi atribuído apenas a manufatura ou armazém.
- [ ] Drivers de vendas, forecast, qualidade, produto, compras e produção foram considerados.
- [ ] Existe dashboard ou visibilidade recorrente dos indicadores críticos.

### 3. Contas a Receber

- [ ] DSO foi calculado e comparado com histórico.
- [ ] BPDSO foi estimado com base nos termos de crédito ponderados por receita.
- [ ] A diferença entre DSO real e BPDSO foi explicada.
- [ ] Past due foi aberto por cliente, idade, valor e causa.
- [ ] DSO count-back foi considerado quando há faturamento concentrado no fim do período.
- [ ] Revenue linearity foi avaliada.
- [ ] Devoluções, disputas, documentação incompleta ou erros de faturamento foram analisados.
- [ ] Customer cash management lag foi considerado.
- [ ] Recebimentos foram conciliados com roll-forward de AR quando necessário.

### 4. Estoques

- [ ] Inventory turns e DSI foram calculados.
- [ ] Estoque foi aberto por categoria relevante.
- [ ] Excess and obsolete inventory foi medido e trendado.
- [ ] Root cause de E&O foi analisado: forecast, qualidade, new product, end-of-life ou outro.
- [ ] Forecast accuracy foi conectado a excesso ou ruptura de estoque.
- [ ] Mix produzido foi comparado ao mix vendido.
- [ ] Supplier performance, lead time e cycle time foram considerados.
- [ ] Número de SKUs ou partes únicas foi avaliado.
- [ ] Purchase commitments foram incluídos como indicador líder de estoque futuro.
- [ ] Top itens de maior valor foram revisados.

### 5. Contas a Pagar

- [ ] DPO ou days payable foi acompanhado.
- [ ] Prazos contratuais foram comparados com prazo real de pagamento.
- [ ] Alongamento de fornecedor foi separado de melhoria estrutural.
- [ ] Risco de preço maior, pior serviço ou tensão com fornecedor foi considerado.
- [ ] Concentração de pagamentos futuros foi avaliada no forecast de caixa.

### 6. Impacto em Caixa e Valor

- [ ] A análise mostra quanto caixa está preso em recebíveis e estoque.
- [ ] Oportunidades de redução de DSO, estoque ou capital operacional foram quantificadas.
- [ ] Efeito em ROIC, asset turnover ou retorno foi considerado quando relevante.
- [ ] Risco de write-off, inadimplência ou obsolescência foi declarado.
- [ ] Ações foram conectadas a responsáveis e indicadores líderes.

## Perguntas de Challenge

1. O caixa piorou por crescimento saudável ou por processo ineficiente?
2. O DSO alto vem de prazo contratado, past due, erro de faturamento, qualidade ou revenue hockey stick?
3. O estoque alto vem de demanda real, forecast errado, mix errado, lead time, qualidade ou fim de vida?
4. O contas a pagar está financiando a operação de forma sustentável ou apenas empurrando problema?
5. Quem é dono do driver que criou o saldo, não apenas do saldo contábil?
6. Que indicador avisaria antes do problema aparecer no caixa?

## Sinais de Alerta

- saldo de recebíveis crescendo mais rápido que receita
- DSO subindo com past due e devoluções também subindo
- concentração de faturamento no fim do trimestre
- estoque crescendo enquanto pedidos atrasados continuam
- E&O crescendo por forecast ou fim de vida
- purchase commitments altos apesar de demanda incerta
- payables aumentando por atraso deliberado com fornecedor crítico
- análise de capital de giro sem roll-forward

## Saída Recomendada

```markdown
## Tese de Capital de Giro

[mensagem sobre caixa preso, driver principal e implicação]

## Componentes

| Componente | Métrica | Tendência | Driver provável | Ação |
|---|---:|---|---|---|
| Recebíveis | [DSO/BPDSO/past due] | [tendência] | [driver] | [ação] |
| Estoque | [DSI/turns/E&O] | [tendência] | [driver] | [ação] |
| Payables | [DPO] | [tendência] | [driver] | [ação] |

## Caixa e Risco

[impacto em caixa, write-off, obsolescência, fornecedor ou liquidez]

## Indicadores Líderes

- [indicador 1]
- [indicador 2]
- [indicador 3]
```

## Módulos Relacionados

- Workflow: `tracks/accounting/workflows/working-capital-and-cash-conversion-review.md`
- Conceito: `concepts/working-capital-foundations.md`
- Workflow: `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md`
- Workflow: `tracks/accounting/workflows/inventory-and-valuation-review.md`
