# Pattern: Gross Margin Bridge

## Papel

Estrutura recorrente para explicar variação de margem bruta entre dois períodos ou contra plano.

## Estrutura base

1. Variação total da margem em valor.
2. Variação total da margem em percentual.
3. Decomposição por drivers.
4. Classificação do efeito.
5. Mensagem gerencial.

## Drivers típicos

| Driver | Pergunta |
|---|---|
| Volume | Quanto da variação vem de vender mais ou menos? |
| Preço | Quanto vem de aumento, redução ou erosão de preço? |
| Mix | A composição de produtos, clientes ou canais mudou? |
| Custo | O custo unitário mudou por insumo, mão de obra, overhead ou eficiência? |
| Descontos | A receita nominal esconde concessões comerciais? |
| Qualidade | Há perdas, scrap, rework ou retrabalho relevantes? |
| Outros | Existe efeito de câmbio, corte, classificação ou não recorrente? |

## Classificação

Para cada driver, classificar como:

- comercial
- operacional
- custo externo
- contábil ou de corte
- pontual
- recorrente

## Saída esperada

Uma boa bridge deve permitir dizer:

- o que mais puxou a margem
- se o efeito é estrutural ou temporário
- qual ação protege ou recompõe margem
- qual indicador precisa ser monitorado

## Conexões operacionais

- Workflow: `tracks/fpa/workflows/gross-margin-bridge.md`
- Heuristic: `heuristics/margin-erosion-signals.md`
