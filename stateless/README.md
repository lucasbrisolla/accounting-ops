# Camada stateless

Esta pasta adapta o `accounting-ops` para ferramentas sem repositório, sem
memória persistente e com limite rígido de anexos.

## Estado da implementação

O MVP está fechado em `2026-09-26`. O pacote mantido contém dois anexos-base,
um prompt curto, lentes opcionais e um modo de saída executivo. As regras
continuam pertencendo às fontes mestras; esta camada só comprime e organiza o
uso.

O contrato de manutenção, as fontes e as condições de atualização estão em
[`adaptation/README.md`](adaptation/README.md).

## Objetivo

Transformar conhecimento operacional rico em artefatos curtos, reutilizáveis e
consumíveis sob demanda.

Esta camada existe para:

- reduzir o custo de preparação por tarefa;
- preservar a lógica central do `accounting-ops`;
- permitir uma interação com no máximo dois anexos e um prompt curto;
- separar a base mestra do pacote de consumo;
- manter rastreabilidade entre cada compressão e sua fonte.

Esta camada não existe para:

- portar o agente inteiro para fora do repositório;
- duplicar `_method-wiki/`, `tracks/`, `skills/` ou `playbooks/`;
- criar uma enciclopédia para anexar;
- reconstruir um harness em ambiente stateless;
- prometer lentes ou modos que ainda não foram implementados.

## Interface de uso

### Pacote base

1. Anexe `operating-manuals/general-analysis-manual.md`.
2. Anexe `core-lenses/accounting-ops-core-lens.md` ou um arquivo de
   `company-packs/`.
3. Cole `prompt-templates/analyze-material-base.md` e preencha a tarefa.
4. Use no máximo uma lente adicional, sem ultrapassar dois anexos.
5. Aplique `output-modes/executive-summary-mode.md` quando a audiência pedir
   uma síntese executiva.

Quando o caso já trouxer o contexto geral necessário, uma lente específica
pode substituir o segundo anexo. O contexto da tarefa sempre fica no prompt.

### Arquitetura

```text
stateless/
  README.md
  operating-manuals/
    general-analysis-manual.md
  core-lenses/
    accounting-ops-core-lens.md
  company-packs/
    <company-pack>.md
  analytical-lenses/
    presentation-critique.md
    variance-analysis.md
    forecast-review.md
    executive-storyline.md
  output-modes/
    executive-summary-mode.md
  prompt-templates/
    analyze-material-base.md
  adaptation/
    README.md
```

## Papel de cada pasta

- `operating-manuals/`: comportamento geral, qualidade e formato da análise;
- `core-lenses/`: princípios centrais sem depender de uma empresa;
- `company-packs/`: contexto comprimido e situado por empresa;
- `analytical-lenses/`: foco especializado para mudar a leitura;
- `output-modes/`: formatos de resposta para diferentes públicos;
- `prompt-templates/`: instruções curtas de execução;
- `adaptation/`: contrato de derivação, rastreabilidade e atualização das fontes.

## Regras de transformação

- `workflow` vira checklist mínimo de sequência analítica;
- `playbook` vira heurística, critério e sinal de alerta;
- `skill` vira instrução curta de operação;
- `template` vira formato de saída;
- `method-wiki` vira princípio estável para uma lente central.

Na compressão, remova dependências longas, roteamento que exige o harness,
detalhes excessivos e exemplos que não mudam a decisão. Preserve lógica,
critérios de julgamento, perguntas-chave, armadilhas e formato de saída.

Para `Variance`, a fonte canônica é
`skills/explain-variance/SKILL.md`. A lente stateless pode resumir essa lógica,
mas não pode criar outra regra para baseline, materialidade, driver, evidência,
impacto, reconciliação ou ação.

## Critérios editoriais

Um artefato stateless é bom quando:

- cabe em leitura rápida;
- funciona sem carregar o repositório inteiro;
- altera claramente a qualidade da análise;
- é reutilizável em várias sessões;
- aponta para a fonte mestra e para a condição de atualização.

Um artefato stateless está ruim quando:

- tenta ensinar tudo;
- repete a base mestra;
- vira texto genérico;
- não muda o comportamento do modelo;
- exige manutenção desproporcional;
- mantém uma promessa de pacote que não existe.

## Expansões futuras

Novas lentes, modos ou prompts só entram depois de um caso recorrente provar
valor. A expansão deve atualizar o contrato em `adaptation/README.md`, incluir a
fonte mestra e passar pela verificação estrutural do produto.
