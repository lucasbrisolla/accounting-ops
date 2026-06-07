# Pattern: Performance Tree

## Papel

Estrutura recorrente para decompor um KPI final em drivers subordinados que expliquem causa, impacto e alavancas de ação.

## Quando usar

- ROIC
- ROE
- margem
- conversão de caixa
- DSO
- produtividade
- qualquer KPI final que esteja correto demais no topo e pouco explicativo na base

## Estrutura base

1. Definir o KPI final.
2. Separar os 2 a 4 drivers imediatamente subordinados.
3. Quebrar cada driver em componentes mais acionáveis.
4. Parar quando a próxima quebra já depender de ação real de uma área.

## Exemplo de lógica

`ROIC`

- margem operacional
- giro do capital investido

`Margem bruta`

- preço
- mix
- volume
- custo unitário

`DSO`

- prazo negociado
- atraso de cobrança
- disputas
- qualidade do faturamento

## Regras de qualidade

- Cada nível precisa ter relação causal clara com o nível acima.
- A árvore deve terminar em drivers que alguém consegue gerenciar.
- Não quebrar demais só porque é possível.
- Se dois drivers se misturam fortemente, nomear a limitação em vez de fingir pureza analítica.

## Como usar na comunicação

A árvore ajuda a:

- organizar a investigação
- priorizar materialidade
- transformar análise em narrativa executiva
- mostrar por que a métrica final mudou

## Limites

- árvore simplifica interdependências
- correlação não garante causalidade
- excesso de nós vira burocracia visual

## Conexões operacionais

- Concept: `concepts/analytical-tools-foundations.md`
- Concept: `concepts/business-model-foundations.md`
- Pattern: `patterns/goal-to-driver-cascade.md`
- Workflow: `tracks/fpa/workflows/gross-margin-bridge.md`

## Fonte

Destilado de Jack Alexander, *Financial Planning, Analysis, and Performance Management*, Cap. 3.
