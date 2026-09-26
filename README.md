<h1 align="center">accounting-ops</h1>

<p align="center">
  Transforme números financeiros em entendimento do resultado, leitura de performance e suporte à decisão.
</p>

<p align="center">
  <a href="#visão-geral">Visão geral</a> ·
  <a href="#capacidades">Capacidades</a> ·
  <a href="#como-funciona">Como funciona</a> ·
  <a href="#estrutura-do-produto">Estrutura</a> ·
  <a href="#limites">Limites</a>
</p>

## Visão geral

O `accounting-ops` é um produto-agente para accounting, controladoria e planejamento e análise financeira (FP&A). Ele ajuda você a transformar números, contabilidade, auditoria e contexto operacional em análises financeiras rastreáveis e suporte à decisão.

O produto organiza conhecimento, método e execução para responder quatro perguntas:

- o que aconteceu;
- por que aconteceu;
- qual foi o impacto;
- o que deve ser feito ou monitorado.

## Para quem é

Use o produto quando você:

- está em transição para accounting, controladoria ou FP&A;
- quer aprender raciocínio financeiro com foco prático;
- precisa estruturar análises de número, variação, margem ou previsão;
- quer transformar uma análise financeira em uma mensagem executiva clara.

## Capacidades

| Capacidade | O que você consegue fazer |
| --- | --- |
| Fechamento e qualidade do número | Estruturar a revisão de saldos, consistência e leitura gerencial do resultado. |
| Análise de variações | Explicar desvios com base de comparação, fator, impacto e ação. |
| Previsão, orçamento e cenários | Revisar premissas, fatores, cenários e projeções. |
| Margem e desempenho | Organizar a análise de preço, mix, custo e eficiência. |
| Custos industriais | Revisar valoração de estoques, custeio por processo, produção em processo (WIP), custo padrão e variâncias industriais. |
| Capital de giro | Apoiar a análise de prazo médio de recebimento (DSO), estoque, contas a pagar e conversão de caixa. |
| Narrativa executiva | Traduzir análise financeira em uma mensagem clara para a gestão. |
| Aprendizagem aplicada | Desenvolver raciocínio financeiro conectado ao trabalho real. |

## Como funciona

O produto usa a menor base de conhecimento suficiente para cada pergunta:

1. Defina o objetivo: fechamento, previsão, margem, capital de giro, narrativa executiva ou aprendizagem.
2. Escolha a trilha principal entre [`tracks/accounting/`](tracks/accounting/) e [`tracks/fpa/`](tracks/fpa/).
3. Carregue a base metodológica mínima em [`_method-wiki/`](_method-wiki/).
4. Aplique o workflow, playbook, template ou skill mais adequado.
5. Transforme a análise em explicação, mensagem executiva ou próximo passo.

Para uma `Variance` já delimitada com `Actual` e `Baseline`, comece pela skill [`explain-variance`](skills/explain-variance/SKILL.md). Para um sinal, anomalia ou discrepância cuja causa ainda não esteja estabelecida, use [`financial-investigation`](skills/financial-investigation/SKILL.md) antes de fechar a explicação.

## Comece por uma pergunta

Escolha o ponto de entrada que corresponde ao trabalho:

| Se você precisa... | Comece por... |
| --- | --- |
| entender a arquitetura e o vocabulário | [`domain.md`](domain.md) e [`CONTEXT.md`](CONTEXT.md) |
| encontrar um workflow, playbook, template ou skill | [`PRODUCT_INDEX.md`](PRODUCT_INDEX.md) |
| revisar fechamento, qualidade do número ou leitura gerencial | [`tracks/accounting/`](tracks/accounting/) |
| revisar forecast, orçamento, drivers ou performance | [`tracks/fpa/`](tracks/fpa/) |
| investigar uma variação ou discrepância | [`skills/financial-investigation/SKILL.md`](skills/financial-investigation/SKILL.md) e [`skills/explain-variance/SKILL.md`](skills/explain-variance/SKILL.md) |
| verificar a saúde operacional do produto | [`HEALTH_CHECK.md`](HEALTH_CHECK.md) |

Carregue apenas os arquivos necessários para o objetivo. A base não deve ser carregada inteira sem critério.

## Estrutura do produto

Esta árvore mostra as principais camadas compartilhadas do produto:

```text
accounting-ops/
├── AGENTS.md          # Entrada para agentes
├── CLAUDE.md          # Instrução operacional autoritativa
├── README.md          # Visão geral do produto
├── PRODUCT_INDEX.md   # Catálogo operacional único
├── CONTEXT.md         # Glossário da arquitetura de conhecimento
├── DATA_CONTRACT.md   # Fronteiras e camadas do produto
├── HEALTH_CHECK.md    # Diagnóstico operacional do produto
├── domain.md          # Mapa conceitual central
├── _method-wiki/      # Base metodológica viva
├── tracks/            # Trilhas por domínio
├── templates/         # Artefatos reutilizáveis
├── skills/            # Transformações atômicas
├── context/companies/ # Estrutura de contexto por empresa
├── stateless/         # Adaptação para ambientes sem repositório
├── scripts/           # Ferramentas auxiliares
└── tests/             # Testes automatizados
```

### Camadas principais

- [`_method-wiki/`](_method-wiki/): conceitos, processos, patterns, checklists e heurísticas reutilizáveis;
- [`tracks/`](tracks/): trilhas de accounting e FP&A;
- [`skills/`](skills/): transformações atômicas para investigação, explicação e comunicação;
- [`templates/`](templates/): formatos de trabalho e outputs recorrentes;
- [`context/`](context/): contexto situado por empresa;
- [`scripts/`](scripts/): validações e adapters determinísticos.

## Princípios do produto

- separar fato, hipótese, impacto e ação;
- não maquiar lacunas de experiência ou evidência;
- traduzir auditoria para a linguagem de negócio sem inflar a experiência prática;
- priorizar raciocínio prático em vez de definições decoradas;
- preservar a relação entre fonte, análise, premissa e decisão.

## Limites

O `accounting-ops` não:

- gera respostas prontas sem raciocínio;
- substitui experiência prática ou julgamento contábil responsável;
- esconde lacunas de dados, evidência ou experiência;
- transforma uma recomendação em decisão aprovada sem registro humano;
- serve para carregar a base inteira sem critério.

## Documentação

- [`CONTEXT.md`](CONTEXT.md): glossário da arquitetura de conhecimento;
- [`CLAUDE.md`](CLAUDE.md): roteamento, guardrails e seleção de módulos;
- [`PRODUCT_INDEX.md`](PRODUCT_INDEX.md): catálogo operacional único de workflows, playbooks, templates, skills e contextos;
- [`HEALTH_CHECK.md`](HEALTH_CHECK.md): como avaliar a saúde operacional do produto;
- o backlog de evolução é mantido em [`_backlog/backlog-accounting-ops.md`](../_backlog/backlog-accounting-ops.md), fora da versão pública.

A versão pública mantém conteúdo genérico e não inclui contextos específicos de empresas, livros, exemplos privados ou arquivos históricos.
