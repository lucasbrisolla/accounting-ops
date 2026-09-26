# Prompt base para análise de material

Use este prompt depois de anexar:

1. `operating-manuals/general-analysis-manual.md`;
2. `core-lenses/accounting-ops-core-lens.md` ou um `company-pack`;
3. no máximo uma lente adicional, quando a tarefa exigir.

Cole o contexto específico no trecho indicado. O prompt é curto de propósito:
as regras estáveis ficam nos anexos.

```text
Analise o material anexado para responder à tarefa abaixo.

Tarefa:
[descreva a pergunta, a decisão e o público]

Contexto que posso afirmar:
[período, entidade, baseline, dados disponíveis e limitações]

Siga estas regras:
- separe fato, hipótese, impacto, risco e ação;
- use apenas evidência presente no material ou declarada no contexto;
- declare lacunas em vez de inventar causa, valor, owner ou prazo;
- conecte a leitura a resultado, margem, caixa, capital, risco ou operação quando isso for relevante;
- adapte a densidade ao público, mantendo a ressalva que muda a decisão.

Entregue no modo de resumo executivo, salvo se eu pedir outro formato.
Comece pela mensagem principal e termine com ação ou próximo teste.
```
