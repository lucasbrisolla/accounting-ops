# accounting-ops

O `accounting-ops` ajuda você a transformar números, contabilidade, auditoria e contexto operacional em análise financeira e suporte à decisão. O produto cobre accounting, controladoria e planejamento e análise financeira (FP&A).

## Para quem é

Use o produto se você:

- está em transição para accounting, controladoria ou FP&A
- quer aprender raciocínio financeiro com foco prático
- precisa estruturar análises de número, variação, margem ou previsão
- quer transformar uma análise financeira em mensagem executiva clara

## Como começar

1. Defina o objetivo: fechamento, previsão (forecast), margem, capital de giro, narrativa executiva ou aprendizagem.
2. Para navegar pela estrutura, consulte [`INDEX.md`](INDEX.md).
3. Para localizar um módulo específico, consulte [`PRODUCT_INDEX.md`](PRODUCT_INDEX.md).
4. Se você trabalha em um ambiente com suporte a agentes, leia [`AGENTS.md`](AGENTS.md) e depois [`CLAUDE.md`](CLAUDE.md).
5. Carregue apenas os arquivos necessários para o objetivo; não carregue a base inteira sem critério.

## Como funciona

O fluxo básico do produto é:

1. Entenda o problema e defina a pergunta que precisa ser respondida.
2. Escolha a trilha principal entre `tracks/accounting/` e `tracks/fpa/`.
3. Carregue a base metodológica mínima em `_method-wiki/`.
4. Aplique o workflow, playbook, template ou skill mais adequado.
5. Transforme a análise em explicação, mensagem executiva ou próximo passo.

## O que o produto cobre

| Capacidade | O que faz |
|---|---|
| Fechamento e qualidade do número | Estrutura a revisão de saldos, consistência e leitura gerencial do resultado. |
| Análise de variações | Explica desvios com base de comparação, fator, impacto e ação. |
| Previsão, orçamento e cenários | Ajuda a revisar premissas, fatores, cenários e projeções. |
| Margem e desempenho | Organiza a análise de preço, mix, custo e eficiência. |
| Custos industriais | Revisa valoração de estoques, custeio por processo, produção em processo (WIP), custo padrão e variâncias industriais. |
| Capital de giro | Apoia a análise de prazo médio de recebimento (DSO), estoque, contas a pagar e conversão de caixa. |
| Narrativa executiva | Traduz análise financeira em mensagem clara para a gestão. |
| Aprendizagem aplicada | Apoia o desenvolvimento de raciocínio financeiro com foco prático e conexão com o trabalho real. |

## O que o produto não é

- não gera respostas prontas sem raciocínio
- não substitui experiência prática
- não deve maquiar lacunas de dados, evidência ou experiência
- não serve para carregar a base inteira sem critério

## Estrutura do projeto

Esta árvore mostra as principais camadas compartilhadas do produto:

```text
accounting-ops/
├── AGENTS.md         # Entrada para agentes
├── CLAUDE.md         # Instrução operacional autoritativa
├── README.md         # Visão geral do produto
├── INDEX.md          # Mapa rápido da estrutura
├── PRODUCT_INDEX.md  # Inventário navegável
├── CONTEXT.md        # Glossário da arquitetura de conhecimento
├── DATA_CONTRACT.md  # Fronteiras e camadas do produto
├── HEALTH_CHECK.md   # Diagnóstico operacional do produto
├── domain.md         # Mapa conceitual central
├── _method-wiki/     # Base metodológica viva
├── tracks/           # Trilhas por domínio
├── templates/        # Artefatos reutilizáveis
├── skills/           # Transformações atômicas
├── context/companies/ # Estrutura de contexto por empresa
├── stateless/        # Adaptação para ambientes sem repositório
├── scripts/          # Ferramentas auxiliares
└── tests/            # Testes automatizados
```

A versão pública mantém conteúdo genérico e não inclui contextos específicos de empresas, livros, exemplos privados ou arquivos históricos.

## Princípios do produto

- separe fato, hipótese, impacto e ação
- não maquie lacunas de experiência ou evidência
- traduza auditoria para a linguagem de negócio sem inflar a experiência prática
- priorize raciocínio prático em vez de definições decoradas

## Onde encontrar detalhes

- [`CONTEXT.md`](CONTEXT.md): glossário da arquitetura de conhecimento
- [`CLAUDE.md`](CLAUDE.md): roteamento, guardrails e seleção de módulos
- [`PRODUCT_INDEX.md`](PRODUCT_INDEX.md): inventário navegável de workflows, playbooks, templates, skills e contextos
- [`HEALTH_CHECK.md`](HEALTH_CHECK.md): como avaliar a saúde operacional do produto
- O backlog de evolução do produto é mantido em um arquivo local, fora da versão pública.
