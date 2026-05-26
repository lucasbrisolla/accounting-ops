# Financial Statement Analysis

Piloto de destilação editorial do livro *Financial Statement Analysis* (Martin Fridson e Fernando Alvarez) para aprofundar o `accounting-ops`.

## Fonte

Arquivo de origem mantido fora desta edição pública.

Leitura atual: apenas índice/sumário.

## Papel desta pasta

Esta pasta não é destino final de conhecimento.

Ela existe para transformar o livro em insumo útil para a base viva do produto, de forma seletiva e incremental.

O modelo desta pasta segue o padrão editorial já testado em outros livros de `books/`, mas com foco mais forte em leitura crítica do número, qualidade do lucro, sinais de distorção e projeções financeiras.

## Estratégia

1. **Índice** (`financial-statement-analysis-index.md`) — mapa de destilação editorial do livro.
2. **Sessões por capítulo** — abrir apenas o capítulo priorizado e o artefato de destino mais provável.
3. **Promoção seletiva** — levar conteúdo apenas para a camada operacional do produto quando houver valor claro.

## Fluxo editorial

O fluxo desejado é:

- lacuna real no `accounting-ops`
- capítulo priorizado
- destino definido antes da escrita
- leitura seletiva
- promoção para a base viva
- atualização do índice com status editorial

## Destinos possíveis

Antes de destilar um capítulo, decidir o destino mais provável:

- `_method-wiki/concepts/`
- `_method-wiki/heuristics/`
- `_method-wiki/checklists/`
- `_method-wiki/patterns/`
- `_method-wiki/processes/`
- `tracks/*/workflows/`
- `tracks/*/playbooks/`
- `tracks/*/modes/`
- `skills/`
- descarte por enquanto

## Filtro de promoção

O teste para promover conteúdo deste livro é:

> "Uma pessoa de accounting, controladoria ou FP&A usaria isso para questionar, interpretar, explicar ou projetar o número sem reescrever do zero?"

Se a resposta for não:

- descartar por enquanto
- ou manter apenas como referência de baixa prioridade

## Regra de uso do índice

O índice não serve apenas para dizer o que cada capítulo parece conter.

Ele funciona como painel de status para responder:

- o que deste livro serve ao produto
- onde isso deve entrar
- o que já está coberto
- o que ainda precisa ser destilado
- o que deve ser descartado por baixa aderência

## Status

- [x] Estrutura da pasta criada.
- [x] Índice inicial baseado no sumário criado.
- [x] Adaptação do framework editorial aplicada.
- [ ] Leitura de capítulos priorizados.
- [ ] Promoção dos primeiros capítulos úteis para a camada operacional.
- [ ] Validação do modelo como parte do padrão para os outros livros de `books/`.

## Observação

Este livro tende a alimentar mais fortemente `playbooks`, `concepts`, `heuristics` e alguns workflows específicos ligados a reconhecimento de receita, despesa e projeções.

Se a leitura detalhada revelar uma lacuna estrutural real, ainda pode fazer sentido criar novos MDs em vez de apenas enriquecer os existentes.
