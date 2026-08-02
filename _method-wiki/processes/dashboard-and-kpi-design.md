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

### 3.1 Escolher o visual conforme a pergunta

Antes de abrir a ferramenta, escrever a frase que o visual precisa ajudar a responder. Escolher a forma de apresentação pela pergunta e pelo padrão que precisa ser percebido, não pelo tipo de gráfico disponível no software.

| Pergunta gerencial | Visual inicial mais provável | Critério de uso |
|---|---|---|
| Qual é o número ou status que precisa ser lembrado? | texto destacado, scorecard ou cartão KPI | poucos números, com unidade, período e comparação necessários explícitos |
| Quais itens são maiores, menores ou estão fora da meta? | barras horizontais ou verticais | ordenar categorias e facilitar comparação de magnitude |
| Como o indicador evolui no tempo? | linha | preservar a ordem temporal e mostrar tendência, mudança ou sazonalidade |
| Como um total se divide entre componentes? | barras empilhadas ou 100% empilhadas | usar quando a composição ou a proporção é a pergunta central |
| Quais fatores explicam a passagem de um valor inicial para um final? | waterfall ou bridge | mostrar contribuição de drivers, ganhos, perdas e efeitos de reconciliação |
| Existe relação entre duas medidas? | dispersão | observar associação, concentração e outliers sem sugerir causalidade automaticamente |
| O leitor precisa consultar valores exatos ou várias dimensões? | tabela | priorizar lookup; não forçar um gráfico quando precisão e detalhe são o objetivo |

Essa tabela é um ponto de partida, não um catálogo obrigatório. Para cada visual relevante:

1. formular a pergunta ou mensagem em uma frase
2. escolher duas alternativas plausíveis
3. testar qual permite perceber o padrão com menos explicação
4. manter a opção mais simples que sustenta a decisão
5. descartar visuais que dependem de legenda extensa, interpretação manual ou narrativa do autor para fazer sentido

Quando houver apenas um ou dois números, não transformar a comunicação em gráfico por hábito. Quando houver muitos visuais possíveis, iterar é parte da análise: a primeira representação serve para aprender, mas não precisa ser a versão final do dashboard.

### 3.2 Aplicar padrões recorrentes com critério

Alguns padrões são especialmente úteis para performance e FP&A, desde que a pergunta continue guiando a escolha:

- **Linha para tendência:** usar quando a ordem temporal é essencial. Limitar o número de séries, preservar a escala comparável e evitar transformar categorias sem continuidade em uma falsa trajetória.
- **Linha anotada com forecast:** separar visualmente actual e forecast, marcar o ponto de transição e anotar a mudança material ou a premissa relevante. Não comunicar precisão maior do que a qualidade da projeção permite.
- **Barras 100% empilhadas:** usar para comparar composição relativa ou proporções entre períodos, produtos, unidades ou respostas. Se o total absoluto também importa, mostrar esse total em outro elemento ou escolher barras que preservem a magnitude.
- **Barras empilhadas positivas e negativas:** usar quando a pergunta exige distinguir contribuições acima e abaixo de uma linha de referência, como efeitos favoráveis e desfavoráveis. Manter o zero visível, a ordem das categorias consistente e o sinal sem ambiguidade.
- **Barras empilhadas horizontais:** usar para comparar composição entre várias categorias com rótulos longos. Ordenar as categorias por uma regra explícita e limitar segmentos para que a comparação não dependa de caça à legenda.

Para cada padrão, registrar a justificativa e a limitação principal. Um visual modelar resolve uma situação específica; ele não deve ser copiado para um KPI diferente só porque parece familiar.

### 3.3 Projetar para uso, acessibilidade e aceitação

Tratar o dashboard como um produto de decisão, não apenas como uma página de gráficos:

- **Affordance:** tornar óbvio como ler o painel e o que fazer depois. Títulos orientados à conclusão, filtros com nomes claros, unidades explícitas, rótulos diretos e sinais de drill-down devem reduzir a necessidade de instrução verbal.
- **Acessibilidade:** não depender apenas de cor para comunicar status ou diferença. Combinar cor com texto, posição, forma ou padrão; manter contraste suficiente; usar tamanhos legíveis; e oferecer tabela, rótulo ou descrição quando o visual sozinho não for acessível.
- **Atenção ao detalhe:** revisar alinhamento, espaçamento, casas decimais, separadores, unidades, títulos, cortes de eixo e consistência de períodos. Pequenos erros repetidos reduzem confiança no número.
- **Aceitação:** testar o painel com usuários representativos antes de torná-lo padrão. Explicar o propósito, observar onde a leitura trava, incorporar feedback útil e separar resistência a uma mudança de hábito de um problema real de usabilidade.

Estética só deve entrar depois de função e legibilidade. Um painel pode ser visualmente agradável, mas não deve usar acabamento para esconder métrica mal definida, interação confusa ou ausência de ação.

### 3.4 Fazer o gate integrado antes de publicar

Antes de transformar o painel em padrão de gestão, revisar as seis camadas em sequência:

1. **Contexto:** objetivo, decisão, audiência e mecanismo de consumo estão claros?
2. **Visual:** cada visual responde a uma pergunta e mostra o padrão necessário?
3. **Ruído:** os elementos que não ajudam a interpretação foram removidos?
4. **Foco:** o primeiro olhar e a hierarquia visual apontam para a exceção ou o driver certo?
5. **Uso:** filtros, rótulos, acessibilidade, detalhe e próxima ação são compreensíveis?
6. **Mensagem:** o painel deixa claro o que aconteceu, o que importa e o que deve ser feito?

Registrar a decisão de publicar, revisar ou devolver para análise. Se uma falha crítica persistir em contexto, interpretação, acessibilidade ou ação, o painel não está pronto, mesmo que a ferramenta o considere tecnicamente concluído.

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

### 7. Reduzir carga cognitiva do painel

Além de limitar métricas, reduzir o esforço de leitura do painel:

- eliminar elementos que não agregam sinal informativo suficiente
- evitar bordas de gráfico, fundos pesados e ornamentos padrão por inércia
- usar gridlines e marcadores só quando ajudam de fato; caso contrário, removê-los
- preservar white space e alinhamento consistente entre títulos, visuais e comentários
- evitar rótulos diagonais e simplificar eixos, períodos e números
- preferir rotular séries diretamente quando isso poupa a ida e volta entre legenda e dado
- usar contraste de forma estratégica: destaque para a exceção ou driver prioritário, neutralidade para o restante
- manter unidades explícitas quando isso reduz ambiguidade, como `$`, `%` e separadores de milhar

Painel bom não apenas mostra o driver certo. Ele faz isso com baixo atrito cognitivo.

### 8. Direcionar atenção e construir hierarquia visual

Depois de remover o ruído, definir explicitamente a ordem em que o painel deve ser lido:

1. mensagem ou exceção que exige atenção
2. evidência que sustenta a leitura
3. contexto, comparação ou detalhe de apoio

Usar atributos pré-atentivos de forma intencional:

- tamanho para indicar importância relativa
- cor ou matiz para destacar exceção, driver material ou status relevante
- posição e alinhamento para estabelecer ordem e facilitar comparação
- texto, título e anotação para declarar o que o visual quer que o leitor perceba

Manter a maior parte do painel neutra e reservar a ênfase para o ponto que corresponde à mensagem principal. A mesma codificação deve manter o mesmo significado entre visuais; não usar uma cor para contar histórias diferentes na mesma página.

Aplicar o teste do primeiro olhar:

- afastar-se do painel e voltar a olhar
- registrar onde os olhos pousam primeiro e qual sequência de leitura surge
- comparar essa sequência com a mensagem, a exceção e a ação pretendidas
- ajustar tamanho, cor, posição, título ou anotação se o olhar começar no lugar errado

Se o painel precisa destacar dois assuntos independentes, separar as mensagens em visuais ou páginas distintas. Destacar tudo elimina a hierarquia.

### 9. Definir alertas e exceções

Quando fizer sentido, trocar revisão exaustiva por exception-based reporting.

Alertas úteis podem incluir:

- contas vencidas
- desconto excessivo
- margem abaixo do piso esperado
- mudança brusca de tendência
- atraso contra meta semanal
- desvio de processo ou qualidade

O objetivo é chamar atenção para o que pede investigação ou ação, não gerar ruído.

### 9. Fechar governança da métrica

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
4. Perguntas gerenciais e visuais escolhidos.
5. Padrões visuais usados e suas limitações.
6. Hierarquia de dashboards.
7. Frequência de atualização.
8. Decisões de decluttering e leitura visual.
9. Alertas e limites de exceção.
10. Riscos de comportamento indesejado.
11. Próximas ações de implantação ou revisão.

## Red flags

- dashboard pronto sem ligação com objetivo do negócio
- excesso de métricas no painel principal
- excesso de ruído visual antes mesmo de haver excesso de métrica
- visual escolhido pelo padrão da ferramenta, sem pergunta explícita
- gráfico mais complexo do que o padrão que precisa ser percebido
- actual e forecast sem separação visual ou ponto de transição explícito
- composição 100% empilhada quando a magnitude absoluta é a decisão relevante
- série temporal com categorias demais ou linha conectando eventos sem continuidade
- primeiro olhar direcionado para decoração, total secundário ou dado sem ação
- várias cores, tamanhos ou caixas competindo pela mesma atenção
- filtro, interação ou próxima ação sem affordance clara
- status comunicado somente por cor ou com contraste insuficiente
- inconsistência de alinhamento, unidade, arredondamento ou período
- design rejeitado sem teste distinguir problema de usabilidade de resistência à mudança
- foco apenas em indicadores atrasados
- métrica sem definição formal
- dado sem responsável claro
- indicador que incentiva comportamento ruim
- dashboard que não muda decisão, prioridade ou ação
- visual bonito sem leitura de driver

## Guardrails

- Não confundir dashboard com relatório mensal.
- Não medir tudo que está disponível.
- Não aceitar defaults visuais da ferramenta sem testar se ajudam ou só poluem.
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
