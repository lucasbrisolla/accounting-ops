# Pattern: Responsibility Reporting

## Papel

Estrutura para ligar linha reportada, nível de agregação e owner de forma coerente.

## Princípio central

Report sem dono vira observação passiva.

Responsibility reporting existe para garantir que cada número relevante chegue ao nível certo de detalhe para quem pode agir sobre ele.

## Estrutura base

1. Definir a decisão ou ação esperada do receptor.
2. Selecionar apenas linhas com owner plausível.
3. Ajustar a granularidade ao nível hierárquico.
4. Explicitar exceções, não despejar detalhe irrelevante.

## Níveis típicos

| Nível | O que precisa receber |
|---|---|
| Executivo | poucos indicadores, tendência, exceções e implicação |
| Gerencial | drivers principais, desvios materiais, causas prováveis e ação |
| Operacional | detalhe suficiente para corrigir processo, cliente, SKU, projeto ou rotina |

## Perguntas de qualidade

- quem consegue agir sobre esta linha?
- esse receptor precisa do total, da quebra ou da exceção?
- estamos mandando detalhe demais para cima?
- estamos escondendo responsabilidade em agregação excessiva?

## Riscos clássicos

- dado demais para executivo
- visão agregada demais para gestor operacional
- linha sem owner real
- custo compartilhado tratado como responsabilidade individual

## Guardrails

- Não inventar ownership onde o processo real não existe.
- Não usar agregação para esconder problema.
- Não dar granularidade falsa só para parecer sofisticado.

## Conexões operacionais

- Process: `processes/management-reporting-and-report-governance.md`
- Playbook: `tracks/fpa/playbooks/flash-report-design.md`
- Playbook: `tracks/fpa/playbooks/margin-reporting-without-bad-allocations.md`

## Fonte

Destilado de Steven Bragg, *The New Controller Guidebook*, Cap. 14.
