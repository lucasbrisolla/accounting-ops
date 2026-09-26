# Lente de revisão de Forecast e Outlook

> Fontes mestras: `_method-wiki/checklists/financial-projection-quality-checklist.md` e `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`.
> Revisão do adapter: `2026-09-26`.

## Quando usar

Use esta lente para revisar forecast, rolling forecast, business outlook,
orçamento atualizado ou cenários base, upside e downside.

Quando o material também explicar uma variação histórica, use a lente de
`Variance` para o desvio e esta lente para o número futuro.

## Objetivo

Testar se o forecast representa a melhor estimativa atual, se suas premissas
continuam válidas e se os riscos e ações estão conectados aos drivers que podem
mudar o resultado.

## Roteiro mínimo

1. Defina finalidade, horizonte, granularidade e referência: orçamento,
   forecast anterior ou plano operacional.
2. Compare realizado acumulado, tendência recente e `run rate` com o número
   projetado.
3. Identifique os drivers materiais e voláteis: volume, preço, mix, custo,
   câmbio, capacidade, estoque, inadimplência, CAPEX ou cronograma comercial.
4. Separe premissas válidas, premissas invalidadas e premissas sem evidência.
5. Teste a reversão de tendência: uma melhora forte precisa de evento, ação ou
   capacidade que a sustente.
6. Construa o cenário base como melhor estimativa atual. Mostre upside e
   downside com gatilho, impacto, indicador líder e ação.
7. Verifique, quando relevante, o efeito em DRE, caixa, capital de giro,
   estoque, CAPEX, financiamento e covenants.
8. Feche com o que mudou desde o último forecast, o que precisa ser decidido e
   quando as premissas serão revisitadas.

## Estrutura de resposta

```md
## Tese do Outlook

[melhor estimativa atual e principal mudança]

## Drivers e premissas críticas

- [driver]: [premissa, evidência e indicador]
- [driver]: [premissa, evidência e indicador]

## Cenários

| Cenário | Gatilho | Impacto | Ação |
|---|---|---:|---|
| Base | [condição] | [valor] | [monitoramento] |
| Downside | [condição] | [valor] | [contingência] |
| Upside | [condição] | [valor] | [captura] |

## Fragilidades

- [premissa ou dado mais fraco]

## Próximo checkpoint

[indicador, owner e data ou evento de revisão]
```

## Guardrails

- Não tratar `Budget`, `Operating Plan` e `Forecast` como sinônimos.
- Não transformar cenário único em certeza.
- Não aceitar melhora projetada sem driver verificável.
- Não esconder downside provável em uma nota de rodapé.
- Não preencher lacuna de dados com precisão aparente.
