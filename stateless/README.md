# Stateless Layer

Esta pasta concentra a camada de adaptação do `accounting-ops` para ferramentas stateless, como ambientes corporativos de Copilot sem repositório, sem memória persistente e com limite rígido de anexos.

## Objetivo

Transformar conhecimento operacional rico em artefatos curtos, reutilizáveis e consumíveis sob demanda.

Esta camada existe para:

- reduzir o custo de preparação por tarefa
- preservar a lógica central do `accounting-ops`
- permitir uso com no máximo 2 anexos e 1 prompt curto
- separar claramente a base mestra do pacote de consumo

Esta camada não existe para:

- portar o agente inteiro para fora do repositório
- duplicar `_method-wiki/`, `tracks/`, `skills/` ou `playbooks/`
- criar uma enciclopédia para anexar
- reconstruir um harness em ambiente stateless

## Arquitetura

```text
stateless/
  README.md
  operating-manuals/
  core-lenses/
  company-packs/
  analytical-lenses/
  output-modes/
  prompt-templates/
  adaptation/
```

## Papel De Cada Pasta

- `operating-manuals/`: instruções estáveis de comportamento, qualidade e formato da análise
- `core-lenses/`: princípios centrais do `accounting-ops` sem depender de empresa específica
- `company-packs/`: contexto organizacional e lente de negócio por empresa
- `analytical-lenses/`: snippets especializados para mudar a lente de leitura
- `output-modes/`: formatos de resposta para diferentes públicos e usos
- `prompt-templates/`: prompts-base curtos para operação diária
- `adaptation/`: regras editoriais da tradução `harness -> stateless`

## Contrato De Uso

Fluxo padrão:

1. anexar um arquivo de `operating-manuals/`
2. anexar um arquivo de `company-packs/` ou `core-lenses/`
3. colar um arquivo de `prompt-templates/` como base da tarefa
4. opcionalmente colar uma lente de `analytical-lenses/`
5. opcionalmente pedir reformatação com um arquivo de `output-modes/`

Limites operacionais:

- no máximo 2 anexos por interação
- no máximo 1 lente adicional por prompt
- o contexto da tarefa deve ficar no prompt, não nos anexos fixos

## Formatos Padrão

### Analytical Lenses

Cada arquivo em `analytical-lenses/` deve seguir esta estrutura:

```md
# Nome da lente

## Quando usar
## Objetivo
## Instruções de análise
## Perguntas-chave
## Sinais de alerta
## Formato sugerido de resposta
```

### Operating Manuals E Core Lenses

Cada arquivo em `operating-manuals/` e `core-lenses/` deve seguir esta estrutura:

```md
# Nome do documento

## Papel deste documento
## Princípios
## Como analisar
## O que priorizar
## O que evitar
## Estrutura padrão de resposta
```

### Company Packs

Cada arquivo em `company-packs/` deve seguir esta estrutura:

```md
# Nome da empresa

## O que é a empresa
## Como ganha dinheiro
## Drivers principais
## O que importa para a liderança
## Linguagem e tom esperados
## Erros comuns de análise neste contexto
```

### Output Modes

Cada arquivo em `output-modes/` deve seguir esta estrutura:

```md
# Nome do modo

## Quando usar
## Objetivo do formato
## Estrutura obrigatória da resposta
## Nível de detalhe
## O que omitir
```

## Taxonomia Inicial

Core layers:

- `operating-manuals/general-analysis-manual.md`
- `core-lenses/accounting-ops-core-lens.md`
- `company-packs/belgo-lens.md`

Analytical lenses:

- `analytical-lenses/presentation-critique.md`
- `analytical-lenses/executive-storyline.md`
- `analytical-lenses/variance-analysis.md`
- `analytical-lenses/forecast-review.md`
- `analytical-lenses/budget-vs-actual.md`
- `analytical-lenses/margin-bridge.md`
- `analytical-lenses/working-capital-review.md`
- `analytical-lenses/cash-and-liquidity-review.md`
- `analytical-lenses/cost-and-productivity-review.md`
- `analytical-lenses/kpi-dashboard-review.md`
- `analytical-lenses/assumption-stress-test.md`
- `analytical-lenses/risk-and-gaps-review.md`

Output modes:

- `output-modes/executive-summary-mode.md`
- `output-modes/diagnostic-mode.md`
- `output-modes/critique-only-mode.md`
- `output-modes/cfo-briefing-mode.md`
- `output-modes/question-generation-mode.md`

Prompt templates:

- `prompt-templates/analyze-material-base.md`
- `prompt-templates/analyze-presentation.md`
- `prompt-templates/analyze-financial-pack.md`
- `prompt-templates/analyze-executive-memo.md`

## Regras De Transformação

Use estas regras ao converter materiais do `accounting-ops`:

- `workflow -> checklist mínimo de sequência analítica`
- `playbook -> heurísticas, critérios e sinais de alerta`
- `skill -> snippet curto de instrução operacional`
- `template -> formato de output`
- `method-wiki -> princípios estáveis para core lens`

Remover na compressão:

- detalhe excessivo de processo
- dependência de arquivos vizinhos
- roteamento longo
- contexto que só faz sentido com harness
- exemplos em excesso

Preservar na compressão:

- lógica analítica
- critérios de julgamento
- perguntas-chave
- armadilhas comuns
- formato de saída

## Mapeamento Inicial Sugerido

- `skills/challenge-variance-explanation.md` -> `analytical-lenses/variance-analysis.md`
- `skills/number-to-management-story.md` -> `analytical-lenses/executive-storyline.md`
- `_method-wiki/patterns/variance-analysis.md` -> `core-lenses/accounting-ops-core-lens.md`
- `_method-wiki/patterns/gross-margin-bridge.md` -> `analytical-lenses/margin-bridge.md`
- `_method-wiki/checklists/financial-projection-quality-checklist.md` -> `analytical-lenses/forecast-review.md`
- `tracks/fpa/playbooks/financial-information-communication.md` -> `analytical-lenses/presentation-critique.md`
- `templates/variance-analysis-one-pager.md` -> `output-modes/diagnostic-mode.md`

## MVP Recomendado

Primeira versão recomendada:

- `operating-manuals/general-analysis-manual.md`
- `core-lenses/accounting-ops-core-lens.md`
- `company-packs/belgo-lens.md`
- `analytical-lenses/presentation-critique.md`
- `analytical-lenses/variance-analysis.md`
- `analytical-lenses/forecast-review.md`
- `analytical-lenses/executive-storyline.md`
- `output-modes/executive-summary-mode.md`

## Critérios Editoriais

Um artefato em `stateless/` é bom quando:

- cabe em leitura rápida
- funciona sem depender do resto do repositório
- altera claramente a qualidade da análise
- é reutilizável em várias sessões
- não mistura contexto estável com instrução de execução

Um artefato em `stateless/` está ruim quando:

- tenta ensinar tudo
- repete a base mestra
- vira texto genérico
- não muda o comportamento do modelo
- exige manutenção desproporcional

## Próximos Passos

1. Criar os 8 arquivos do MVP.
2. Testar o pacote em uso real por duas semanas.
3. Revisar quais lentes realmente são usadas.
4. Expandir apenas o que provar valor.
