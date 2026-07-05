# Workflow -- Estoque e Revisão de Valuation

## Quando usar

Use este workflow quando o usuário pedir:

- revisão de estoque contábil versus físico
- investigação de FIFO, custo médio ou custo padrão
- análise de valuation, overhead ou absorção
- apoio para entender obsolescência, perdas ou provisões
- investigação de impacto de estoque em CPV, margem e resultado
- ponte entre operação, cost accounting e qualidade do número

## Objetivo

Transformar a revisão de estoque em uma leitura integrada de quantidade, atribuição de custo, overhead e perda de valor.

O workflow existe para responder, em ordem:

1. a quantidade registrada é confiável?
2. o método de custo foi aplicado corretamente?
3. landed cost e overhead foram incorporados de forma consistente?
4. o estoque ainda recupera o valor pelo qual está registrado?
5. qual é o impacto em estoque, CPV, margem e resultado?

## Princípio central

Quantidade confiável é condição necessária, mas não suficiente para valuation correto.

Uma revisão robusta separa quatro camadas:

| Camada | Pergunta |
|---|---|
| Quantidade | O rollforward físico e contábil fecha? |
| Método de custo | FIFO, média ponderada ou custo padrão foram aplicados de forma consistente? |
| Landed cost e overhead | Os custos elegíveis foram incorporados à categoria correta e na base adequada? |
| Perda de valor | Obsolescência, dano ou preço de venda insuficiente exigem provisão ou write-down? |

## Entradas esperadas

Sempre que possível, trabalhar com:

- subledger e razão de estoque
- posição física ou inventário
- rollforward de quantidade e valor
- histórico de recebimentos, produção, consumos, transferências e saídas
- custo unitário por lote, camada ou item
- invoices, fretes, câmbio e componentes de landed cost
- critérios de FIFO, média ponderada ou custo padrão
- taxas e bases de overhead
- posição de matéria-prima, WIP e produto acabado
- aging, giro, preço de venda e custos de conclusão ou venda
- provisões para obsolescência, perdas e write-downs
- análise de margem, CPV, produção e variâncias

## Sequência de trabalho

### 1. Definir o recorte da revisão

Confirmar:

- período
- entidade, planta, armazém ou centro de custo
- tipo de estoque
- itens ou famílias materiais
- comparativo principal
- método de custo oficialmente adotado

### 2. Validar quantidade e cut-off

Começar por:

- saldo inicial + entradas - saídas = saldo final
- saldo contábil versus posição física
- unidade de medida consistente
- movimentos duplicados, ausentes ou fora do período
- estoque negativo ou consumo anterior à entrada
- transferências registradas nos dois locais
- recebimentos, produção e embarques próximos à virada do mês

Se a quantidade não fecha, declarar que ainda não há base para concluir que o problema é de valuation.

### 3. Identificar e testar o método de custo

| Método | Quando tende a ser útil | Teste principal | Risco típico |
|---|---|---|---|
| FIFO | Fluxo físico normal e custos variáveis entre períodos | Reconstruir camadas e consumir primeiro as mais antigas | Camada negativa, backdating ou consumo fora de sequência |
| Média ponderada | Produção homogênea e baixa necessidade de rastrear camadas | Reconciliar custos totais e unidades equivalentes | Suavizar mudança recente ou volatilidade de custo |
| Custo padrão | Operação com padrões mantidos e variâncias disciplinadas | Validar padrão, atualização e tratamento das variâncias | Padrão obsoleto ou ineficiência capitalizada |

Não escolher um método apenas pela sofisticação. O método precisa refletir a operação e produzir informação útil.

### 4. Testar integridade de FIFO

Para itens materiais:

1. Ordenar saldo inicial e entradas por data.
2. Registrar quantidade e custo unitário de cada camada.
3. Consumir primeiro as camadas mais antigas.
4. Comparar as camadas remanescentes com o estoque final registrado.
5. Comparar o custo consumido esperado com o CPV contabilizado.
6. Localizar o primeiro movimento em que a reconstrução diverge do sistema.

Procurar:

- camadas negativas
- datas invertidas ou movimentos retroativos
- custos zerados ou anormais
- consumo de lote recente antes do lote antigo
- invoice, frete ou câmbio lançados depois do consumo
- unidade de medida ou conversão incorreta
- custo de entrada substituído ou recalculado sem trilha

### 5. Localizar a natureza da divergência

| Divergência | Hipótese mais provável |
|---|---|
| Quantidade final correta, valor final incorreto | custo unitário, camada, landed cost ou overhead |
| Estoque final superavaliado e CPV subavaliado | consumo de camadas recentes, custo ausente ou perda de valor não registrada |
| Estoque final subavaliado e CPV superavaliado | consumo excessivo de camadas antigas ou entrada subavaliada |
| Camada negativa | cut-off, backdating, movimento ausente ou configuração do ERP |
| Método correto, margem ainda distorcida | overhead, padrão, provisão ou classificação |
| Diferença concentrada na virada do mês | cut-off de recebimento, produção, embarque ou invoice |

### 6. Revisar landed cost, overhead e absorção

Testar:

- quais componentes formam o custo de entrada
- se frete, câmbio, tributos e outros custos elegíveis foram tratados de forma consistente
- se overhead de fabricação foi aplicado a WIP e produto acabado
- se matéria-prima recebeu custo de conversão indevido
- se a base de alocação conversa com o consumo real de recursos
- se capacidade ociosa ou ineficiência foi capitalizada sem transparência
- se mudanças de taxa explicam variações de margem ou estoque

### 7. Testar perda de valor e obsolescência

Revisar:

- itens danificados, deteriorados ou sem giro
- excesso frente à demanda e aos compromissos de compra
- preço de venda esperado
- custos necessários para concluir e vender
- valor esperado de descarte, devolução ou recuperação
- timing e suficiência da provisão

Obsolescência deve ser reconhecida quando o risco é identificado, e não somente quando o item é vendido ou descartado.

### 8. Usar estimativas somente com limite explícito

O método do lucro bruto pode apoiar uma estimativa interina, destruição de estoque ou contingência documental.

Não deve substituir:

- apuração regular do estoque
- reconstrução de quantidade e custo
- valuation de fechamento anual
- evidência adequada para demonstrações auditadas

### 9. Fechar impacto e ação

Quantificar:

- ajuste no estoque final
- ajuste no CPV
- efeito na margem bruta e no resultado
- provisão ou write-down necessário
- efeito tributário, quando aplicável
- correção imediata de lançamento
- correção estrutural de processo, cadastro ou ERP

## Estrutura de saída sugerida

1. Resumo executivo do estoque.
2. Confiabilidade da quantidade e do cut-off.
3. Resultado do teste do método de custo.
4. Diferenças de landed cost, overhead ou absorção.
5. Obsolescência e perda de valor.
6. Impactos em estoque, CPV, margem e resultado.
7. Ajustes imediatos e correções estruturais.

## Red flags

- camadas FIFO negativas ou muito antigas
- ajustes manuais recorrentes perto do fechamento
- custo padrão sem revisão e variâncias acumuladas
- custos zerados em entradas relevantes
- margem melhorando por aumento de estoque sem base operacional
- overhead crescendo com produção ou capacidade em queda
- matéria-prima recebendo overhead de conversão inadequado
- itens sem giro mantidos a valor integral
- write-down reconhecido apenas após venda, descarte ou auditoria
- uso recorrente do método do lucro bruto para fechar estoque

## Guardrails

- Não olhar estoque apenas como saldo patrimonial.
- Não discutir FIFO sobre uma base de quantidade pouco confiável.
- Não assumir que reconciliação física garante valuation correto.
- Não tratar efeito de estoque como performance sem separar timing e absorção.
- Não aplicar lower of cost or market sem adaptar o teste ao framework contábil aplicável.
- Se o foco for produção contínua e WIP, usar também `process-costing-and-wip-review.md`.
- Se o foco for padrão e desvios industriais, usar também `standard-cost-and-industrial-variance-review.md`.
- Quando o foco for caixa preso e giro, usar também `working-capital-and-cash-conversion-review.md`.

## Fonte de promoção

- Steven Bragg, *Cost Accounting Fundamentals*, Cap. 4 — Inventory Valuation.
- Steven Bragg, *The New Controller Guidebook*, Cap. 5 — Inventory Management.
