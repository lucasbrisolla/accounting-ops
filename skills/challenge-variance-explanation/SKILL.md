---
name: challenge-variance-explanation
description: Pressionar uma explicação de variação antes que ela vire narrativa oficial. Usar quando a causa, o driver, a matemática ou a separação entre efeito operacional, contábil e não recorrente precisar ser testada.
---

# Desafiar explicação de Variance

## Objetivo

Submeter uma explicação canônica de `Variance` a pressão lógica antes que ela vire narrativa oficial.

Este documento é um `adapter` do módulo [`explain-variance`](../explain-variance/SKILL.md). Ele não recalcula a variação nem cria uma segunda regra para baseline, materialidade, driver, evidência, impacto ou ação.

## Usar quando

- a explicação de desvio parece boa demais e precisa ser testada
- o usuário quer questionar causa, driver ou racional de uma variação
- a narrativa mistura efeito operacional, contábil e não recorrente
- há risco de transformar hipótese em explicação fechada

## Não usar quando

- para variações irrelevantes ou rotineiras sem impacto decisório
- quando ainda não existe explicação mínima para ser desafiada
- quando o usuário só quer um resumo, não um challenge

## Interface

O challenge recebe uma `VarianceExplanation` já construída pelo módulo canônico. Ele preserva:

- baseline, actual, referência e variação calculada;
- materialidade e relevância decisória;
- quebra e drivers;
- evidência, status e confiança;
- impacto, recorrência e ação.

O adapter acrescenta somente:

- fragilidades encontradas;
- resultado do teste quantitativo de reconciliação;
- classificação de drivers operacionais, contábeis e hipotéticos;
- leitura revisada;
- confirmações pendentes.

## Sequência do adapter

### 1. Preservar a tese e o baseline

Ler do contrato canônico:

- qual variação está sendo explicada;
- qual é o `baseline`;
- qual materialidade foi declarada;
- qual impacto e ação foram registrados.

### 2. Ler o resultado quantitativo existente

Usar a reconciliação do contrato canônico:

- `reconciled`: os impactos dos drivers fecham com a `Variance`;
- `unreconciled`: os impactos não fecham e a narrativa precisa ser revista;
- `incomplete`: existe driver sem impacto conhecido e a investigação não está concluída.

O adapter não refaz a soma nem substitui o resultado do contrato.

### 3. Procurar fragilidades declaradas

Sinalizar:

- driver com status `hypothesis`;
- driver com status `missing_evidence`;
- reconciliação `unreconciled` ou `incomplete`;
- ausência de evidência em explicação que ainda não pode ser confirmada.

Classificar efeito contábil, `timing` e `one-off` separadamente. Essas naturezas não são fragilidades por si só. Abrir confirmação pendente somente quando `status`, reconciliação ou `evidence_gap` do contrato canônico demonstrar uma lacuna.

### 4. Preservar fato, hipótese e lacuna

Manter os status do módulo canônico também na linguagem da leitura revisada: usar leitura confirmada para `confirmed`, leitura hipotética para `hypothesis` e leitura preliminar com evidência insuficiente para `insufficient_evidence`. O challenge pode dizer que uma explicação é frágil, mas não deve converter hipótese em fato nem rebaixar fato confirmado por causa do tipo do driver ou da recorrência.

### 5. Reescrever a leitura

Produzir uma leitura revisada com:

- o impacto já registrado;
- o nível de certeza preservado;
- a ação ou validação recomendada;
- as confirmações pendentes quando houver fragilidade, tanto no campo estruturado quanto na leitura revisada.

## Formato de saída

1. Explicação original, preservada pelo contrato canônico.
2. Fragilidades da explicação.
3. Teste quantitativo: `reconciled`, `unreconciled` ou `incomplete`.
4. Leitura revisada.
5. O que ainda precisa ser confirmado.

## Guardrails

- Não desafiar por esporte.
- Não inventar drivers alternativos sem plausibilidade.
- Não tratar ausência de prova como refutação definitiva.
- Se a explicação estiver boa, dizer isso explicitamente.
- Não recalcular baseline, porcentual ou reconciliação fora do módulo canônico.
- Preservar o status e a confiança da explicação original nos campos e na linguagem da leitura revisada.
