# Revisão de Despesas Operacionais e Efetividade

Fonte principal: Jack Alexander, *Financial Planning, Analysis, and Performance Management*, Cap. 16.

## Quando usar

- pressão de SG&A sem explicação convincente
- dúvida se a margem depende de eficiência real ou de `pricing strength`
- crescimento de headcount, estrutura ou overhead sem clareza sobre retorno
- revenue concentrada no fim do período, com custo, risco ou retrabalho crescentes
- baixa conversão de lucro em caixa por falhas operacionais
- comparável ou empresa analisada defendendo forte ganho de eficiência
- necessidade de separar despesa estrutural do modelo de ineficiência operacional

## Princípio central

`SG&A % da receita` não explica uma operação.

Despesa operacional precisa ser lida como consequência de modelo de negócio, processo, qualidade, forecasting, flexibilidade e disciplina de execução. Margem forte pode coexistir com operação ruim se a empresa ainda consegue repassar custo via preço. O objetivo deste playbook é descobrir se o custo é estrutural, transitório, investimento deliberado ou falha operacional.

## Sequência prática

### 1. Clarificar o problema econômico principal

Perguntar:

- a preocupação é margem, caixa, crescimento, qualidade, velocidade, headcount ou risco?
- a empresa está gastando demais ou executando mal?
- o problema está em custo recorrente, pico pontual, complexidade crescente ou investimento para crescer?

Sem essa pergunta, a revisão de despesas vira caça a linha contábil.

### 2. Separar estrutura do modelo de ineficiência

Antes de concluir que o custo está alto, testar:

- o canal exige estrutura comercial pesada?
- o nível de serviço ou customização exige mais pessoas?
- a empresa é verticalizada onde o comparável é asset-light ou terceiriza?
- o negócio está investindo em crescimento, inovação ou implantação?

Nem todo custo alto é ineficiência. Parte dele pode ser consequência do modelo econômico escolhido.

### 3. Testar se a margem está escondendo custo ruim

Perguntar:

- a empresa sustenta preço por diferenciação real?
- descontos, share ou pedidos perdidos contradizem a tese de força de preço?
- se o prêmio de preço desaparecer, a operação continua saudável?

Use como complemento:

- `_method-wiki/concepts/pricing-strength-vs-operating-efficiency.md`
- `tracks/fpa/playbooks/pricing-strength-vs-operating-efficiency.md`

### 4. Sair da linha da DRE e ir para o processo

Ler despesa por processo crítico, não apenas por função:

- revenue process: pedido, faturamento, entrega, cobrança
- supply chain: planejamento, compras, produção, lead time, fornecedores
- desenvolvimento de produto: prazo, custo, yield, retrabalho, ECNs
- qualidade: scrap, rework, devolução, garantia, correção
- planejamento: forecast accuracy, expediting, ociosidade, overtime

Se o processo for ruim, o custo costuma aparecer em mais de uma linha ao mesmo tempo.

### 5. Revisar flexibilidade operacional e padrões de receita

Sinais importantes:

- revenue `hockey stick` no fim do mês ou do trimestre
- forecast ruim gerando write-off, overtime, frete urgente ou excesso de estoque
- cycle time alto
- baixo first-time yield
- gargalos e handoffs que aumentam custo e erro

Efetividade operacional não é só gastar menos. É responder melhor com menos fricção.

### 6. Revisar pessoas, capacidade e estrutura

Olhar:

- headcount por área e sua tendência
- open requisitions, admissões e desligamentos
- custo de pessoal como percentual do custo total
- produtividade com contexto de business model
- utilização de pessoas ou capacidade quando isso fizer sentido

Guardrail:

`sales per employee` pode enganar muito em negócios com outsourcing, verticalização diferente ou mix distinto. Quando possível, preferir `value added per employee`.

### 7. Usar análise por natureza de despesa para priorizar o 80/20

Depois da leitura por processo, usar a visão por natureza para atacar materialidade:

- salários e encargos
- materiais comprados
- serviços terceiros
- viagens
- benefícios
- telecom
- aluguel
- depreciação

Essa leitura ajuda a priorizar onde realmente vale agir. Ela não substitui a visão por processo, mas evita discutir custo imaterial.

### 8. Fechar com implicação econômica

Toda conclusão deve responder:

- o que parece estrutural do modelo
- o que parece corrigível por execução
- o que parece investimento deliberado
- o que isso muda em margem, caixa, capital e risco

## Indicadores úteis com ressalvas

| Indicador | O que pode revelar | Onde engana |
|---|---|---|
| SG&A % da receita | Nível agregado de despesa comercial e administrativa | Diferença de canal, estágio, mix e investimento |
| R&D % da receita | Esforço de inovação e crescimento futuro | Pode confundir ineficiência com investimento deliberado |
| Sales per employee | Produtividade bruta | Outsourcing, verticalização e mix distorcem a comparação |
| Value added per employee | Produtividade ajustada | Exige boa leitura de custos externos |
| Revenue linearity | Pressão operacional e risco de fim de período | Parte da sazonalidade pode ser legítima |
| Forecast accuracy | Qualidade de planejamento e disciplina operacional | Pode culpar previsão por problema de execução |
| Invoice error rate | Fricção operacional que vira custo e DSO | Erros não detectados podem ficar fora |
| Cycle time | Flexibilidade, custo e estoque | Definição ruim da métrica atrapalha comparação |
| First-time yield | Eficiência e qualidade do processo | Pode esconder retrabalho fora do ponto medido |
| Headcount analysis | Leading indicator de custo estrutural | Não mostra sozinho produtividade nem valor gerado |
| Cost of quality failures | Custo escondido da má qualidade | Pode ficar incompleto se o escopo for estreito |
| Natural expense code analysis | Onde está o 80/20 do custo | Não mostra causalidade operacional sozinho |

## Sinais de alerta

- margem estável apesar de processo visivelmente fraco
- corte linear de custo apresentado como ganho de eficiência
- revenue concentrada no fim do período
- headcount crescendo sem efeito claro em throughput, qualidade ou serviço
- forecast ruim recorrente tratado como “normal do negócio”
- custo de qualidade espalhado e invisível
- muitos vendors, partes, exceções ou retrabalho sem dono claro
- empresa defendendo eficiência com uma métrica única
- comparável com SG&A menor, mas modelo claramente diferente

## Perguntas de challenge

1. O custo parece alto porque a empresa executa mal ou porque o modelo exige essa estrutura?
2. O ganho de margem vem de processo melhor ou de preço ainda favorável?
3. Que processo explica o custo: revenue, supply chain, NPD, qualidade ou planejamento?
4. O problema está em despesa recorrente, complexidade, baixa flexibilidade ou pico de fim de período?
5. O headcount adicional está entregando capacidade, qualidade ou crescimento mensurável?
6. O forecast ruim está contaminando custo, estoque, DSO ou nível de serviço?
7. A análise está olhando causa operacional ou apenas sintoma contábil?

## Estrutura de resposta sugerida

1. Explicar qual parte do custo parece estrutural, qual parte parece ineficiência e qual parte parece investimento deliberado.
2. Mostrar que processo ou alavanca operacional sustenta essa leitura.
3. Apontar os indicadores e evidências que confirmam ou negam a tese.
4. Fechar com impacto em margem, caixa, capital e risco.
5. Dizer o que precisa ser monitorado ou atacado em seguida.

## Módulos relacionados

- Concept: `_method-wiki/concepts/pricing-strength-vs-operating-efficiency.md`
- Concept: `_method-wiki/concepts/value-driver-framework.md`
- Playbook: `tracks/fpa/playbooks/pricing-strength-vs-operating-efficiency.md`
- Workflow: `tracks/accounting/workflows/working-capital-and-cash-conversion-review.md`
- Workflow: `tracks/accounting/workflows/inventory-and-valuation-review.md`
- Playbook: `tracks/fpa/playbooks/asset-utilization-and-capital-discipline.md`
