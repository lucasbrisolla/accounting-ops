# Processo: Dashboards e KPIs

## Papel

Hub metodológico para desenhar dashboards e KPIs que ajudem a monitorar performance, antecipar problemas e orientar decisão gerencial.

Este processo existe para evitar dashboards decorativos, métricas soltas e painéis que apenas repetem dados históricos sem ligação com drivers, objetivos ou ações.

## Quando usar

Use este processo quando a pergunta envolver:

- desenho de dashboard gerencial
- escolha de KPIs
- revisão de indicadores de performance
- acompanhamento de orçamento, forecast ou plano operacional
- definição de alertas e exception-based reporting
- leitura de leading indicators e lagging indicators

## Princípio central

Dashboard bom funciona como painel de controle, não como relatório posterior.

Ele deve mostrar o que importa para conduzir o negócio enquanto ainda há tempo de agir.

## Sequência recomendada

### 1. Definir o objetivo gerencial

Antes de escolher métricas, responder:

- qual decisão este dashboard precisa apoiar?
- qual objetivo de negócio está em jogo?
- qual processo, unidade, projeto ou área será monitorado?
- qual problema o gestor precisa enxergar mais cedo?

Não começar por gráfico, ferramenta ou template pronto.

### 2. Mapear drivers e relações de causa e efeito

Separar:

- resultado final
- drivers operacionais
- fatores externos relevantes
- premissas críticas
- sinais antecipados de risco ou oportunidade

Exemplo: para reduzir DSO, não basta medir DSO. É preciso acompanhar drivers como linearidade de receita, qualidade de cobrança, vencidos, causas de atraso e ritmo de recebimento.

### 3. Selecionar medidas com critério

Para cada métrica candidata, testar:

- relevância para o objetivo
- objetividade e definição clara
- tempestividade da informação
- integridade da base de dados
- capacidade de antecipar problema ou ação
- risco de comportamento indesejado
- necessidade de métrica de equilíbrio

Métrica que não muda decisão, prioridade ou ação deve sair do dashboard principal.

### 4. Balancear indicadores

Evitar dashboards dominados por um único tipo de indicador.

Buscar equilíbrio entre:

- leading e lagging indicators
- financeiro e operacional
- cliente e processo interno
- curto prazo e saúde de longo prazo
- produtividade e qualidade
- eficiência e nível de serviço

Exemplo: medir giro de estoque sem medir entrega no prazo pode incentivar redução de estoque às custas de atendimento ao cliente.

### 5. Definir nível e frequência

Escolher o tipo de dashboard conforme o uso:

- corporativo ou divisão
- diário ou semanal
- função ou departamento
- processo
- projeto
- melhoria de performance
- gestor individual

Definir frequência por natureza da métrica:

- diária ou contínua para processos sensíveis e operacionais
- semanal para progresso contra meta de curto prazo
- mensal para performance financeira e gerencial
- trimestral ou anual para métricas de capital e retorno

A frequência errada enfraquece até uma boa métrica.

### 6. Limitar o dashboard principal

O dashboard principal deve concentrar atenção.

Como regra prática:

- usar poucas métricas realmente centrais
- manter algo próximo de 8 a 12 medidas no nível corporativo
- usar dashboards de suporte para detalhe por processo, função ou projeto
- evitar transformar o painel principal em inventário de dados

Se tudo está no dashboard, nada está em foco.

### 7. Definir alertas e exceções

Quando fizer sentido, trocar revisão exaustiva por exception-based reporting.

Alertas úteis podem incluir:

- contas vencidas
- desconto excessivo
- margem abaixo do piso esperado
- mudança brusca de tendência
- atraso contra meta semanal
- desvio de processo ou qualidade

O objetivo é chamar atenção para o que pede investigação ou ação, não gerar ruído.

### 8. Fechar governança da métrica

Para cada KPI relevante, documentar:

- definição
- fórmula
- fonte de dados
- responsável
- frequência
- meta ou limite
- interpretação esperada
- possíveis efeitos colaterais
- métrica de equilíbrio, quando aplicável

Indicador sem definição estável vira disputa de interpretação.

## Estrutura de saída sugerida

1. Objetivo gerencial do dashboard.
2. Drivers e relações de causa e efeito.
3. KPIs selecionados e descartados.
4. Hierarquia de dashboards.
5. Frequência de atualização.
6. Alertas e limites de exceção.
7. Riscos de comportamento indesejado.
8. Próximas ações de implantação ou revisão.

## Red flags

- dashboard pronto sem ligação com objetivo do negócio
- excesso de métricas no painel principal
- foco apenas em indicadores atrasados
- métrica sem definição formal
- dado sem responsável claro
- indicador que incentiva comportamento ruim
- dashboard que não muda decisão, prioridade ou ação
- visual bonito sem leitura de driver

## Guardrails

- Não confundir dashboard com relatório mensal.
- Não medir tudo que está disponível.
- Não usar KPI sem testar efeito colateral.
- Não separar visualização de qualidade do dado.
- Não substituir julgamento gerencial por métrica; usar métrica para informar e desafiar julgamento.

## Módulos relacionados

- Conceito: `concepts/budget-vs-forecast-vs-operating-plan.md`
- Conceito: `concepts/working-capital-foundations.md`
- Heurística: `heuristics/margin-erosion-signals.md`
- Checklist: `checklists/forecast-review-checklist.md`
- Pattern: `patterns/variance-analysis.md`
- Workflow: `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`
- Workflow: `tracks/fpa/workflows/integrated-budget-and-driver-review.md`
- Workflow: `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md`

## Critério de qualidade

Um bom dashboard não prova que a empresa está sendo gerida. Ele mostra se os drivers certos estão sendo acompanhados, se os sinais aparecem cedo o bastante e se a informação ajuda alguém a decidir melhor.

## Fonte

Destilado de Jack Alexander, *Financial Planning, Analysis, and Performance Management*, Cap. 8.
