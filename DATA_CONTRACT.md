# Contrato de Dados

Fronteira de dados do `accounting-ops`.

## Camada do Usuário

Pode conter contexto pessoal, empresas específicas, casos reais, fontes, evidências e exercícios do mantenedor.

- `context/`
- `examples/`

### Subcamadas recomendadas em `context/`

| Caminho | Uso |
|---|---|
| `context/companies/` | Empresas específicas, comparáveis, empresa piloto, relatórios de administração, MD&A, releases, evidências e destilações por companhia. |
| `context/cases/` | Casos aplicados, exercícios reais e análises com contexto sensível ou situado. |
| `context/learning/` | Mapas de aprendizagem, planos pessoais e trilhas de estudo do mantenedor. |

Informação de empresa específica deve começar em `context/companies/<slug-da-empresa>/`, não em `_method-wiki/` nem diretamente em `tracks/`.

## Camada de Sistema

Camada de método e operação reutilizável do agente.

- `CLAUDE.md`
- `README.md`
- `domain.md`
- `PRODUCT_INDEX.md`
- `DATA_CONTRACT.md`
- `_method-wiki/`
- `books/`
- `skills/`
- `tracks/`
- `templates/`

## Camada de Ingestão

Pode conter fonte externa, índice editorial e decisões de promoção.

- `books/`
- projetos de fonte criados com apoio do `agent-knowledge-ops`
- subpastas de `context/companies/<empresa>/raw/`, `library/`, `distillations/` e `promotions/`

A camada de ingestão não é destino final de método. Ela preserva rastreabilidade e evidência.

## Regra de Promoção

Informação específica de uma empresa só deve subir para a camada de sistema quando virar padrão recorrente, método reutilizável ou rotina operacional aplicável a mais de uma empresa.

| Origem | Destino inicial | Promoção possível |
|---|---|---|
| Relatório de administração de empresa | `context/companies/<empresa>/` | `_method-wiki/`, `tracks/`, `templates/` se gerar método recorrente. |
| Evidência, trecho, PDF, release ou call | `context/companies/<empresa>/raw/` ou `distillations/` | Evidence bundle ou nota sintética. |
| Insight sobre a empresa piloto | `context/companies/<empresa-piloto>/` | Playbook/checklist apenas se generalizar. |
| Conceito geral de accounting, controladoria ou FP&A | `_method-wiki/` | Pode alimentar workflows, skills e templates. |
| Rotina repetível | `tracks/*/workflows/` ou `tracks/*/playbooks/` | Pode ganhar template ou skill. |

## Regra

Personalização do mantenedor, empresas específicas e casos reais devem ficar em `context/`, `examples/` ou arquivos de preparação específicos.

Conceitos gerais de accounting, controladoria, FP&A, método operacional, templates reutilizáveis e regras de roteamento ficam na camada de sistema.

Não gravar contexto empresarial específico em `_method-wiki/` ou `tracks/` sem decisão explícita de promoção.
