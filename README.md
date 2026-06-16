# accounting-ops

Agente para accounting, controladoria e FP&A com foco em entendimento do número, performance e suporte à decisão.

## O que é

O `accounting-ops` existe para transformar número, contabilidade, auditoria e contexto operacional em raciocínio de negócio.

Ele ajuda principalmente em temas como:

- fechamento e qualidade do número
- leitura gerencial de resultado
- orçamento, forecast e cenários
- análise de variações
- margem e drivers de performance
- capital de giro, caixa e reconciliações

## Para quem é

O `accounting-ops` é útil para:

- profissionais em transição para controladoria, accounting ou FP&A
- pessoas que querem aprender raciocínio financeiro com foco prático
- quem precisa estruturar análises de número, variação, margem e forecast
- quem quer transformar leitura financeira em mensagem executiva mais clara

## Como começar

Se você está entendendo o produto:

- leia `README.md`
- use `INDEX.md` para um mapa rápido
- use `PRODUCT_INDEX.md` se precisar localizar módulos específicos

Se você é um agente ou ambiente agentic:

- use `AGENTS.md` como porta de entrada compatível
- use `CLAUDE.md` como instrução operacional autoritativa

## Quick Start

1. Abra este repositório no seu ambiente agentic de preferência.
2. Leia `AGENTS.md` e depois `CLAUDE.md`.
3. Defina o objetivo com clareza: fechamento, forecast, margem, capital de giro, narrativa executiva ou aprendizagem.
4. Use `PRODUCT_INDEX.md` apenas se precisar localizar o módulo mais adequado.
5. Trabalhe com o menor conjunto possível de arquivos, em vez de carregar a base inteira.

## Como funciona

O fluxo básico do produto é:

1. entender o problema
2. escolher a trilha principal entre `tracks/accounting/` e `tracks/fpa/`
3. carregar a base metodológica mínima em `_method-wiki/`
4. aplicar o workflow, playbook, template ou skill mais adequado
5. transformar a análise em explicação, mensagem executiva ou próximo passo

## O que ele não é

- não é gerador de resposta decorada
- não substitui experiência hands-on que a pessoa ainda não teve
- não deveria maquiar gaps de dado, evidência ou experiência
- não serve para carregar a base inteira sem critério

## Project Structure

```text
accounting-ops/
├── AGENTS.md         # Entry point compatível para agentes
├── CLAUDE.md         # Instrução operacional autoritativa
├── README.md         # Visão geral do produto
├── INDEX.md          # Mapa rápido da estrutura
├── PRODUCT_INDEX.md  # Inventário navegável
├── PROMPT_INICIAL.md # Prompt sugerido para novas conversas
├── DATA_CONTRACT.md  # Fronteiras e camadas do produto
├── HEALTH_CHECK.md   # Diagnóstico operacional do produto
├── domain.md         # Mapa conceitual central
├── _method-wiki/     # Base metodológica viva
├── tracks/           # Trilhas por domínio
├── templates/        # Artefatos reutilizáveis de análise e treino
├── skills/           # Transformações atômicas
├── context/          # Contexto pessoal, casos e mapas de aprendizagem
├── books/            # Camada de ingestão e mapeamento de livros
├── examples/         # Exemplos calibradores
└── archive/          # Histórico de specs, planos e casos anteriores
```

## Capacidades principais

| Capacidade | O que faz |
|---|---|
| Fechamento e qualidade do número | Estrutura revisão de saldos, consistência e leitura gerencial do resultado |
| Análise de variações | Explica desvio com baseline, driver, impacto e ação |
| Forecast e orçamento | Ajuda a revisar premissas, drivers, cenários e outlook |
| Margem e performance | Organiza leitura de preço, mix, custo e eficiência |
| Capital de giro | Apoia análise de DSO, estoque, payables e conversão de caixa |
| Narrativa executiva | Traduz análise financeira em mensagem clara para gestão |
| Aprendizagem aplicada | Apoia desenvolvimento de raciocínio financeiro com foco prático e conexão com o trabalho real |

## Princípios do produto

- separar fato, hipótese, impacto e ação
- não maquiar gaps de experiência ou evidência
- traduzir auditoria para linguagem de negócio sem inflar experiência hands-on
- priorizar raciocínio prático sobre definição decorada

## Onde está o detalhe

- `CLAUDE.md`: roteamento, guardrails e seleção de módulos
- `PRODUCT_INDEX.md`: inventário navegável de workflows, playbooks, templates, skills, contextos e books
- `HEALTH_CHECK.md`: como avaliar a saúde operacional do produto
- `backlog local do produto: evolução planejada fora da versão pública`: evolução planejada do produto
