# Checklist de Drivers de Receita e Margem Bruta

Checklist para revisar se crescimento de receita, projeção comercial e margem bruta estão sustentados por drivers reais.

Fonte principal: Jack Alexander, *Financial Planning, Analysis, and Performance Management*, Cap. 15.

## Quando Usar

- projeção de receita, forecast comercial ou plano de vendas
- análise de crescimento orgânico
- revisão de margem bruta, preço, mix, volume ou custo
- discussão sobre força de preço, descontos ou pressão competitiva
- dashboard de receita, inovação, margem ou pricing strength

## Ideia Central

Receita e margem bruta não devem ser lidas como totais agregados.

Receita precisa ser aberta por mercado, share, volume, preço, mix, novos produtos, clientes, região e reação competitiva. Margem bruta precisa ser aberta por preço, desconto, mix, custo, qualidade, perdas e eficiência operacional.

## Checklist

### 1. Natureza do Crescimento

- [ ] O crescimento foi separado entre orgânico e adquirido.
- [ ] O crescimento orgânico foi separado entre crescimento de mercado, ganho de share e entrada em novos mercados.
- [ ] O plano explicita se a empresa está surfando mercado forte ou ganhando posição competitiva.
- [ ] A projeção mostra de quem o share será ganho quando o crescimento superar o mercado.
- [ ] A reação dos concorrentes foi considerada.

### 2. Visões de Receita

- [ ] Receita foi aberta por produto ou linha.
- [ ] Receita foi aberta por cliente ou concentração relevante.
- [ ] Receita foi aberta por região, canal ou mercado quando aplicável.
- [ ] Receita foi aberta entre produtos existentes e novos produtos.
- [ ] Produtos em declínio por ciclo de vida foram separados de produtos em crescimento.
- [ ] A projeção mostra impactos negativos, não apenas novas fontes de crescimento.

### 3. Forecast Comercial

- [ ] A filosofia do forecast está clara: base 50/50, mais conservadora ou mais agressiva.
- [ ] O cenário base representa resultado mais provável.
- [ ] Upsides e downsides foram identificados.
- [ ] Upsides e downsides com alta probabilidade foram incorporados ao base case.
- [ ] A efetividade histórica do forecast comercial foi medida.
- [ ] O forecast do restante do ano foi comparado contra YTD, ano anterior e plano.
- [ ] A projeção não exige aceleração sem pipeline, backlog, preço, share ou capacidade que a sustente.

### 4. Premissas Comerciais Críticas

- [ ] Tamanho e crescimento de mercado estão explícitos.
- [ ] Market share atual e projetado estão explícitos.
- [ ] Preço e ASP estão explícitos.
- [ ] Mix de produto, cliente, geografia ou canal está explícito.
- [ ] Descontos, rebates ou concessões foram considerados.
- [ ] Novos produtos têm cronograma, adoção esperada e risco de atraso.
- [ ] Produtos maduros ou em declínio têm curva realista.
- [ ] Fatores macroeconômicos relevantes foram considerados.

### 5. Indicadores Líderes de Receita

- [ ] Pipeline, backlog ou carteira foram considerados.
- [ ] Pedidos perdidos foram analisados por motivo.
- [ ] Pedidos perdidos por preço foram separados.
- [ ] On-time delivery, qualidade, devoluções ou past-due orders foram considerados quando afetam receita.
- [ ] Satisfação, retenção, churn ou expansão em clientes existentes foram considerados quando disponíveis.
- [ ] Indicadores de lançamento de novos produtos foram acompanhados.

### 6. Margem Bruta

- [ ] Margem foi reconciliada em valor e percentual.
- [ ] Efeito volume foi separado.
- [ ] Efeito preço foi separado.
- [ ] Efeito mix foi separado.
- [ ] Efeito descontos foi separado quando relevante.
- [ ] Efeito custo de insumo, mão de obra ou produção foi separado.
- [ ] Efeito qualidade, scrap, rework, warranty ou variância foi separado.
- [ ] Câmbio ou efeitos externos relevantes foram separados.

### 7. Força de Preço vs. Eficiência

- [ ] ASP foi acompanhado ao longo do tempo.
- [ ] Descontos como percentual do preço de lista foram acompanhados.
- [ ] Market share foi lido junto com preço.
- [ ] Pedidos perdidos por preço foram monitorados.
- [ ] Comparação de preço/performance contra concorrentes foi considerada.
- [ ] Margem alta não foi tratada automaticamente como eficiência operacional.
- [ ] Foi testado se a operação continuaria saudável caso o prêmio de preço diminuísse.

## Perguntas de Challenge

1. A receita cresceu porque o mercado cresceu, porque ganhamos share ou porque entramos em novo mercado?
2. Se o crescimento projetado supera o mercado, de quem estamos tomando share e por quê?
3. A projeção considera produtos que vão cair, ou só produtos que vão crescer?
4. O forecast restante do ano exige performance muito melhor que o YTD?
5. A margem melhorou por preço, mix, custo ou efeito temporário?
6. Desconto crescente está sendo mascarado por receita nominal maior?
7. Estamos perdendo pedidos por preço enquanto preservamos ASP?
8. A margem forte vem de vantagem competitiva ou de operação eficiente?

## Sinais de Alerta

- crescimento projetado acima do mercado sem tese de share
- forecast comercial sempre otimista e sem medição de erro
- novos produtos usados como plug para fechar meta
- perda de receita por ciclo de vida ignorada
- pedidos perdidos por preço aumentando
- ASP caindo e desconto subindo ao mesmo tempo
- market share caindo com margem ainda alta
- margem explicada por "preço/mix" sem separação real
- custo, qualidade ou rework escondidos dentro de COGS agregado

## Saída Recomendada

```markdown
## Receita

Tese: [crescimento/queda explicado por mercado, share, preço, mix, cliente, produto ou região]

| Driver | Evidência | Impacto | Risco / monitoramento |
|---|---|---:|---|
| [driver] | [evidência] | [valor/%] | [risco ou indicador] |

## Margem Bruta

Tese: [expansão/erosão explicada por preço, mix, custo, desconto ou eficiência]

| Fator | Impacto | Natureza | Recorrência | Ação |
|---|---:|---|---|---|
| [fator] | [valor/%] | [comercial/custo/operacional] | [pontual/recorrente] | [ação] |

## Indicadores Líderes

- [indicador 1]
- [indicador 2]
- [indicador 3]
```

## Módulos Relacionados

- Workflow: `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md`
- Workflow: `tracks/fpa/workflows/gross-margin-bridge.md`
- Pattern: `patterns/gross-margin-bridge.md`
- Conceito: `concepts/pricing-strength-vs-operating-efficiency.md`
- Heuristic: `heuristics/margin-erosion-signals.md`
- Processo: `processes/dashboard-and-kpi-design.md`
