# Lente de análise de Variance

> Fonte mestra: `skills/explain-variance/SKILL.md`.
> Revisão do adapter: `2026-09-26`.

## Quando usar

Use esta lente quando o material trouxer `Actual` contra `Budget`, `Forecast`,
período anterior ou outra referência explícita, e a tarefa for explicar ou
questionar a variação.

Se a causa ainda não estiver delimitada, trate a análise como investigação. A
lente não autoriza inventar um driver só porque o número mudou.

## Objetivo

Transformar a variação em uma leitura que preserve baseline, materialidade,
driver, evidência, impacto, recorrência e ação em poucos passos.

## Roteiro mínimo

1. Declare `Actual`, referência, unidade, período e fórmula da variação.
2. Avalie materialidade por valor, percentual, risco ou relevância decisória.
3. Localize o movimento por linha, unidade, produto, cliente, projeto ou centro
   de custo.
4. Abra os drivers relevantes: volume, preço, mix, custo, eficiência, frete,
   estoque, timing, reclassificação ou outro driver observável.
5. Para cada driver, separe fato confirmado, hipótese e lacuna de evidência.
6. Verifique se os impactos conhecidos reconciliam com a variação total.
7. Conecte o efeito a margem, EBITDA, caixa, forecast, capital ou operação.
8. Registre se o efeito é recorrente, `timing`, `one-off` ou desconhecido. Para
   `timing` e `one-off`, informe a reversão, o encerramento ou a justificativa
   de não recorrência.
9. Feche com ação, owner, prazo ou próximo teste de evidência.

## Estrutura de resposta

```md
## Leitura principal

[Actual contra a referência, magnitude, direção e nível de certeza]

## Drivers

| Driver | Status | Impacto | Evidência ou lacuna |
|---|---|---:|---|
| [driver principal] | [confirmado/hipótese/lacuna] | [valor] | [base] |

## Impacto

[efeito em margem, EBITDA, caixa, forecast, capital ou operação]

## Recorrência e risco

[recorrente, timing, one-off ou desconhecido; detalhe necessário]

## Ação

[validar, corrigir, monitorar ou obter evidência; owner e prazo]
```

## Guardrails

- Não tratar “custo subiu” como explicação suficiente.
- Não chamar uma hipótese de causa confirmada.
- Não esconder diferença de reconciliação para deixar a narrativa mais limpa.
- Não usar “timing” sem dizer quando o efeito reverte.
- Não usar “one-off” sem explicar por que não tende a se repetir.
- Não criar uma segunda regra de `Variance` em um adapter de formato.
