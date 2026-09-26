---
title: Desenvolvimento e revisão de modelos analíticos
date: 2026-09-13
tags:
  - accounting-ops
  - fpa
  - modelagem-financeira
  - forecast
aliases:
  - Revisão de modelo financeiro
  - Predictive and Analytical Models
status: ativo
---

# Desenvolvimento e Revisão de Modelos Analíticos

Workflow para construir ou revisar modelos que representem a dinâmica de um
negócio, projeto, transação ou decisão e convertam premissas em uma saída útil
para gestão.

Fonte principal: Jack Alexander, *Financial Planning, Analysis, and Performance Management*, Cap. 4.

## Pergunta central

O modelo responde à pergunta certa, com arquitetura compreensível, premissas
controláveis, ownership operacional, validação suficiente e uma saída que a
gestão consegue usar?

Neste workflow, um modelo preditivo ou analítico é uma representação matemática
de relações, eventos e premissas para testar resultados. O termo não pressupõe
machine learning nem justifica complexidade técnica sem utilidade gerencial.

## Quando usar

- budget, operating plan, forecast ou business outlook;
- projeção de receita, margem, custo, caixa ou liquidez;
- decisão de CAPEX, novo produto, aquisição ou outsourcing;
- análise de pricing, mix, capacidade, working capital ou valor;
- teste de cenários estratégicos ou alternativas de decisão;
- revisão de planilha que virou dependência crítica da operação;
- modelo duplicado, pouco documentado, difícil de atualizar ou sem owner claro.

## Princípio central

Um modelo não termina na fórmula. Seu valor depende de uma cadeia completa:

1. objetivo e cliente claros;
2. arquitetura que separa entradas, processamento e saída;
3. premissas e drivers explícitos;
4. dados reais suficientes para validar o comportamento;
5. ownership das premissas e adesão das áreas;
6. flexibilidade para sensibilidade e cenários;
7. revisão de exatidão e razoabilidade;
8. resumo de apresentação ligado ao modelo;
9. armazenamento e reuso com governança.

## Contrato mínimo do modelo

| Elemento | Pergunta que precisa ser respondida | Evidência esperada |
|---|---|---|
| Objetivo | Que decisão, transação ou dinâmica o modelo precisa esclarecer? | objetivo escrito e critério de uso |
| Cliente | Quem usará a saída e quem decidirá a partir dela? | audiência e decisão identificadas |
| Horizonte e frequência | Por quanto tempo o modelo olha e com que frequência será atualizado? | calendário e granularidade coerentes |
| Arquitetura | Como inputs, cálculos e outputs fluem? | mapa ou primeira aba de arquitetura |
| Premissas e drivers | Quais variáveis movem o resultado e quem as sustenta? | lista de premissas com owner |
| Actual e histórico | O modelo reproduz o realizado e oferece baseline comparável? | teste contra dados reais |
| Flexibilidade | Uma mudança controlada em uma premissa percorre o modelo inteiro? | sensibilidade e cenários executáveis |
| Validação | Quem revisou a lógica e os resultados? | revisão independente e testes documentados |
| Comunicação | A saída mostra o que importa sem exigir a planilha inteira? | resumo com mensagem e implicação |
| Governança | O modelo pode ser encontrado, compreendido, atualizado e acessado com segurança? | portfólio, instruções, owner e acesso |

Se um elemento não for relevante para o caso, registrar a razão. Ausência
explicada é diferente de lacuna escondida.

## Sequência de trabalho

### 1. Definir objetivo, cliente e uso

Antes de abrir uma planilha, registrar:

- qual pergunta o modelo precisa responder;
- qual saída permitirá decidir, comparar ou monitorar alternativas;
- quem é o cliente principal e quem fornece as premissas;
- qual é o horizonte e o nível de detalhe adequado;
- com que frequência o modelo será atualizado e por quem;
- qual decisão ou ação deverá ocorrer depois da análise.

Validar esse escopo com o cliente. Alguns minutos de alinhamento podem evitar
um modelo tecnicamente sofisticado que não responde à pergunta real.

### 2. Desenhar a arquitetura

Mapear o fluxo antes de desenvolver os cálculos:

```text
Fontes e actuals → Inputs e premissas → Processamento → Outputs → Resumo para decisão
```

Definir, no mínimo:

- fonte e periodicidade de cada input;
- área ou aba de premissas;
- cálculos e relações principais;
- saídas financeiras e operacionais;
- resumo ou apresentação final;
- pontos de validação e reconciliação.

Em modelos complexos, uma primeira aba de arquitetura reduz o tempo gasto para
entender o fluxo e facilita a revisão por outra pessoa.

### 3. Separar inputs, processamento e outputs

Tornar visível o que pode ser alterado pelo usuário e o que deve ser preservado:

- concentrar inputs e premissas em área identificável;
- diferenciar valores informados, cálculos e outputs;
- evitar o mesmo input digitado em vários pontos;
- sinalizar células de alteração permitida;
- proteger fórmulas contra sobrescrita acidental;
- deixar limitações e dependências próximas da premissa.

Proteção de fórmula não deve criar lógica oculta. O usuário precisa entender o
que pode mudar, o que será recalculado e como investigar uma saída inesperada.

### 4. Identificar drivers e premissas críticas

Listar as variáveis que mais movem o resultado e priorizar sua revisão:

- preço, desconto, volume, mix e ciclo de vida;
- custo unitário, produtividade, inflação e câmbio;
- capacidade, headcount, investimentos e cronograma;
- recebíveis, estoque, payables, caixa e financiamento;
- entrada de produto, perda de cliente, concorrência ou mudança de canal.

Para cada premissa material, registrar:

- definição e unidade;
- fonte ou método de estimativa;
- owner operacional;
- justificativa para o valor-base;
- indicador que permitirá revisar a premissa;
- sensibilidade ou cenário que a desafia.

Não dar o mesmo nível de detalhe a todas as linhas. O esforço deve acompanhar
materialidade, volatilidade e sensibilidade.

### 5. Incorporar actuals e histórico

Usar dados realizados para dois testes diferentes:

1. verificar se o modelo reproduz a realidade observada;
2. estabelecer uma base de comparação para a projeção.

Escolher o histórico conforme ciclo do negócio, disponibilidade, mudança
estrutural e frequência do modelo. Mais períodos não compensam dados
incomparáveis ou uma definição de negócio que mudou.

Se o modelo não reproduzir o realizado, classificar a diferença antes de usar a
projeção: erro de dado, definição, fórmula, timing, evento não recorrente ou
mudança real do driver.

### 6. Obter ownership e buy-in

Finance pode facilitar a construção, mas não deve ser o único dono das
premissas operacionais. Confirmar com as áreas responsáveis:

- quem fornece cada input;
- quem responde por alcançar o resultado projetado;
- quais premissas foram aceitas e quais permanecem como hipótese;
- que restrições operacionais não aparecem na planilha;
- como mudanças de contexto serão comunicadas.

Quando Finance inventa sozinho as premissas, o modelo pode virar um produto de
Finance e a área responsável deixa de se reconhecer no resultado.

### 7. Construir flexibilidade, sensibilidade e cenários

O modelo deve permitir alterar uma premissa em um ponto controlado e refletir a
mudança nos resultados relacionados. Evitar múltiplas digitações manuais para a
mesma hipótese.

Separar:

- **sensibilidade:** altera uma variável, ou um pequeno conjunto, para medir a
  exposição do resultado;
- **cenário:** altera um conjunto coerente de condições para representar um
  futuro ou alternativa de decisão.

Para cada teste, mostrar:

- premissas alteradas;
- linhas afetadas;
- impacto em resultado, margem, caixa, capital ou retorno;
- condição que faria o teste ser relevante;
- indicador para monitorar a hipótese.

O caso-base é uma referência de trabalho, não uma certeza. Cenários devem
ajudar a entender a dinâmica e a preparar decisões, não produzir falsa
precisão.

### 8. Revisar exatidão e razoabilidade

Aplicar uma revisão independente quando a materialidade ou o risco justificar.
O revisor deve:

- conferir inputs críticos contra a fonte;
- rastrear os principais números até o resumo;
- testar sinais, unidades, períodos e relações;
- comparar outputs com actuals, tendência e ordem de grandeza esperada;
- verificar se a lógica funciona em upside, downside e valores extremos;
- avaliar o resultado pela perspectiva do cliente;
- registrar erros, hipóteses não testadas e perguntas abertas.

Uma revisão de modelo não deve verificar apenas se as fórmulas calculam. Deve
testar se a saída faz sentido para a decisão.

### 9. Criar o resumo de apresentação

Integrar ao modelo uma saída curta que acompanhe suas alterações. O resumo deve
mostrar, conforme o caso:

- objetivo e mensagem principal;
- premissas e drivers críticos;
- resultado-base e alternativas;
- gráfico ou tabela que mostre magnitude, tendência ou composição;
- sensibilidade e cenário relevante;
- implicação para decisão, risco, caixa, capital ou operação;
- ação recomendada e próximo checkpoint.

Planilhas detalhadas ficam como suporte. Se a narrativa manual mudar quando o
modelo for recalculado, atualizar a comunicação antes de circular o material.

### 10. Catalogar e governar o modelo

Registrar o modelo em um portfólio compartilhado com, no mínimo:

- área temática e nome;
- objetivo e cliente;
- descrição da saída;
- owner e curador;
- data da última revisão e do último uso;
- fontes, dependências e instruções;
- nível de sensibilidade e controle de acesso;
- modelos relacionados ou versões substituídas.

O portfólio reduz duplicação, facilita reuso e permite localizar boas práticas.
Padronizar modelos relacionados ajuda o cliente a revisar materiais com lógica e
aparência consistentes, sem impedir adaptação ao caso.

## Gate de qualidade antes de usar

- [ ] O objetivo e a decisão estão escritos.
- [ ] O cliente, o usuário e a frequência de uso estão claros.
- [ ] A arquitetura separa inputs, processamento e outputs.
- [ ] Premissas e drivers críticos estão identificados fora da lógica oculta.
- [ ] Os inputs têm fonte, unidade, período e owner.
- [ ] Actuals ou histórico foram usados para validar o comportamento quando aplicável.
- [ ] Fórmulas estão protegidas ou sujeitas a controle equivalente.
- [ ] O modelo permite sensibilidade e cenários relevantes.
- [ ] Houve revisão de inputs, fluxo, exatidão e razoabilidade proporcional ao risco.
- [ ] O resumo de saída explica resultado, implicação e ação.
- [ ] O modelo está documentado, catalogado e acessível às pessoas certas.

## Sinais de modelo fraco

- o modelo começa com uma planilha antes de definir objetivo e cliente;
- inputs críticos estão espalhados ou misturados com fórmulas;
- a mesma premissa precisa ser digitada em várias abas;
- o modelo produz um número, mas não mostra a dinâmica que o gerou;
- o histórico não reconcilia e a diferença é ignorada;
- Finance é tratado como dono de premissas que pertencem à operação;
- uma mudança simples exige várias alterações manuais;
- só existe cenário-base, mesmo quando a incerteza é material;
- a saída exige abrir a planilha inteira para entender a mensagem;
- ninguém sabe qual é a versão vigente ou como atualizar o arquivo;
- um modelo sensível está disponível sem controle de acesso.

## Guardrails

- Não transformar um modelo em forecast automático: premissas e resposta do negócio continuam sujeitas a julgamento.
- Não usar complexidade, macros ou técnica estatística como substituto de objetivo, dados e decisão.
- Não tratar o histórico como prova de que o futuro seguirá igual.
- Não importar um template de outro negócio sem revisar drivers, owners, definições e fluxo operacional.
- Não centralizar a lógica a ponto de tornar o modelo incompreensível para quem fornece os inputs.
- Não confundir proteção de fórmula com controle de qualidade; ambos precisam ser revisados.
- Não circular o número projetado sem o resumo, os riscos e a implicação gerencial.
- Não armazenar modelos sensíveis em repositório sem governança de acesso.

## Saída recomendada

```markdown
## Objetivo e Decisão

[pergunta, cliente, horizonte e decisão apoiada]

## Arquitetura e Ownership

[inputs, processamento, outputs e responsáveis pelas premissas]

## Premissas e Drivers Críticos

| Premissa | Fonte | Owner | Base | Teste |
|---|---|---|---:|---|

## Resultado e Cenários

| Cenário | Premissas alteradas | Resultado | Implicação |
|---|---|---:|---|

## Validação

[actuals, testes de fluxo, revisão independente e limitações]

## Recomendação e Próximo Checkpoint

[ação, indicador e data de revisão]
```

## Módulos relacionados

- Checklist: `_method-wiki/checklists/financial-projection-quality-checklist.md`
- Processo: `_method-wiki/processes/forecasting-and-business-outlook.md`
- Workflow: `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`
- Workflow: `tracks/fpa/workflows/integrated-budget-and-driver-review.md`
- Playbook: `tracks/fpa/playbooks/long-term-projection-and-strategic-scenario-review.md`
- Playbook: `tracks/fpa/playbooks/financial-information-communication.md`
- Conceito: `_method-wiki/concepts/analytical-tools-foundations.md`
