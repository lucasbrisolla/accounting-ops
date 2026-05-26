# Comunicação de Informação Financeira

Playbook para transformar análise financeira em mensagem executiva, apresentação ou report de gestão.

Fonte principal: Jack Alexander, *Financial Planning, Analysis, and Performance Management*, Cap. 6.

## Quando Usar

- A análise já existe, mas ainda está em linguagem técnica demais.
- É preciso apresentar variação, forecast, orçamento, KPI ou resultado para gestão.
- O material tem muitos números, mas pouca mensagem.
- A audiência precisa decidir, priorizar ou agir, não apenas receber informação.
- Há risco de a apresentação virar defesa contábil, planilha comentada ou excesso de detalhe.

## Princípio Central

A melhor análise não é necessariamente a melhor forma de apresentação.

O trabalho de FP&A não termina quando o número foi explicado. Ele termina quando a mensagem ajuda a gestão a entender:

- o que aconteceu
- por que aconteceu
- o que isso muda
- quais alternativas existem
- que ação ou monitoramento vem depois

## Fluxo

### 1. Definir a Decisão ou Objetivo

Antes de montar slides, relatório ou mensagem, declarar:

- qual pergunta a comunicação precisa responder
- qual decisão, alinhamento ou atenção ela deve provocar
- quem é a audiência
- que nível de detalhe essa audiência consegue usar
- quais vieses ou premissas podem distorcer a leitura

Se não houver objetivo claro, a comunicação tende a virar despejo de análise.

### 2. Extrair a Mensagem Executiva

Converter a análise em uma tese curta:

- headline do resultado
- 3 a 5 mensagens principais
- causa dominante
- impacto financeiro ou operacional
- risco, oportunidade ou trade-off
- ação recomendada ou próximo passo

Boa comunicação financeira evita começar pela planilha. Ela começa pela implicação.

### 3. Adaptar à Audiência

Executivos normalmente precisam de:

- objetivo claro
- achados principais
- gráficos que mostrem tendência, magnitude ou exceção
- resumo das implicações
- ações indicadas
- detalhe técnico em anexo, não no corpo principal

Conselho, diretoria ou fórum sênior exigem preparação extra:

- antecipar perguntas difíceis
- dominar os detalhes mesmo que eles não apareçam nos slides
- ter uma versão curta caso o tempo seja reduzido
- separar fato, hipótese, julgamento e recomendação

Para gestores não financeiros, trocar jargão por linguagem de negócio:

- de "variação negativa de mix" para "vendemos mais itens de menor margem"
- de "efeito de competência" para "a despesa pertence ao período, embora o caixa saia depois"
- de "reclassificação contábil" para "muda a linha do demonstrativo, mas não muda o caixa nem a operação"

### 4. Escolher o Formato de Entrega

Escolher o canal pelo uso esperado:

| Situação | Melhor formato |
|---|---|
| Acompanhar rotina e exceções | dashboard, KPI ou alerta |
| Decisão executiva | apresentação curta com recomendação |
| Registro formal | relatório ou memo |
| Debate de premissas | reunião com material de apoio |
| Assunto sensível | conversa ao vivo antes de circular material |
| Consumo sob demanda | relatório pull com filtros e histórico |

O canal errado força a mensagem errada. Nem todo dashboard deve virar slide, e nem toda análise deve virar dashboard.

### 5. Estruturar a Apresentação

Estrutura base:

1. Objetivo ou pergunta da reunião.
2. Executive summary com a mensagem antes do detalhe.
3. Evidências principais.
4. Implicações para resultado, caixa, margem, risco ou operação.
5. Alternativas e recomendação.
6. Próximos passos e mecanismo de acompanhamento.
7. Anexos com detalhe técnico.

Regra prática: se o tempo cair pela metade, a audiência ainda deve receber a mensagem principal.

### 6. Escolher a Visualização Certa

Escolher o gráfico pelo ponto que ele precisa provar:

| Necessidade | Visual mais provável |
|---|---|
| Mostrar tendência no tempo | linha |
| Comparar magnitude entre itens | barras ou colunas |
| Mostrar composição de um total | barras empilhadas, pizza ou donut com poucas fatias |
| Explicar ponte entre início e fim | waterfall / bridge |
| Comparar actual vs budget ou forecast | colunas, barras ou bridge |
| Mostrar sensibilidade a premissas | tabela ou gráfico de sensibilidade |
| Sinalizar status contra meta | semáforo, scorecard ou gauge com parcimônia |

Guardrail: o gráfico deve reduzir ruído, não decorar a análise.

### 7. Ensaiar a Entrega

Antes de apresentar:

- escrever talking points por slide
- não ler o slide
- ensaiar o tempo
- preparar versão curta com as 3 mensagens essenciais
- antecipar perguntas e objeções
- saber onde estão os detalhes de suporte
- checar confidencialidade e sensibilidade da informação

Entrega boa combina objetividade com leitura da sala. Se a audiência travar em uma premissa, o apresentador precisa conseguir voltar ao objetivo sem perder a conversa.

## Checklist de Qualidade

- A primeira página já responde "e daí?".
- A mensagem separa fato, hipótese, impacto e ação.
- O material mostra o que vai bem e o que precisa melhorar.
- A recomendação é proporcional ao nível de certeza.
- O detalhe técnico está disponível, mas não domina a narrativa.
- A visualização escolhida reforça a mensagem principal.
- O material funciona como handout se circular depois da reunião.
- O tom foi ajustado para a audiência, não para quem fez a análise.

## Sinais de Problema

- Muitos números e nenhuma decisão.
- Explicação correta, mas sem implicação gerencial.
- Slide com planilha inteira em fonte pequena.
- Jargão contábil usado para esconder incerteza.
- Gráfico bonito que não responde a pergunta.
- Apresentação depende de 100% do tempo disponível para fazer sentido.
- Recomendação aparece apenas no final, depois que a audiência já se perdeu.

## Saída Recomendada

```markdown
## Mensagem Executiva

[headline curta]

## O Que Está Movendo o Número

- [driver 1]
- [driver 2]
- [driver 3]

## Implicação

[impacto em resultado, caixa, margem, risco ou operação]

## Recomendação

[ação, alternativa ou decisão proposta]

## Monitoramento

[KPI, prazo, responsável ou próximo checkpoint]
```

## Módulos Relacionados

- Skill: `skills/number-to-management-story.md`
- Template: `templates/variance-analysis-one-pager.md`
- Pattern: `_method-wiki/patterns/variance-analysis.md`
- Processo: `_method-wiki/processes/dashboard-and-kpi-design.md`
- Workflow: `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md`
