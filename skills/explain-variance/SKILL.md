---
name: explain-variance
description: Construir uma explicação canônica de Variance com baseline, materialidade, drivers, evidência, impacto e ação.
---

# Explicar uma Variance

## Papel deste documento

Este é o módulo canônico para explicar uma `Variance` entre `Actual`, `Budget`, `Forecast` ou outro período comparativo. Ele concentra a decisão analítica antes que um `adapter` transforme a decisão em challenge, one-pager, narrativa executiva ou pacote stateless.

O contrato executável correspondente mantém as invariantes quantitativas e devolve um registro estável. O módulo de conteúdo mantém a sequência de raciocínio, os critérios de julgamento e os guardrails que o agente deve aplicar.

## Interface

O caller fornece:

- a pergunta que precisa ser respondida;
- o `Actual` e o `baseline` de comparação;
- o recorte da análise: linha, unidade, produto, cliente, projeto ou centro de custo;
- os dados disponíveis e as limitações de evidência;
- a audiência e a decisão que podem ser afetadas.

O módulo devolve uma decisão com estes campos:

| Campo | Papel |
|---|---|
| `Baseline` | Define a referência, o actual, a unidade, o tamanho e a direção da variação. |
| `Materialidade` | Registra limiar absoluto, porcentual e relevância decisória como booleano explícito acompanhado de justificativa. |
| `Quebra` | Localiza a variação no nível que permite investigá-la. |
| `Driver` | Explica a causa principal ou concorrente, seu tipo (operacional, contábil, comercial ou desconhecido) e seu impacto conhecido ou estimado. |
| `Driver principal` | Declara `primary_driver_name`; com múltiplos drivers, a prioridade pertence à decisão canônica, não ao adapter. |
| `Evidência` | Separa o dado disponível (`evidence`) da lacuna que ainda precisa ser obtida (`evidence_gap`). |
| `Impacto` | Conecta a variação a margem, EBITDA, caixa, forecast, risco ou operação. |
| `Ação` | Define validação, correção, monitoramento, owner e timing quando conhecidos. |
| `Recorrência` | Classifica o efeito como recorrente, one-off, timing ou desconhecido e registra em `recurrence_detail` a reversão, o encerramento ou a justificativa de não recorrência. |
| `Confiança` | Indica o nível de segurança da explicação. |

## Sequência

1. Defina a pergunta e o `baseline`: Actual vs. Budget, Actual vs. Forecast, mês anterior ou outra comparação explícita.
2. Calcule o valor e o porcentual da variação quando o denominador permitir.
3. Teste a materialidade por valor, porcentual, risco, recorrência ou impacto decisório. Declare separadamente se a relevância decisória é verdadeira ou falsa; o texto registra a justificativa, não decide sozinho.
4. Localize a variação por linha, unidade, produto, cliente, projeto ou centro de custo.
5. Abra os drivers plausíveis: volume, preço, mix, custo, eficiência, frete, estoque, timing, reclassificação ou outro driver de domínio.
6. Separe fato confirmado, hipótese provável e evidência ausente. Hipótese precisa declarar sua base; evidência ausente precisa nomear a lacuna.
7. Verifique se os impactos dos drivers reconciliam com a variação total. Se não reconciliarem, declare a diferença.
8. Declare o driver principal quando houver mais de um driver e conecte o número a margem, EBITDA, caixa, `Working capital`, `Forecast` ou operação.
9. Registre a recorrência. Para `timing`, declare a reversão ou o evento de encerramento; para `one_off`, justifique por que o efeito não tende a se repetir.
10. Feche com ação, owner, timing ou pergunta de validação. Quando não houver base para concluir, a ação deve ser obter a evidência faltante.

## Contrato de saída

Uma explicação só pode ser classificada como confirmada quando:

- existe um `Baseline` explícito;
- a materialidade foi avaliada;
- existe pelo menos uma quebra e um driver;
- existe um `primary_driver_name` pertencente aos drivers declarados;
- cada driver confirmado possui impacto e evidência;
- cada hipótese possui evidência que lhe dá base e cada driver sem evidência nomeia a lacuna;
- a soma dos drivers conhecidos reconcilia com a variação total;
- o impacto gerencial e a ação estão declarados;
- classificações `timing` e `one_off` possuem detalhe de recorrência;
- a confiança não é baixa.

Quando qualquer condição faltar, o módulo deve manter a explicação como hipótese ou insuficiência de evidência. A ausência de evidência não pode ser preenchida com uma causa inventada.

## Invariantes

- `Variance = Actual - Baseline`.
- Quando o `Baseline` é diferente de zero, `Variance % = Variance / Baseline × 100`.
- Driver confirmado exige impacto e evidência.
- Hipótese exige uma base de evidência; driver com evidência insuficiente exige `evidence_gap` explícito.
- O tipo do driver deve separar, quando possível, efeito operacional, contábil e comercial.
- Driver sem impacto conhecido torna a reconciliação incompleta.
- Driver estimado ou concorrente não pode ser apresentado como fato confirmado.
- O driver principal é declarado pelo contrato; adapters não inferem prioridade pela ordem.
- Explicação confirmada exige drivers confirmados e reconciliação completa.
- Materialidade pode ser quantitativa ou decisória. O booleano `decision_relevant` decide a relevância; `decision_relevance` registra sua justificativa.
- `Timing` deve indicar quando o efeito reverte ou qual evento o encerra.
- `One-off` deve explicar por que o efeito não tende a se repetir.
- Ação sem owner ou timing conhecido deve declarar a lacuna, não inventar um responsável.

## Cenários de referência

### Actual vs. Budget

O `Actual` é 120 e o `Budget` é 100. A variação de 20 é explicada por volume de 8 e serviços contratados de 12. Os dois drivers têm evidência, a soma reconcilia com a variação e a explicação pode ser classificada como confirmada, desde que o impacto e a ação estejam registrados.

### Actual vs. Forecast

O `Actual` é 130 e o `Forecast` é 110. O frete urgente explica 12 com evidência disponível, mas ainda faltam horas padrão e reais para confirmar o efeito de eficiência da linha. A explicação deve nomear essa lacuna em `evidence_gap`, marcar a reconciliação como incompleta e indicar a validação necessária antes de revisar o `Forecast`.

## Adapters previstos

O módulo é a fonte canônica para qualquer pergunta de `Variance`. O routing
deve carregá-lo antes de escolher uma saída. Os callers são adapters:

- `skills/challenge-variance-explanation/SKILL.md` pressiona a decisão;
- `skills/number-to-management-story/SKILL.md` adapta a decisão para narrativa
  executiva;
- a camada `stateless/` comprime a instrução, sem criar uma segunda regra
  mestre.

Esses callers podem mudar formato, audiência, canal e densidade, mas não podem
duplicar baseline, materialidade, driver, evidência, impacto, reconciliação ou
ação.

## Guardrails

- Não terminar em “a conta aumentou”.
- Não tratar ausência de evidência como prova de uma causa alternativa.
- Não confundir efeito contábil, timing e desempenho operacional.
- Não chamar toda variação favorável de eficiência ou oportunidade.
- Não esconder uma diferença de reconciliação para produzir uma narrativa mais limpa.
- Não escolher um workflow industrial antes de testar se o problema é de quantidade, valuation, WIP, padrão, absorção, eficiência, perda ou obsolescência.
- Escrever em PT-BR, com acentuação correta, e declarar lacunas de dados com clareza.
