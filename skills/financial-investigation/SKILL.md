---
name: financial-investigation
description: Investigar sinais, anomalias, afirmações ou dúvidas financeiras, operacionais, contábeis ou normativas quando a causa, o tratamento ou a evidência ainda não estiverem estabelecidos. Usar para separar fatos de hipóteses, definir testes, localizar fontes e fechar impacto e próximo passo; para uma Variance já estruturada, carregar primeiro explain-variance.
---

# Investigar uma questão financeira

## Objetivo

Transformar um `Sinal` em uma investigação sustentada por evidências. A skill
organiza o caminho entre o que foi observado, o que pode explicá-lo, qual dado
discrimina as hipóteses e qual decisão pode ser tomada.

Ela é uma camada transversal. Roteia para workflows, playbooks, contexto
empresarial e fontes normativas, mas não duplica conhecimento especializado nem
substitui a autoridade fiscal, contábil ou operacional responsável.

## Usar quando

- o usuário pedir para investigar, validar ou descobrir se algo está correto;
- houver uma discrepância, anomalia, afirmação de causa ou tratamento diferente
  entre transações, fornecedores, períodos ou unidades;
- uma explicação tiver sido recebida sem evidência, reconciliação ou fonte
  suficiente;
- for necessário decidir qual pergunta fazer em seguida ou qual evidência
  reduzirá mais a incerteza.

## Não usar como primeira camada quando

- já existe uma pergunta de `Variance` com `Actual`, `Baseline`, materialidade e
  drivers a construir: carregar primeiro `skills/explain-variance/SKILL.md`;
- o usuário quer apenas adaptar uma decisão já concluída para report, slide,
  e-mail ou reunião;
- a solicitação é brainstorming genérico sem sinal, escopo ou corpus mínimo.

## Roteamento

Classificar o sinal antes de carregar documentos. Usar o menor conjunto de fontes
capaz de testar a hipótese.

1. Para `Variance` direta, carregar primeiro
   `skills/explain-variance/SKILL.md`. Se já houver uma `VarianceExplanation`,
   preservá-la e investigar apenas drivers, evidências ou lacunas pendentes.
2. Para custos industriais amplos, carregar
   `skills/diagnose-industrial-costs/SKILL.md` e o workflow encaminhado por ela.
3. Para uma explicação frágil já construída, usar
   `skills/challenge-variance-explanation/SKILL.md` depois do contrato canônico.
4. Para uma empresa específica, consultar o README da empresa e apenas os
   playbooks, modelos e evidências situados que correspondam ao sinal. Manter
   o conhecimento empresarial fora desta skill.
5. Para questão normativa, localizar a fonte oficial aplicável, registrar sua
   data e comparar suas condições com os fatos da operação. Encaminhar a
   validação à área responsável quando o risco ou a evidência exigir.

Não carregar a base inteira para compensar uma pergunta mal delimitada.

## Entrada mínima

Aceitar uma frase, afirmação, número, transação, documento ou anomalia como
entrada inicial. Quando o contexto for insuficiente:

1. declarar o escopo que foi possível entender;
2. separar o que é dado observado do que é afirmação de alguém;
3. formular somente as perguntas de maior valor informacional;
4. entregar um mapa preliminar da investigação sem inventar fatos.

Não bloquear a investigação só porque faltam dados. A falta deve aparecer como
`Lacuna`, com a fonte provável e o teste necessário para fechá-la.

## Ciclo investigativo

### 1. Delimitar o sinal e a decisão

Registrar o evento ou afirmação, a pergunta que precisa ser respondida, a
entidade, operação, período, unidade, moeda, baseline e audiência quando
conhecidos. Marcar explicitamente cada dimensão ausente.

Para um caso normativo, incluir jurisdição, data de vigência, tipo de operação,
partes envolvidas, natureza do item e documentação disponível.

### 2. Separar fatos, afirmações e lacunas

Tratar como fato apenas o que tiver suporte observável ou documental. Uma
declaração de fornecedor, área ou gestor pode iniciar uma hipótese, mas não a
confirma sozinha.

Registrar:

- fatos conhecidos e sua fonte;
- afirmações ainda não testadas;
- dados ausentes, conflitantes ou fora do período;
- impacto que ainda não pode ser quantificado.

### 3. Formular hipóteses concorrentes

Criar poucas hipóteses plausíveis e mutuamente distinguíveis. Classificar cada
uma como investigação de:

- número: o valor, sinal, cálculo ou reconciliação está correto?
- processo: como o número foi produzido e transformado?
- causa: qual evento operacional ou comercial explica o efeito?
- norma: qual regra permite, exige ou impede o tratamento?
- decisão: o que ainda precisa ser conhecido antes de decidir?

Não listar possibilidades por exaustão. Priorizar hipóteses que mudariam a
decisão e que possam ser diferenciadas por evidência acessível.

### 4. Montar o plano de evidência

Para cada hipótese material, indicar a evidência necessária, a fonte provável,
o período, o owner conhecido, o custo de obtenção e o resultado que confirmaria
ou enfraqueceria a hipótese.

Usar a hierarquia conforme a natureza do sinal:

| Investigação | Evidência primária | Evidência auxiliar |
|---|---|---|
| Transação ou número | Sistema de origem, documento da operação e reconciliação | Declaração do owner, histórico e padrão |
| Processo operacional | Medição real, log, apontamento, BOM, padrão ou relatório operacional | Entrevista e média histórica |
| Causa financeira | Quebra quantitativa, driver reconciliado e vínculo com o evento | Explicação da área e comparação histórica |
| Tratamento normativo | Fonte oficial vigente e condições da regra | Prática histórica, solicitação comercial e opinião não formal |

O tipo, a origem, a data e a cobertura da evidência devem permanecer visíveis.

### 5. Executar testes discriminantes

Para cada hipótese material, especificar:

1. pergunta do teste;
2. evidência a consultar;
3. resultado esperado para cada hipótese concorrente;
4. resultado observado;
5. limitação ou conflito remanescente.

Classificar o achado como:

- `confirmada`: a evidência suporta a hipótese, as condições relevantes foram
  verificadas e a quantificação reconcilia quando aplicável;
- `refutada`: a evidência contradiz materialmente a hipótese;
- `inconclusiva`: falta evidência, há conflito entre fontes ou o teste não
  permite distinguir as hipóteses.

Ausência de evidência não é refutação. Plausibilidade não é confirmação.

### 6. Quantificar impacto e efeitos relacionados

Quantificar o impacto financeiro sempre que os dados permitirem. Separar valor
observado, estimativa, fórmula e dado ainda necessário.

Testar DRE, margem, EBITDA, caixa, capital de giro, estoque, forecast, risco ou
tratamento tributário somente quando forem relevantes ao sinal. Não preencher
uma dimensão apenas para completar um modelo. Quando não houver base, escrever
que o efeito é desconhecido e como obtê-lo.

Para `Variance`, não recalcular nem substituir o contrato canônico. Preservar
baseline, drivers, reconciliação, recorrência, confiança, impacto e ação de uma
`VarianceExplanation` já fornecida.

### 7. Fechar com decisão ou próximo teste

Encerrar com ação, owner e timing quando conhecidos. Se ainda não for possível
decidir, declarar a pergunta pendente e a evidência que a responde.

A investigação termina quando as hipóteses materiais estiverem classificadas ou
quando o próximo teste discriminante estiver claramente definido e for
proporcional ao valor da decisão.

## Formato de saída

Adaptar a densidade ao caso, preservando esta ordem:

```markdown
## Estado da investigação
[confirmada, refutada ou inconclusiva; força da evidência: forte, moderada,
fraca ou ausente]

## Sinal e escopo
[o que foi observado, pergunta, período, entidade, operação e lacunas de escopo]

## Fatos conhecidos
- [fato + fonte + data/período]

## Hipóteses
| Hipótese | Tipo | Evidência necessária | Fonte provável | Status | Força da evidência |
|---|---|---|---|---|---|
| [hipótese] | [número/processo/causa/norma/decisão] | [dado] | [fonte] | [status] | [força] |

## Testes e resultados
| Teste | Evidência consultada | Resultado | Limitação |
|---|---|---|---|
| [teste] | [evidência] | [achado] | [lacuna] |

## Impacto financeiro e riscos relevantes
[valor, fórmula, impacto em resultado/caixa/capital/estoque/forecast ou motivo
para a dimensão não se aplicar]

## Ação e pendências
[ação, owner, timing, fonte faltante ou pergunta para validação]
```

Não atribuir owner ou prazo quando não houver base. Escrever a lacuna em vez de
preencher o campo por inferência.

## Investigação normativa e tributária

Em ICMS, sucata ou qualquer tratamento dependente de regra:

1. identificar a jurisdição, período e operação concreta;
2. localizar a fonte oficial vigente e citar autoridade, regra e data;
3. listar as condições do enquadramento;
4. comparar cada condição com documentos, cadastro e fatos da operação;
5. separar o tratamento solicitado pelo fornecedor do tratamento permitido;
6. classificar como confirmada, refutada ou inconclusiva;
7. encaminhar a aprovação à área fiscal quando a materialidade, risco ou
   incerteza exigir.

Sem fonte normativa atual ou sem fatos suficientes, o resultado é
`inconclusivo`. A skill não emite parecer tributário nem transforma prática
histórica em regra.

## Padrões de aceitação

### Fornecedores de sucata com tratamentos de ICMS diferentes

Tratar a diferença como sinal. Investigar regra aplicável, condições da operação,
cadastro e documentação de cada fornecimento, fonte da informação fiscal e
responsável pela validação. Não concluir que a diferença está correta apenas
porque existe em lançamentos anteriores.

### EBITDA explicado por `Usage & Mix`

Carregar o contrato de `Variance`, reconciliar o valor e abrir o driver em
produto, planta ou processo. Testar consumo por tonelada, padrão, yield, scrap,
rework, setup, especificação e terceirização quando houver sinais. Preservar
qualquer hipótese ou diferença de reconciliação.

### Custo explicado por reajuste de fornecedor

Testar preço unitário contratado e realizado, volume, mix, data de vigência,
câmbio, especificação e efeito financeiro observado. Classificar a explicação
sem aceitar o reajuste declarado como causa suficiente.

## Guardrails

- Começar pelo sinal e pela decisão, não por uma conclusão desejada.
- Separar fato, afirmação, hipótese, evidência, achado e ação.
- Preferir o teste mais barato e discriminante antes de ampliar a coleta.
- Não inventar causa, valor, fonte, regra, owner ou prazo.
- Não tratar ausência de evidência como refutação.
- Não tratar explicação contábil, timing ou classificação como desempenho
  operacional sem teste do mecanismo econômico.
- Não alterar uma `VarianceExplanation` canônica nem criar uma segunda regra de
  baseline, materialidade, driver ou reconciliação.
- Para fontes normativas atuais, usar autoridade oficial e registrar a data.
- Declarar limitações e manter o resultado inconclusivo quando a evidência não
  sustentar uma conclusão.
- Responder em PT-BR, com acentuação correta e raciocínio explícito.
