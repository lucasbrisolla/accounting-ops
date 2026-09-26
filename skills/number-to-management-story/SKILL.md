---
name: number-to-management-story
description: Adaptar uma decisão canônica de Variance para narrativa executiva curta, clara e utilizável em report, slide, e-mail ou reunião.
---

# Transformar número em narrativa gerencial

## Papel do skill

Este skill é o adapter de comunicação da decisão canônica de `Variance`. Ele
ajusta audiência, canal e densidade; não investiga a variação, não recalcula o
baseline e não cria uma causa nova.

A decisão precisa existir antes da comunicação, no módulo
`skills/explain-variance/SKILL.md`. O adapter executável está em
`scripts/variance_output_adapters.py`, na função `build_management_story`.

## Usar quando

- a explicação da variação já foi construída e precisa virar mensagem executiva;
- o usuário quer headline, slide, report, e-mail curto ou fala de reunião;
- é necessário reduzir densidade sem perder impacto, evidência, recorrência ou
  nível de confiança;
- a mesma decisão também será exibida em um one-pager, report, slide, e-mail ou
  fala de reunião.

## Não usar quando

- a análise ainda está exploratória e não existe uma decisão canônica, mesmo
  que essa decisão venha a ser classificada como hipótese ou evidência insuficiente;
- o objetivo é descobrir ou testar drivers, e não comunicar uma decisão;
- a audiência pede a trilha técnica integral em vez de síntese;
- faltam baseline, drivers, impacto, ação ou status no contrato canônico.

## Interface

Entrada obrigatória:

- `VarianceExplanation` do módulo canônico;
- `audience` opcional para identificar a audiência;
- `channel` opcional para identificar report, slide, e-mail ou reunião.
- `density` opcional (`concise`, `standard` ou `detailed`); quando ausente, o
  canal e a audiência definem o nível de detalhe.

Saída de `build_management_story`:

1. `headline`: direção, unidade, referência, status e driver principal;
2. `principal_driver`: `primary_driver_name` declarado pela decisão canônica;
3. `caveat`: incerteza, lacuna, reconciliação, efeito contábil, timing ou
   one-off que devam permanecer visíveis;
4. `managerial_implication`: impacto gerencial canônico;
5. `monitoring`: ação, owner e timing canônicos;
6. `drivers`, `evidence`, `recurrence`, `status`, `confidence` e
   `reconciliation` como suporte da mensagem;
7. `density` e `message`: densidade aplicada e mensagem renderizada para o canal;
8. `original`: registro completo da `VarianceExplanation` que originou a
   narrativa.

O registro `original` e os campos de suporte permitem revisar a mensagem sem
precisar reconstruir a decisão a partir de uma frase resumida.

## Sequência do adapter

### 1. Ler a decisão, não reabrir a investigação

Usar baseline, quebra, drivers, evidência, impacto, recorrência, confiança,
status, reconciliação e ação exatamente como foram entregues pelo contrato.

### 2. Definir audiência e canal

Registrar quem receberá a mensagem e como ela será consumida. `slide` e reunião
usam densidade concisa; e-mail usa densidade padrão; report e one-pager usam
densidade detalhada. `density` explícita pode substituir esse default. A
densidade altera a quantidade de contexto renderizado, preservando todos os
campos analíticos estruturados.

### 3. Formar a headline

Descrever Actual contra a referência com direção, magnitude e unidade canônicas,
usando apenas o `primary_driver_name`. Para status `hypothesis` ou
`insufficient_evidence`, declarar a incerteza na própria headline. O adapter não
escolhe o driver por posição ou impacto e não transforma hipótese em fato.

### 4. Preservar a ressalva

Mostrar no corpo principal qualquer driver contábil, `evidence_gap`,
hipótese, reconciliação incompleta ou não reconciliada, além de timing e
one-off. Se o status não for confirmado, escrever como leitura preliminar ou
insuficiente, conforme o contrato.

### 5. Fechar com implicação e monitoramento

Usar o impacto gerencial e a ação canônicos. O monitoramento pode ser
apresentado em uma frase mais curta, mas deve manter owner e timing quando
existirem.

## Formato de saída

### Narrativa executiva

1. Headline do resultado.
2. Driver principal.
3. Ressalva ou ruído contábil.
4. Implicação gerencial.
5. Próximo passo ou monitoramento.

### Padrões de redação

Headline confirmada:

`Actual ficou [unidade] [magnitude] [acima/abaixo] de [referência], principalmente por [driver canônico].`

Headline com incerteza:

`Actual ficou [magnitude] [acima/abaixo] de [referência]; a leitura permanece [hipotética/com evidência insuficiente]. Driver principal declarado: [driver canônico].`

Mensagem para slide:

`Mensagem principal: [headline]. Ressalva: [caveat]. Implicação: [impacto]. Monitoramento: [ação].`

Mensagem para gestor não financeiro:

Explicar a consequência gerencial do impacto canônico sem remover a ressalva
contábil ou a incerteza que condiciona a decisão.

## Guardrails

- Não recalcular Actual, referência, Variance, percentual ou reconciliação.
- Não reclassificar drivers, decidir uma causa concorrente ou alterar impacto.
- Não alterar `status`, `confidence`, `recurrence` ou `requires_validation`.
- Não esconder efeito contábil, evidência faltante, hipótese ou lacuna atrás de
  uma frase executiva.
- Não apresentar uma leitura preliminar como conclusão confirmada.
- Não adaptar apenas para soar melhor; adaptar para melhorar a decisão.
- Não remover o registro `original` da saída persistida.
