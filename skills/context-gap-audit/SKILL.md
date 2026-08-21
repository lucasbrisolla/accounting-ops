---
name: context-gap-audit
description: Auditar o que o corpus do accounting-ops sustenta, o que está documentado, o que contradiz outra fonte e o que ainda exige contexto. Usar quando o usuário pedir lacunas, contradições, oportunidades, próximos passos ou impacto potencial com base em documentos.
---

# Auditar contexto e oportunidades

Status: `rascunho`

## Objetivo

Auditar o que o corpus já sustenta, o que apenas descreve, o que contradiz outra fonte e o que ainda exige contexto antes de virar uma oportunidade ou decisão.

Esta skill propõe oportunidades fundamentadas no corpus. Ela encontra diferenças entre o que o projeto afirma, o que já consegue fazer e o que ainda não consegue responder, sem transformar hipóteses documentais em recomendações aprovadas.

## Usar quando

- o usuário pedir ideias, próximos passos, lacunas, contradições ou preocupações de aplicabilidade com base no corpus
- for necessário estimar impacto potencial sem transformar hipótese em recomendação aprovada

## Não usar quando

- a solicitação for brainstorming genérico sem corpus suficiente
- o objetivo for desenhar uma solução antes de estabelecer a lacuna

## Pré-condição

Exigir um corpus suficiente para a pergunta. O corpus pode ser:

- a base documental do projeto, quando o usuário pedir uma auditoria do produto;
- um conjunto de arquivos ou pastas indicado pelo usuário;
- um recorte de método, workflow, playbook e contexto empresarial.

Se não houver acesso a documentos suficientes, declarar a limitação e parar. Não preencher a ausência com conhecimento externo ou sugestões genéricas.

Usar a conversa apenas para entender a pergunta. Usar os documentos como evidência. Só usar fontes externas quando o usuário pedir; nesse caso, separar claramente o que veio de fora.

## Pergunta de auditoria

Antes de procurar oportunidades, formular a pergunta operacional:

- que decisão, capacidade ou próximo passo o usuário quer avaliar?
- qual produto, trilha, empresa ou contexto está no escopo?
- o que seria uma descoberta útil e o que seria apenas uma confirmação?

Não auditar a base inteira por padrão. Começar pelo menor conjunto de documentos que possa responder à pergunta e registrar esse escopo na saída.

## Procedimento

### 1. Mapear o corpus

Registrar os arquivos consultados, a função de cada um e os limites do recorte.

Priorizar, quando existirem:

1. `domain.md` e `README.md` para escopo e linguagem;
2. `_method-wiki/` para conceitos, processos, padrões, checklists e heurísticas;
3. `tracks/` para workflows e playbooks;
4. `context/` para fatos situados, empresas, fontes e evidências;
5. `skills/` e `templates/` para capacidades e contratos já operacionalizados.

Não tratar a existência de um arquivo como prova de que o conteúdo está validado ou em uso.

### 2. Extrair o estado atual

Para cada tema relevante, identificar:

- o que o corpus afirma;
- o que já está definido;
- o que já está operacionalizado em workflow, skill, script ou template;
- o que possui evidência ou uso real;
- o que depende de hipótese, decisão ou contexto adicional;
- o que contradiz outra fonte.

### 3. Eliminar falsos achados

Antes de chamar algo de descoberta:

- procurar termos equivalentes e nomes anteriores;
- verificar se a ideia já aparece em outro módulo;
- verificar se existe uma decisão, workflow ou script que já a resolve;
- distinguir ausência de arquivo de ausência de capacidade;
- tratar conteúdo parcialmente definido como parcial, não como novo.

Se a ideia já estiver resolvida no corpus, classificá-la como `CONFIRMATION`. Nunca reapresentá-la como descoberta nova.

### 4. Classificar o estado da ideia

Usar uma classificação de estado e uma classificação de saída.

#### Estado da ideia

| Estado | Significado |
|---|---|
| `0 — resolvida` | O corpus define o conceito, o uso e o limite com evidência suficiente. |
| `1 — documentada, não operacionalizada` | Existe método, playbook ou especificação, mas ainda não há rotina, skill, script, output ou uso demonstrado. |
| `2 — parcialmente resolvida` | Há peças relevantes, mas falta uma relação, definição, etapa, responsável ou critério de conclusão. |
| `3 — lacuna de contexto` | O potencial pode ser real, mas falta uma informação específica para avaliar aplicabilidade. |
| `4 — hipótese de alto potencial` | O corpus sustenta uma oportunidade plausível, mas a aplicabilidade ainda precisa de teste. |
| `5 — especulativa` | A ideia depende principalmente de imaginação, analogia ou conhecimento externo não confirmado. |

#### Saída da auditoria

- `CONFIRMATION`: já existe no corpus; não é descoberta.
- `OPERATIONALIZATION GAP`: está documentada, mas ainda não virou capacidade demonstrada.
- `CONTEXT GAP`: falta uma informação específica para julgar a aplicabilidade.
- `CONTRADICTION`: fontes relevantes afirmam coisas incompatíveis.
- `OPPORTUNITY`: há uma oportunidade sustentada o bastante para propor investigação ou implementação.
- `SPECULATIVE`: não há base suficiente; descartar ou manter fora do backlog.

Uma ideia pode ser `OPPORTUNITY` e ainda estar no estado `3` ou `4`. Potencial não é confirmação de aplicabilidade.

### 5. Nomear o tipo exato de lacuna

Não escrever apenas “faltam dados”. Escolher o tipo mais específico:

- `informação`: falta um fato ou fonte;
- `definição`: falta definir um termo, unidade, granularidade ou escopo;
- `relação`: falta explicar a ligação causal entre drivers, métricas, processos ou resultados;
- `decisão`: existem opções, mas não há escolha ou critério de arbitragem;
- `processo`: existe intenção, mas faltam passos, owner, frequência ou critério de saída;
- `evidência`: existe uma afirmação, mas falta fonte, período, reconciliação ou teste;
- `operacionalização`: existe método ou desenho, mas não existe capacidade usada e verificada.

### 6. Estimar impacto potencial sem criar precisão falsa

Para cada item remanescente, perguntar:

- que decisão ou capacidade ele pode melhorar?
- qual artefato, workflow ou processo seria afetado?
- que evidência no corpus sustenta o potencial?
- qual informação específica falta?
- qual teste pequeno confirmaria ou enfraqueceria a hipótese?
- qual seria o critério para parar, adiar ou descartar?

#### Índice de impacto potencial

Para cada `OPERATIONALIZATION GAP`, `CONTEXT GAP` ou `OPPORTUNITY` que for proposto como ideia, calcular um índice de `1–100%`. O índice representa o impacto caso a ideia seja aplicável; não representa probabilidade de sucesso, confiança ou retorno financeiro realizado.

Pontuar os componentes antes de somá-los:

| Componente | Peso máximo | Pergunta orientadora |
|---|---:|---|
| Materialidade e alavancagem da decisão | 30 | A ideia muda uma decisão financeira, operacional ou de gestão relevante? |
| Alcance | 20 | Quantos processos, áreas, empresas, produtos ou contextos podem ser afetados? |
| Recorrência e reutilização | 20 | O benefício se repete ou fica restrito a um caso isolado? |
| Desbloqueio de outras capacidades | 15 | A ideia habilita outras iniciativas, análises ou decisões? |
| Redução de risco, retrabalho ou tempo | 15 | Ela reduz exposição, esforço manual ou demora de forma relevante? |

Classificar o total assim:

| Faixa | Interpretação |
|---:|---|
| 1–20% | baixo |
| 21–40% | limitado |
| 41–60% | relevante |
| 61–80% | alto |
| 81–100% | muito alto |

Registrar também a `Confiança da estimativa`:

- `alta`: o corpus traz evidência direta, uso, métrica ou decisão afetada;
- `média`: o corpus mostra uma relação plausível, mas faltam dados, owners ou teste;
- `baixa`: o score depende principalmente de uma inferência estrutural ou hipótese.

Separar sempre `Impacto potencial`, `Confiança da estimativa` e `Aplicabilidade atual`. Uma ideia pode ter impacto potencial de `85%`, confiança baixa e aplicabilidade não confirmada. Não usar o score sozinho para ordenar implementação. Para `SPECULATIVE`, registrar `não estimável` em vez de inventar uma pontuação.

## Formato de saída

Começar sempre com o escopo da auditoria:

```text
Corpus consultado:
Pergunta avaliada:
Limitações do recorte:
```

Depois, separar os achados por saída. Para cada item, usar:

```text
## [SAÍDA] Nome curto

Estado:
Tipo de lacuna:
Onde aparece no corpus:

O que já está resolvido:
O que ainda não está resolvido:
Informação ou decisão faltante:
Impacto potencial estimado:
Base do score:
Confiança da estimativa:
Aplicabilidade atual:
Por que isso importa:
O que confirmaria a aplicabilidade:
Próxima investigação mínima:
Critério para parar, adiar ou avançar:
```

Encerrar com:

- confirmações que não devem voltar como ideias novas;
- contradições que exigem resolução;
- lacunas de operacionalização;
- lacunas de contexto;
- oportunidades sustentadas;
- itens especulativos descartados ou mantidos fora do escopo.

## Guardrails

- Não gerar ideias a partir de conhecimento externo quando a tarefa pedir leitura do corpus.
- Não chamar de novo algo já documentado, mesmo que apareça com outra formulação.
- Não confundir arquitetura desenhada com capacidade funcionando.
- Não confundir ausência de evidência com evidência de ausência.
- Não transformar uma lacuna de definição em uma solução técnica.
- Não recomendar implementação antes de nomear a lacuna e o teste de aplicabilidade.
- Não apresentar o impacto potencial como probabilidade de sucesso, retorno garantido ou certeza de aplicabilidade.
- Não dar score sem explicar os componentes que o formam.
- Não permitir que um score alto esconda confiança baixa ou falta de contexto.
- Não esconder contradições por escolher silenciosamente uma fonte.
- Não transformar uma prática específica de uma empresa em regra geral sem promoção metodológica.
- Separar fato, interpretação, hipótese, recomendação e decisão.

## Relação com outras capacidades

Use esta skill antes de uma skill de desenho de produto ou decisão quando a pergunta ainda for “o que está faltando?” ou “o que merece investigação?”.

Depois de uma saída `OPERATIONALIZATION GAP`, `CONTEXT GAP` ou `OPPORTUNITY`, uma skill de desenho pode avaliar se vale criar um produto, workflow, skill ou script.
