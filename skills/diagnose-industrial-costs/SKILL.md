---
name: diagnose-industrial-costs
description: Classificar uma pergunta ampla de custos industriais, explicitar evidências e lacunas e encaminhar a investigação para o workflow especializado adequado.
---

# Diagnosticar custos industriais

## Objetivo

Receber uma pergunta ampla sobre custo industrial e devolver primeiro a
natureza provável do problema, a evidência que sustenta a leitura, as lacunas e
o workflow de aprofundamento. O diagnóstico evita escolher estoque, WIP ou
custo padrão antes de entender o sinal observado.

## Interface de triagem

Entrada:

- uma pergunta ampla sobre o custo industrial;
- um ou mais sinais observáveis, cada um com evidência disponível e evidência
  ainda faltante;
- uma decisão canônica de Variance opcional, de
  `skills/explain-variance/SKILL.md`, quando o impacto já tiver sido analisado.

Saída:

1. `primary`: classificação principal entre quantidade, valuation, WIP, padrão,
   absorção, eficiência, perda, obsolescência ou desconhecida;
2. `secondary`: camadas adicionais sustentadas pelos sinais;
3. `supporting_evidence`: evidências que sustentam as classificações;
4. `missing_evidence`: dados necessários para confirmar ou refutar a leitura;
5. `recommended_workflows`: encaminhamento para estoque/valuation, process
   costing/WIP, custo padrão/variâncias ou pedido de evidência;
6. `status` e `confidence`: distinguem classificação, ambiguidade e
   insuficiência de evidência;
7. `warnings`: guardrails específicos do diagnóstico;
8. `variance`: decisão canônica preservada quando fornecida.

Sem uma decisão canônica de Variance, o resultado é triagem. Ele não deve declarar um
fechamento de impacto em estoque, CPV ou margem a partir de texto solto.

## Sequência

### 1. Capturar o sintoma

Registrar a pergunta ampla e os sinais observáveis. Não converter “o custo
subiu” automaticamente em eficiência, valuation ou perda.

### 2. Classificar a camada

Testar os sinais contra as oito camadas do domínio:

| Camada | Sinais típicos |
|---|---|
| Quantidade | contagem física, rollforward, entradas, saídas, cut-off, estoque negativo |
| Valuation | FIFO, custo médio, método de custo, landed cost, camadas, custo unitário |
| WIP | WIP, process costing, unidades equivalentes, percentual de conclusão |
| Padrão | custo padrão, standard costing, padrão desatualizado, variância |
| Absorção | overhead, capacidade ociosa, base de atividade, custos fixos, absorção |
| Eficiência | horas, consumo, setup, downtime, produtividade, yield |
| Perda | scrap, refugo, rework, retrabalho, desperdício, spoilage |
| Obsolescência | aging, sem giro, dano, deterioração, write-down, valor realizável |

O primeiro resultado é primário; uma camada adicional só deve aparecer como
secundária quando houver sinal ou evidência correspondente. Em empate, marcar
ambiguidade em vez de inventar prioridade.

### 3. Separar evidência e lacuna

Para cada classificação, registrar:

- o dado que suporta a leitura;
- o dado que ainda falta;
- o teste que pode confirmar ou refutar a hipótese.

Quantidade que não fecha é uma lacuna anterior ao valuation. Percentual de
conclusão sem evidência operacional é uma lacuna de WIP. Padrão sem data de
revisão é uma lacuna de standard costing.

### 4. Encaminhar ao workflow

- quantidade, valuation e obsolescência →
  `tracks/accounting/workflows/inventory-and-valuation-review.md`;
- WIP →
  `tracks/accounting/workflows/process-costing-and-wip-review.md`;
- padrão, absorção, eficiência e perda →
  `tracks/accounting/workflows/standard-cost-and-industrial-variance-review.md`;
- natureza desconhecida → pedir evidência antes de escolher um workflow.

Quando primária e secundária apontarem para workflows diferentes, preservar a
ordem e devolver ambos. Não esconder a segunda camada para simplificar a
resposta.

### 5. Fechar com Variance canônica

Quando existir uma decisão canônica de Variance, preservá-la como fonte de baseline,
driver, evidência, impacto, recorrência, confiança, reconciliação e ação. O
diagnóstico pode indicar que a camada industrial qualifica a investigação, mas
não deve construir uma segunda decisão canônica nem alterar seus campos.

O fechamento deve tornar visível o impacto canônico em estoque, CPV, margem ou
outro resultado declarado e preservar o owner, timing e ação.

## Cenários de referência

| Cenário | Classificação primária | Encaminhamento |
|---|---|---|
| Quantidade que não fecha | Quantidade | Estoque e valuation; reconciliar antes de concluir valuation |
| Valuation incorreto | Valuation | Estoque e valuation |
| WIP com percentual de conclusão frágil | WIP | Process costing e WIP |
| Padrão desatualizado | Padrão | Custo padrão e variâncias industriais |
| Absorção favorável | Absorção | Custo padrão; testar demanda, capacidade e estoque |
| Waste ou scrap recorrente | Perda | Custo padrão; investigar causa e captura operacional |

## Guardrails

- Não tratar todo aumento de custo como uma única explicação genérica.
- Não concluir valuation enquanto quantidade ou cut-off não fecharem.
- Não tratar variância favorável, absorção favorável ou eficiência aparente
  como melhoria econômica automaticamente.
- Não transformar evidência faltante em causa confirmada.
- Não escolher o workflow mais conhecido antes de classificar o sinal.
- Não substituir os workflows especializados por uma explicação genérica.
- Não alterar a decisão canônica de Variance anexada ao diagnóstico.
- Escrever em PT-BR, com acentuação correta, e declarar a incerteza.
