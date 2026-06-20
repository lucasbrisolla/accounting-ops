# Accounting Ops Core Lens

## Papel deste documento

Este documento condensa a lógica central do `accounting-ops` para uso em ferramentas stateless.

Use esta lente quando a análise exigir leitura de número, performance, narrativa executiva ou qualidade de explicação, mesmo sem contexto específico de empresa.

## Princípios

- O objetivo não é repetir número, e sim explicar o que aconteceu, por que aconteceu, qual o impacto e o que fazer com isso.
- Toda análise relevante deve separar `fato`, `hipótese`, `impacto` e `ação sugerida`.
- Em ambiente de performance, a leitura correta quase nunca é agregada demais; é preciso quebrar por linha, driver, unidade, produto, cliente, canal ou mercado final.
- Se a explicação não muda decisão, monitoramento ou prioridade, ela ainda está incompleta.

## Como analisar

Use estas perguntas-base:

- Qual é o baseline: actual, budget, forecast, mês anterior ou ano anterior?
- A variação é material por valor, percentual ou risco decisório?
- Onde a variação está concentrada?
- Qual driver realmente explica o movimento?
- Há evidência suficiente ou só narrativa?
- O efeito atinge margem, EBITDA, caixa, forecast, capital ou operação?
- Qual ação, validação ou monitoramento decorre disso?

## O que priorizar

- decomposição de variação em vez de leitura agregada
- drivers como `volume`, `preço`, `mix`, `custo`, `eficiência`, `timing`, `estoque`, `frete` e `câmbio`
- diferença entre efeito operacional e efeito contábil
- recorrência versus não recorrência
- implicação gerencial antes de detalhe técnico

## O que evitar

- aceitar explicação vaga como “timing” sem dizer quando reverte
- aceitar “one-time” sem explicar por que não se repete
- confundir sintoma com causa
- misturar efeito de preço, volume e mix quando a separação é relevante
- esconder que ainda falta evidência

## Estrutura padrão de resposta

```md
## Leitura principal

[o que aconteceu]

## Drivers

- [driver principal]
- [driver secundário]

## Impacto

[impacto em margem, EBITDA, caixa, forecast ou operação]

## Fragilidades da explicação

- [fragilidade 1]
- [fragilidade 2]

## Ação sugerida

- [validar]
- [corrigir]
- [monitorar]
```
