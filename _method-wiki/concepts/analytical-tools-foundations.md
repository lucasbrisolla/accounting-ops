# Analytical Tools Foundations

## Ideia central

Ferramenta analítica boa não é a mais sofisticada. É a que ajuda a separar sinal de ruído, priorizar materialidade e transformar base bruta em decisão melhor.

Este conceito existe para dar linguagem comum ao `accounting-ops` quando a análise pede ordenação, recorte, dispersão, sensibilidade, cenário ou decomposição probabilística.

## Quando usar

- priorização de clientes, produtos, custos ou desvios
- leitura de distribuição e concentração
- revisão de forecast e cenários
- análise de drivers com alta incerteza
- diagnóstico de bases grandes demais para leitura linha a linha

## Ferramentas centrais

### Ordenação por materialidade

Comece pelo que mais move resultado, caixa, risco ou decisão.

Antes de sofisticar a análise, ordenar:

- maiores linhas por valor
- maiores desvios absolutos e percentuais
- itens com maior recorrência
- itens com maior assimetria de risco

Se a ordenação já resolve a pergunta, não complicar.

### Quartile analysis

Útil para separar grupos por comportamento:

- clientes com maior margem
- SKUs com pior giro
- centros de custo com maior volatilidade
- unidades com melhor conversão de caixa

Ajuda a evitar média que esconde extremos.

### Pareto

Serve para responder onde está a maior parte do efeito.

Perguntas típicas:

- quais clientes explicam a maior parte da inadimplência?
- quais itens concentram write-offs?
- quais causas explicam a maior parte da queda de margem?

Se poucas causas explicam a maior parte do problema, a ação deve começar nelas.

### Média vs. mediana

`Média` é útil quando a distribuição é relativamente equilibrada.

`Mediana` é melhor quando há outliers, cauda longa ou concentração.

Exemplo prático:

- prazo médio pode parecer saudável
- mediana e quartis podem mostrar que uma minoria muito atrasada está distorcendo a leitura

### Desvio-padrão

Use como sinal de dispersão, não como fim em si.

Ajuda a testar:

- estabilidade de demanda
- previsibilidade de custo
- volatilidade de margem
- confiabilidade de lead time

Dispersão alta pede mais cautela em forecast, meta e capacidade.

### Sensitivity analysis

Útil quando poucas premissas mudam muito o resultado.

Testar:

- preço
- volume
- mix
- câmbio
- matéria-prima
- prazo médio de recebimento

Pergunta central: qual variável, se errar pouco, muda muito lucro, caixa ou retorno?

### Scenario analysis

Serve para recalcular um conjunto coerente de premissas.

Usar quando o contexto muda junto:

- mercado mais fraco
- pressão competitiva
- atraso de projeto
- queda de utilização de capacidade
- melhora operacional real

Cenário não é trocar uma célula isolada. É recontar a história econômica do caso.

### Probability and expected value

Faz sentido quando existem eventos discretos com probabilidades diferentes.

Exemplos:

- perda ou ganho de contrato relevante
- chance de atraso em CAPEX
- downside regulatório ou tributário

Nem toda decisão precisa de valor esperado formal, mas a lógica ajuda a sair do binário.

### Decision trees, performance trees e predictive models

`Decision tree` ajuda quando há caminhos alternativos de ação.

`Performance tree` ajuda a decompor um indicador em drivers subordinados.

`Predictive model` só vale quando existe base, padrão e uso gerencial claros. Não usar para decorar análise fraca.

## Regras práticas de uso

- Escolha a ferramenta pela pergunta, não pelo prestígio técnico.
- Prefira a menor ferramenta que responda bem.
- Se a análise não muda decisão, ela está sofisticada demais.
- Sempre ligar a ferramenta a driver, risco ou ação.

## Sinais de mau uso

- média usada para esconder distribuição torta
- cenário tratado como sensibilidade simples
- probabilidade arbitrária sem hipótese clara
- modelo preditivo sem dados confiáveis
- análise estatística sem implicação gerencial

## Módulos relacionados

- Concept: `concepts/business-model-foundations.md`
- Concept: `concepts/operating-leverage-and-break-even.md`
- Pattern: `patterns/performance-tree.md`
- Pattern: `patterns/variance-analysis.md`
- Process: `processes/forecasting-and-business-outlook.md`
- Workflow: `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md`

## Fonte

Destilado de Jack Alexander, *Financial Planning, Analysis, and Performance Management*, Cap. 3.
