---
title: Companies Context
tags:
  - accounting-ops
  - context
  - companies
---

# Contexto de Companhias

Esta pasta guarda contexto situado de empresas específicas, comparáveis e empresa piloto.

## Objetivo

Usar relatórios, releases, apresentações, MD&A, formulários de referência e outras fontes de uma companhia específica para gerar insumo operacional para:

- accounting
- controladoria
- FP&A
- leitura externa de modelo de negócio
- perguntas para a empresa piloto

## Regra de camada

Tudo aqui começa como contexto específico de companhia.

Não promover conteúdo desta pasta para `_method-wiki/`, `tracks/`, `skills/` ou `templates/` sem decisão explícita de promoção.

## Estrutura padrão

Cada companhia deve usar a seguinte estrutura:

```text
context/companies/<slug-da-empresa>/
  README.md
  source-manifest.md
  promotion-matrix.md
  raw/
  library/
  distillations/
  promotions/
  enterprise-context.md
  evidence-bundle.md
  promotion-notes.md
```

## Pastas especiais

- `_template/`: estrutura-modelo para novas companhias
- `company-slug/`: exemplo pronto para duplicar ou renomear ao iniciar a primeira destilação real

## Próximo uso recomendado

1. Escolher a companhia comparável.
2. Renomear ou copiar `company-slug/` para o `slug` real.
3. Preencher `source-manifest.md`.
4. Posicionar a primeira fonte em `raw/`.
5. Criar a leitura operacional em `enterprise-context.md`.
