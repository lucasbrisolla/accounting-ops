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
| Fonte viva | `domain.md`, `_method-wiki/`, `tracks/`, `skills/`, `templates/`, `context/` e `books/` estão com papéis claros? |  |  |
| Routing | O problema é roteado primeiro para a trilha certa antes de carregar detalhes excessivos? |  |  |
| Method wiki | A base metodológica está sendo usada como fonte principal quando o problema pede conceito, checklist, pattern ou processo? |  |  |
| Tracks | A divisão `tracks/accounting/` x `tracks/fpa/` continua clara e útil? |  |  |
| Skills auxiliares | As skills fazem transformações atômicas e não substituem workflows inteiros? |  |  |
| Templates | Templates reduzem variação sem virar burocracia obrigatória? |  |  |
| Contexto | `context/` ajuda a calibrar uso e narrativa sem contaminar o produto inteiro? |  |  |
| Contexto empresarial | `context/companies/` separa evidência situada, contexto de companhia e candidatos de promoção metodológica? |  |  |
| Stateless | `stateless/` contém adaptações úteis para ambientes sem memória persistente sem virar taxonomia aspiracional demais? |  |  |
| Books | `books/` continuam como camada de ingestão e não como desvio do fluxo principal? |  |  |
| Pipeline editorial | A camada `books/` e o contexto empresarial usam o mesmo registro de promoção, sem competir com `_method-wiki/`? |  |  |
| Evolução | O produto consegue crescer sem concentrar tudo no `CLAUDE.md`? |  |  |

## Check Operacional

| Área | Pergunta | Nota | Evidência |
| --- | --- | --- | --- |
| Objetivo | Antes de responder, o agente deixa claro qual objetivo está atacando? |  |  |
| Escopo mínimo | O agente carrega só os módulos necessários, em vez da base inteira? |  |  |
| Explicação | A resposta separa causa, impacto, ação e lacuna quando isso importa? |  |  |
| Qualidade do número | O agente evita falar de performance sem antes considerar qualidade e confiabilidade do número? |  |  |
| Tradução para negócio | O produto traduz técnica contábil para linguagem de negócio sem inflar experiência hands-on? |  |  |
| Consistência editorial | O tom e o formato final permanecem coerentes com o produto? |  |  |
| Reuso | O mesmo tipo de problema tende a cair sempre no mesmo workflow ou playbook? |  |  |
| Crescimento controlado | Novos módulos entram em lugar certo, sem gerar duplicação óbvia? |  |  |

## Resultado

- `0-14`: arquitetura ou operação ainda estão confusas demais.
- `15-28`: utilizável, mas com risco de carga cognitiva e inconsistência.
- `29-42`: produto maduro para uso recorrente.
- `43-54`: produto muito bem modularizado e operacionalmente confiável.

## Sinais De Alerta Específicos

Se dois ou mais itens abaixo aparecerem, o `accounting-ops` merece refactor prioritário:

- `CLAUDE.md` absorveu contexto que deveria estar em workflow, skill ou fonte metodológica
- a fronteira entre `tracks/accounting/` e `tracks/fpa/` ficou ambígua
- o agente precisa carregar `PRODUCT_INDEX.md` cedo demais para tarefas simples
- a mesma regra aparece em `README.md`, `CLAUDE.md` e `_method-wiki/` sem fonte clara
- `books/` começaram a competir com o fluxo principal em vez de alimentar a base viva
- `context/companies/` começou a promover aprendizados situados para método geral sem registro em matriz ou nota de promoção
- `stateless/` passou a divergir das fontes mestras ou a manter artefatos sem fonte registrada
- a experiência de auditoria está sendo vendida como experiência direta de controladoria ou FP&A

## Estado Sugerido Hoje

| Componente | Estado sugerido | Próxima melhoria |
| --- | --- | --- |
| Superfície de entrada | `forte` | manter papéis separados entre `README.md`, `AGENTS.md` e `CLAUDE.md` |
| Routing por trilha | `forte` | evitar expandir demais o `CLAUDE.md` |
| Base metodológica | `forte` | continuar promovendo conteúdo maduro para `_method-wiki/` |
| Contexto, companies e books | `utilizável` | manter a fronteira entre evidência situada, promoção metodológica e ingestão editorial |
| Stateless | `confiável` | validar o pacote em uso real e manter a derivação registrada em `stateless/adaptation/README.md` |
| Verificabilidade | `utilizável` | manter o `Product Contract` versionado, o `doctor` calibrado por camada e os checks próximos dos outputs canônicos |

## Ritual De Revisão

Use este arquivo:

1. ao revisar o `CLAUDE.md`
2. ao criar ou reescrever workflow importante
3. ao ampliar a trilha `accounting` ou `fpa`
4. quando o produto começar a parecer "inteligente demais cedo demais"
5. antes de replicar padrões deste agente para outros produtos
6. junto com `scripts/accounting_ops_product_contract.py` e `scripts/accounting_ops_doctor.py`, quando houver mudança estrutural relevante

## Regra De Calibração Do Doctor

O `doctor` deve medir fronteiras atuais do produto, não fantasmas de versões antigas.

- `scripts/accounting_ops_product_contract.py` é a fonte da política; o
  `doctor` não deve reintroduzir listas, regex ou regras de camada na saída.
- Findings devem preservar categoria, alvo, mensagem e gravidade para que um
  caller possa renderizar a decisão sem reconstruir a regra.
- `scripts/promotion_pipeline.py` é o formato comum; o `Product Contract` deve
  rejeitar registros ausentes, incoerentes ou fora da camada de origem.

- nomes de empresas são esperados em `context/companies/`
- lentes específicas de companhia são esperadas em `stateless/company-packs/`
- nomes de empresas em `_method-wiki/`, `tracks/`, `skills/`, `templates/` ou superfícies principais devem ser tratados como possível contaminação de método geral por caso específico
- termos legados só devem permanecer como drift se ainda representarem risco real de regressão

## Regra De Ouro

Se o produto explica bem a própria arquitetura, mas exige carregar arquivo demais antes de operar, ele ainda não está saudável o bastante.
