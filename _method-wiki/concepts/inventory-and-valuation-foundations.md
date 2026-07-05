# Inventory and Valuation Foundations

## Ideia central

Estoque não é apenas saldo patrimonial.

Ele conecta operação, custo, margem, capital de giro e qualidade do resultado.

Quantidade confiável é condição necessária, mas não suficiente. Depois de confirmar o saldo físico e transacional, ainda é preciso testar atribuição de custo, overhead e perda de valor.

## Cadeia de valuation

| Camada | Função | Falha típica |
|---|---|---|
| Quantidade | Determinar quais unidades existem e em qual estágio | movimento ausente, cut-off ou unidade de medida |
| Método de custo | Atribuir custo às unidades consumidas e remanescentes | FIFO incorreto, média distorcida ou padrão obsoleto |
| Landed cost e overhead | Incorporar custos elegíveis de aquisição e conversão | base de rateio ruim ou ineficiência capitalizada |
| Perda de valor | Limitar o ativo ao valor recuperável | obsolescência ou deterioração reconhecida tarde |

O erro em qualquer camada pode alterar simultaneamente estoque final, CPV e margem bruta.

## Dimensões de leitura

| Dimensão | Pergunta |
|---|---|
| Quantidade | O saldo contábil conversa com a posição física? |
| Valuation | O critério de mensuração está consistente e defensável? |
| Giro | O estoque está rodando ou virando capital parado? |
| Obsolescência | Existe item sem giro, perda esperada ou necessidade de provisão? |
| Custo | O estoque está absorvendo custo normal ou ineficiência? |
| Margem | A margem do período foi afetada por estoque, absorção ou corte? |

## Métodos de custo

- **FIFO:** tende a acompanhar o fluxo físico normal e deixa o estoque final mais próximo dos custos recentes. Exige integridade de datas, camadas e sequência de consumo.
- **Média ponderada:** simplifica o cálculo e reduz a manutenção de camadas, mas pode suavizar mudanças relevantes de custo.
- **Custo padrão:** oferece benchmark e velocidade operacional, mas depende de padrão atualizado e tratamento disciplinado das variâncias.

O método escolhido não corrige uma base ruim. Valuation sofisticado sobre quantidades frágeis produz falsa precisão.

## Efeitos comuns

- diferença física
- ajuste de inventário
- mudança de custo padrão
- alteração de rateio ou absorção
- obsolescência
- perda, scrap ou rework
- efeito temporário de corte ou timing

## Red flags

- margem melhorando por aumento de estoque sem base operacional
- itens sem giro mantidos a valor íntegro
- ajuste físico recorrente sem causa tratada
- custo padrão descolado da realidade
- perdas diluídas sem transparência

## Conexões operacionais

- Workflow: `tracks/accounting/workflows/inventory-and-valuation-review.md`
- Workflow: `tracks/accounting/workflows/process-costing-and-wip-review.md`
- Workflow: `tracks/accounting/workflows/standard-cost-and-industrial-variance-review.md`
- Conceito relacionado: `concepts/working-capital-foundations.md`
- Pattern relacionado: `patterns/gross-margin-bridge.md`

## Fonte de promoção

- Steven Bragg, *Cost Accounting Fundamentals*, Cap. 4 — Inventory Valuation.
