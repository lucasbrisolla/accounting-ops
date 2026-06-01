# accounting-ops

Agente para accounting, controladoria e FP&A com foco em entendimento do número, performance e suporte à decisão.

## O que é

O `accounting-ops` existe para transformar número, contabilidade e raciocínio financeiro em leitura gerencial e pensamento de negócio.

Ele ajuda principalmente em temas como:

- fechamento e qualidade do número
- leitura gerencial de resultado
- orçamento, forecast e cenários
- análise de variações
- margem e drivers de performance
- capital de giro, caixa e reconciliações

## Como começar

Se você está entendendo o produto:

- leia `README.md`
- use `INDEX.md` para um mapa rápido
- use `PRODUCT_INDEX.md` se precisar localizar módulos específicos

Se você é um agente ou ambiente agentic:

- use `AGENTS.md` como porta de entrada compatível
- use `CLAUDE.md` como instrução operacional autoritativa

## Estrutura em alto nível

- `domain.md`: mapa conceitual central
- `_method-wiki/`: base metodológica viva
- `tracks/accounting/`: trilha de accounting e controladoria
- `tracks/fpa/`: trilha de FP&A
- `templates/`: formatos reutilizáveis de análise
- `skills/`: transformações atômicas sob demanda

## Project Structure

```text
accounting-ops-public/
├── AGENTS.md         # Entry point compatível para agentes
├── CLAUDE.md         # Instrução operacional autoritativa
├── README.md         # Visão geral do produto
├── INDEX.md          # Mapa rápido da estrutura
├── PRODUCT_INDEX.md  # Inventário navegável
├── DATA_CONTRACT.md  # Fronteiras e camadas do produto
├── domain.md         # Mapa conceitual central
├── _method-wiki/     # Base metodológica viva
├── tracks/           # Trilhas por domínio
├── templates/        # Artefatos reutilizáveis
└── skills/           # Transformações atômicas
```

## Princípios do produto

- separar fato, hipótese, impacto e ação
- não maquiar gaps de experiência ou evidência
- traduzir técnica contábil para linguagem de negócio
- priorizar raciocínio prático sobre definição decorada

## Onde está o detalhe

- `CLAUDE.md`: roteamento, guardrails e seleção de módulos
- `PRODUCT_INDEX.md`: inventário navegável de workflows, playbooks, templates e skills
