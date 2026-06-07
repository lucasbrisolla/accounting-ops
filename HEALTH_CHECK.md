---
tags:
  - accounting-ops
  - health-check
  - quality
---

# Health Check

Use esta nota para avaliar se o `accounting-ops` está saudável como produto agêntico e se a operação continua coerente com a arquitetura desejada.

O foco aqui não é revisar técnica financeira em si. É revisar a qualidade do sistema que organiza esse conhecimento e esse uso.

## Escala

- `0 - ausente`: não existe ou está apenas implícito.
- `1 - frágil`: existe, mas está concentrado, ambíguo ou pesado demais.
- `2 - utilizável`: opera com boa qualidade, mas ainda pede disciplina manual.
- `3 - confiável`: está modular, revisável e aguenta uso recorrente sem sobrecarga desnecessária.

## Check Estrutural Do Produto

| Área | Pergunta | Nota | Evidência |
| --- | --- | --- | --- |
| Entrada | `README.md`, `AGENTS.md` e `CLAUDE.md` têm papéis claros e sem duplicação desnecessária? |  |  |
| Fonte viva | `domain.md`, `_method-wiki/`, `tracks/`, `skills/` e `templates/` estão com papéis claros? |  |  |
| Routing | O problema é roteado primeiro para a trilha certa antes de carregar detalhes excessivos? |  |  |
| Method wiki | A base metodológica está sendo usada como fonte principal quando o problema pede conceito, checklist, pattern ou processo? |  |  |
| Tracks | A divisão `tracks/accounting/` x `tracks/fpa/` continua clara e útil? |  |  |
| Skills auxiliares | As skills fazem transformações atômicas e não substituem workflows inteiros? |  |  |
| Templates | Templates reduzem variação sem virar burocracia obrigatória? |  |  |
| Evolução | O produto consegue crescer sem concentrar tudo no `CLAUDE.md`? |  |  |

## Check Operacional

| Área | Pergunta | Nota | Evidência |
| --- | --- | --- | --- |
| Objetivo | Antes de responder, o agente deixa claro qual objetivo está atacando? |  |  |
| Escopo mínimo | O agente carrega só os módulos necessários, em vez da base inteira? |  |  |
| Explicação | A resposta separa causa, impacto, ação e lacuna quando isso importa? |  |  |
| Qualidade do número | O agente evita falar de performance sem antes considerar qualidade e confiabilidade do número? |  |  |
| Tradução para negócio | O produto traduz técnica contábil para linguagem de negócio sem inflar experiência hands-on? |  |  |
| Reuso | O mesmo tipo de problema tende a cair sempre no mesmo workflow ou playbook? |  |  |

## Resultado

- `0-12`: arquitetura ou operação ainda estão confusas demais.
- `13-24`: utilizável, mas com risco de inconsistência.
- `25-36`: produto maduro para uso recorrente.
- `37-42`: produto muito bem modularizado e operacionalmente confiável.

## Sinais De Alerta Específicos

Se dois ou mais itens abaixo aparecerem, o `accounting-ops` merece refactor prioritário:

- `CLAUDE.md` absorveu contexto que deveria estar em workflow, skill ou fonte metodológica
- a fronteira entre `tracks/accounting/` e `tracks/fpa/` ficou ambígua
- o agente precisa carregar `PRODUCT_INDEX.md` cedo demais para tarefas simples
- a mesma regra aparece em `README.md`, `CLAUDE.md` e `_method-wiki/` sem fonte clara
- a explicação de número virou narrativa bonita sem base suficiente

## Estado Sugerido Hoje

| Componente | Estado sugerido | Próxima melhoria |
| --- | --- | --- |
| Superfície de entrada | `forte` | manter papéis separados entre `README.md`, `AGENTS.md` e `CLAUDE.md` |
| Routing por trilha | `forte` | evitar expandir demais o `CLAUDE.md` |
| Base metodológica | `forte` | continuar promovendo conteúdo maduro para `_method-wiki/` |
| Verificabilidade | `frágil` | decidir no futuro se vale criar `doctor` ou `verify` leve |

## Ritual De Revisão

Use este arquivo:

1. ao revisar o `CLAUDE.md`
2. ao criar ou reescrever workflow importante
3. ao ampliar a trilha `accounting` ou `fpa`
4. quando o produto começar a parecer "inteligente demais cedo demais"

## Regra De Ouro

Se o produto explica bem a própria arquitetura, mas exige carregar arquivo demais antes de operar, ele ainda não está saudável o bastante.
