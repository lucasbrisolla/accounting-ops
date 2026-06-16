# Flash Report Design

Playbook para desenhar ou criticar flash reports curtos, acionáveis e voltados à sobrevivência operacional de curto prazo.

Fonte principal: Steven Bragg, *The New Controller Guidebook*, Cap. 14.

## Quando usar

- report diário ou semanal para liderança
- acompanhamento de caixa, liquidez, backlog, margem de contribuição ou nível de serviço
- ambiente com necessidade de reação rápida

## Princípio central

Flash report existe para foco imediato, não para completar obrigação de reporting.

## O que deve entrar

- poucas métricas críticas
- tendência curta
- exceções relevantes
- comentário curto do controller
- risco imediato
- ação ou checkpoint

## O que normalmente não deve entrar

- inventário completo de KPIs
- detalhe histórico excessivo
- métricas lentas sem capacidade de ação no horizonte do report
- análise longa que pertence ao fechamento mensal

## Seleção de métricas

Perguntar para cada item:

- isso muda alguma decisão de curto prazo?
- o receptor consegue agir?
- a métrica antecipa problema ou apenas descreve atraso?

## Decluttering visual

Antes de circular o flash report, fazer uma passada explícita de redução de ruído:

- remover bordas, fundos, sombras e ornamentos que não ajudam a interpretar
- usar gridlines só quando realmente ajudam leitura e, se usadas, mantê-las leves
- evitar marcadores redundantes quando a linha ou barra já conta a história
- limpar eixos e labels: sem zeros inúteis, sem texto diagonal e sem período escrito de forma que force rotação
- preferir rótulo direto próximo ao dado em vez de depender de legenda distante
- usar uma cor de destaque para exceção, risco ou desvio principal e deixar o restante neutro
- preservar white space em vez de preencher a página por ansiedade
- manter unidades explícitas quando ajudam leitura imediata, como `$`, `%` e separadores de milhar

Regra prática: se a página provoca reação de "tem coisa demais aqui", ela ainda não está pronta.

## Categorias comuns

- caixa e liquidez
- backlog e pedidos
- contribuição ou margem curta
- gargalos operacionais
- nível de serviço
- exceções comerciais ou de supply

## Qualidade editorial

- o report cabe em leitura rápida
- a mensagem principal aparece antes do detalhe
- as exceções estão mais visíveis que o resto
- o leitor entende o gráfico sem caça à legenda
- a página tem ordem visual e espaço para respirar
- o comentário fecha o “e daí?”

## Módulos relacionados

- Process: `_method-wiki/processes/management-reporting-and-report-governance.md`
- Pattern: `_method-wiki/patterns/responsibility-reporting.md`
- Template: `templates/flash-report.md`
