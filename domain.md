# domain: accounting-ops

Mapa leve de consulta para o agente de accounting, controladoria e FP&A.

Este arquivo não é uma enciclopédia. Use-o para orientar raciocínio e decidir qual trilha carregar.

## Ideia Central

Accounting, controladoria e FP&A transformam dados financeiros e operacionais em entendimento do número, performance e suporte à decisão.

O trabalho não é apenas reportar número. É explicar:

- o que aconteceu
- por que aconteceu
- qual o impacto
- o que deve ser feito ou monitorado

## Conceitos Base

| Conceito        | Definição prática                                                                                                               |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Actual          | Resultado realizado no período.                                                                                                 |
| Budget          | Plano financeiro aprovado para o período.                                                                                       |
| Forecast        | Revisão mais atual da expectativa futura.                                                                                       |
| Variance        | Diferença entre actual, budget ou forecast.                                                                                     |
| Driver          | Causa que explica uma variação: volume, preço, mix, custo, eficiência, câmbio, prazo, estoque, frete.                           |
| Bridge          | Ponte que reconcilia uma variação em blocos explicativos.                                                                       |
| Margem bruta    | Receita menos custos diretos; indica eficiência econômica do produto/projeto.                                                   |
| EBITDA          | Resultado operacional antes de juros, impostos, depreciação e amortização.                                                      |
| OPEX            | Despesas operacionais recorrentes.                                                                                              |
| CAPEX           | Investimentos em ativos e projetos de capital.                                                                                  |
| Working capital | Capital de giro: contas a receber, estoques e contas a pagar.                                                                   |
| MRF             | Monthly Results Forecast ou rotina mensal de revisão/previsão de resultado, dependendo da empresa. Confirmar definição interna. |

## Raciocínio de Variação

Toda variação relevante deve ser analisada em quatro camadas:

1. Tamanho: quanto variou em valor e porcentual.
2. Local: qual linha, unidade, produto, centro de custo ou projeto.
3. Causa: qual driver explica a variação.
4. Ação: o que monitorar, corrigir ou comunicar.

## DRE Gerencial

Leitura básica esperada:

- Receita: volume, preço, mix, descontos, devoluções.
- Custos: matéria-prima, mão de obra, energia, frete, perdas, absorção de custo.
- Margem: pressão de custo, mix, eficiência e precificação.
- Despesas: pessoal, serviços, manutenção, SG&A.
- Resultado: impacto combinado e leitura executiva.

## FP&A Industrial

Em ambiente industrial, FP&A conversa com operação.

Drivers comuns:

- volume produzido e vendido
- preço de venda
- mix de produto
- custo de matéria-prima
- estoque e giro
- frete e logística
- eficiência de fábrica
- perdas, refugos e retrabalho
- investimentos industriais
- capacidade ociosa

### Pacote de custos industriais

Separar a análise em três perguntas:

1. **Inventory Valuation:** qual valor está carregado no estoque e no CPV?
2. **Process Costing:** como materiais e conversão foram acumulados entre WIP e unidades concluídas?
3. **Standard Costing:** por que o custo real divergiu do padrão e a diferença é acionável?

Essa separação evita atribuir ao FIFO um problema de WIP, ou à eficiência um problema de padrão desatualizado.

### Diagnóstico de custos industriais

Quando a pergunta ainda é ampla, classificar primeiro a natureza do problema e
só então escolher o workflow. Uma pergunta pode ter uma camada primária e uma
secundária quando a evidência atravessar mais de uma parte do custo:

| Camada | Pergunta de diagnóstico | Workflow de aprofundamento |
|---|---|---|
| Quantidade | O saldo físico, o rollforward ou o cut-off fecham? | Estoque e valuation |
| Valuation | O método de custo, as camadas e os custos incorporados estão corretos? | Estoque e valuation |
| WIP | O fluxo, as unidades equivalentes e o percentual de conclusão são defensáveis? | Process costing e WIP |
| Padrão | O custo padrão é atual, atingível e comparável ao custo real? | Custo padrão e variâncias industriais |
| Absorção | Volume, capacidade e overhead estão absorvendo o custo de forma econômica? | Custo padrão e variâncias industriais |
| Eficiência | O consumo, as horas ou a produtividade divergem do padrão por causa operacional? | Custo padrão e variâncias industriais |
| Perda | Scrap, refugo, retrabalho ou desperdício explicam o custo e têm recorrência? | Custo padrão e variâncias industriais |
| Obsolescência | Giro, demanda, dano ou valor realizável exigem perda de valor? | Estoque e valuation |

O diagnóstico deve separar evidência que sustenta a classificação de dados que
ainda faltam. Quantidade não reconciliada impede concluir valuation. Absorção
favorável, por si só, não prova melhoria econômica.

## Ponte Auditoria para FP&A

Experiência de auditoria ajuda quando vira raciocínio de negócio:

| Auditoria | FP&A |
|---|---|
| Procedimento analítico | Análise de performance |
| Budget vs. actual | Explicação de variação |
| Revisão de DRE | Leitura gerencial de resultado |
| Teste de controles | Confiabilidade do processo e dado |
| Achado/recomendação | Plano de ação e decisão |
| Evidência | Base de suporte da explicação |

## Perguntas-Chave de FP&A

- O resultado veio melhor ou pior que o esperado?
- Qual linha explica a maior parte da variação?
- A variação é recorrente ou pontual?
- O driver é operacional, comercial, contábil ou de timing?
- O forecast precisa mudar?
- Existe risco para o ano fechado?
- Qual mensagem a gestão precisa ouvir primeiro?
