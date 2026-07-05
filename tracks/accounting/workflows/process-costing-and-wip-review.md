# Workflow -- Process Costing e Revisão de WIP

## Quando usar

Use este workflow quando houver:

- produção contínua ou grande volume de unidades homogêneas
- necessidade de calcular custo por processo, departamento ou estágio
- saldo material de WIP
- dúvida sobre unidades equivalentes ou percentual de conclusão
- transferência de custos entre departamentos produtivos
- operação híbrida com partes padronizadas e customização posterior

## Objetivo

Verificar se os custos de produção foram acumulados e distribuídos corretamente entre unidades concluídas, WIP e produto acabado.

O workflow responde:

1. process costing é apropriado para a operação?
2. o fluxo físico de unidades reconcilia?
3. materiais e custos de conversão foram separados corretamente?
4. as unidades equivalentes e o percentual de conclusão são defensáveis?
5. o método escolhido distribui adequadamente os custos entre períodos?

## Quando process costing faz sentido

É adequado quando:

- há grande volume de produção
- as unidades são substancialmente homogêneas
- não é econômico rastrear o custo individual
- materiais, mão de obra e overhead podem ser acumulados por processo

Se produtos, lotes ou customizações têm consumo materialmente diferente, considerar sistema híbrido ou job costing para essa parcela.

## Entradas esperadas

- fluxo físico de unidades por processo ou departamento
- WIP inicial e final
- unidades iniciadas, concluídas e transferidas
- percentual de conclusão de materiais e conversão
- custos do WIP inicial
- materiais adicionados no período
- mão de obra e overhead de conversão
- método aplicado: média ponderada, padrão ou FIFO
- lançamentos entre WIP, produto acabado e CPV
- evidência operacional do estágio de produção

## Sequência de trabalho

### 1. Mapear o fluxo produtivo

Documentar:

- onde o material entra
- em quais etapas ocorre conversão
- quando as unidades são transferidas
- quais departamentos acumulam custo
- onde existe customização ou processamento diferente

### 2. Reconciliar o fluxo físico

Usar:

> WIP inicial + unidades iniciadas = unidades concluídas e transferidas + WIP final

Investigar qualquer diferença antes de distribuir custos.

### 3. Separar materiais de custos de conversão

Materiais podem ser adicionados:

- no início do processo
- ao longo do processo
- em um ponto específico

Mão de obra e overhead normalmente são adicionados ao longo da conversão. Por isso, materiais e conversão podem exigir percentuais de conclusão distintos.

### 4. Calcular unidades equivalentes

Para cada componente:

> Unidades equivalentes = unidades físicas × percentual de conclusão

Não aplicar automaticamente o percentual de conversão aos materiais.

Exemplo: 200 unidades em WIP com materiais integralmente adicionados e conversão em 30% representam:

- 200 unidades equivalentes de materiais
- 60 unidades equivalentes de conversão

### 5. Escolher e testar o método

| Método | Tratamento | Quando usar |
|---|---|---|
| Média ponderada | Combina custos do WIP inicial com custos do período | Ambiente simples e custos relativamente estáveis |
| FIFO | Separa trabalho e custo do período anterior do trabalho atual | Oscilação relevante de custos e necessidade de tendência por período |
| Custo padrão | Aplica padrões às unidades equivalentes e separa variâncias | Operação com standard costing disciplinado |

FIFO oferece maior precisão entre períodos, mas só deve ser usado quando o ganho decisório justificar a complexidade.

### 6. Distribuir os custos

Separar:

- custo das unidades concluídas e transferidas
- custo do WIP final
- custo de materiais
- custo de conversão
- custo do WIP inicial, quando o método exigir segregação

Confirmar que o total distribuído reconcilia com o total de custos a contabilizar.

### 7. Testar o percentual de conclusão

O percentual de conclusão é a principal área de julgamento e risco.

Validar com:

- estágio físico observável
- consumo de horas ou máquina
- marcos produtivos
- inspeção de engenharia ou produção
- histórico por processo
- consistência com períodos anteriores

Red flags:

- mudança pequena no percentual que produz efeito relevante no lucro
- percentual informado apenas pelo gestor com incentivo ligado ao resultado
- início anormal de produção no último dia do período
- padrão fixo sem validação do fluxo real
- WIP crescente sem aumento compatível de throughput

### 8. Avaliar sistema híbrido

Usar modelo híbrido quando:

- o processamento básico é homogêneo
- materiais ou acabamentos variam por lote, pedido ou produto
- process costing funciona para conversão comum
- job costing funciona melhor para customização específica

### 9. Revisar lançamentos e impacto

Reconciliar:

- materiais para WIP
- conversão para WIP
- WIP transferido para produto acabado
- produto acabado transferido para CPV
- variâncias, quando houver custo padrão

Quantificar o efeito de qualquer erro em WIP, produto acabado, CPV, margem e resultado.

## Estrutura de saída sugerida

1. Adequação do método à operação.
2. Reconciliação do fluxo físico.
3. Unidades equivalentes de materiais e conversão.
4. Custo por unidade equivalente.
5. Alocação entre concluído e WIP final.
6. Julgamentos e riscos no percentual de conclusão.
7. Ajustes contábeis e correções de processo.

## Guardrails

- Não usar process costing para produtos materialmente diferentes sem camada híbrida.
- Não tratar percentual de conclusão como dado objetivo sem evidência.
- Não misturar materiais e conversão quando entram em momentos diferentes.
- Não aceitar alocação que não reconcilie com custos e unidades totais.
- Não interpretar aumento de WIP como produção concluída.
- Se houver padrão e variâncias relevantes, usar também `standard-cost-and-industrial-variance-review.md`.
- Para perda de valor ou método de estoque, usar também `inventory-and-valuation-review.md`.

## Fonte de promoção

- Steven Bragg, *Cost Accounting Fundamentals*, Cap. 6 — Process Costing.
