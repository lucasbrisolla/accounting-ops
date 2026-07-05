# Workflow -- Custo Padrão e Variâncias Industriais

## Quando usar

Use este workflow quando o usuário pedir:

- revisão de custo padrão
- explicação de variâncias de materiais, mão de obra ou overhead
- análise de padrão versus custo real
- impacto de variâncias em estoque, CPV e margem
- revisão de padrões desatualizados
- investigação de eficiência industrial, scrap ou absorção

## Objetivo

Transformar standard costing em benchmark operacional útil, sem confundir variância favorável com boa performance ou padrão desatualizado com eficiência.

O workflow responde:

1. o padrão é válido e atingível?
2. a diferença está em preço, quantidade, rate, eficiência, spending ou volume?
3. a variância é material, acionável e tempestiva?
4. existe comportamento induzido pelo KPI que piora estoque, fluxo ou economia total?
5. como a diferença afeta estoque, CPV, margem e decisão?

## Princípio central

Variância só é informativa quando o padrão é confiável.

O custo padrão deve funcionar como aproximação e benchmark, não como verdade econômica permanente.

## Entradas esperadas

- item master e bill of materials
- roteiros, tempos e taxas padrão
- custos reais de materiais, mão de obra e overhead
- volumes produzidos e vendidos
- scrap, spoilage, rework e yield
- horas reais e padrão
- capacidade e utilização
- critérios de overhead
- histórico e data de atualização dos padrões
- estoque, CPV e contas de variância
- explicações operacionais por planta, linha, célula ou lote

## Sequência de trabalho

### 1. Definir a finalidade do padrão

Confirmar se ele é usado para:

- orçamento
- valuation de estoque
- aplicação de overhead
- formação de preço
- controle de eficiência
- process costing

A precisão necessária depende da decisão. Aproximação aceitável para orçamento pode ser insuficiente para contrato cost-plus ou valuation material.

### 2. Validar a base do padrão

Classificar:

| Base | Característica | Leitura |
|---|---|---|
| Histórica | Replica média recente | Atingível, mas incorpora ineficiências |
| Atingível | Inclui melhoria realista | Referência preferencial para gestão |
| Teórica | Pressupõe operação perfeita | Gera desfavoráveis crônicas e pouca credibilidade |

Testar se o padrão considera:

- idade e eficiência dos equipamentos
- setup e tamanho de lote
- mudanças de automação e mão de obra
- reajustes salariais
- curva de aprendizado
- termos, fornecedores e volumes de compra
- qualidade do material e scrap esperado
- fluxo push ou pull

### 3. Verificar governança e atualização

Confirmar:

- owner do padrão
- participação de engenharia, compras, produção e accounting
- data da última revisão
- gatilhos de atualização
- controle de versão e data efetiva
- foco mais frequente nos itens de maior valor

Padrão antigo em ambiente de custo volátil transforma toda análise posterior em ruído.

### 4. Abrir as variâncias

| Bloco | Variância | Pergunta |
|---|---|---|
| Materiais | preço de compra | Pagamos diferente do padrão por mercado, fornecedor, volume, urgência ou frete? |
| Materiais | uso ou yield | Consumimos mais por scrap, qualidade, setup, armazenamento ou BOM? |
| Mão de obra | rate | O mix de função, hora extra ou taxa salarial mudou? |
| Mão de obra | eficiência | Foram necessárias mais horas por treinamento, falta de material, setup ou capacidade? |
| Overhead variável | spending | A taxa real mudou por preço, classificação ou outsourcing? |
| Overhead variável | eficiência | A base de atividade consumida divergiu do padrão? |
| Overhead fixo | spending | O gasto fixo real divergiu do orçamento? |
| Overhead fixo | volume/absorção | A produção e utilização absorveram o custo fixo esperado? |

### 5. Testar causa operacional

O ledger localiza o desvio, mas raramente prova a causa.

Buscar evidência em:

- máquina, linha, célula ou lote
- setup e downtime
- falta ou substituição de material
- qualidade e inspeção
- overtime e mix de mão de obra
- compras urgentes e frete especial
- capacidade, volume e sequência de produção
- mudança de fornecedor ou especificação

### 6. Testar comportamento induzido

Uma variância favorável pode ser economicamente ruim.

Exemplos:

- compra em lote maior melhora preço, mas aumenta estoque e risco de obsolescência
- produção longa melhora eficiência, mas cria excesso e piora fluxo
- scrap embutido no padrão normaliza perda evitável
- absorção favorável nasce de produção sem demanda
- postergação de manutenção reduz gasto hoje e eleva risco futuro

### 7. Priorizar variâncias acionáveis

Reportar principalmente quando houver:

- materialidade
- padrão confiável
- causa minimamente identificada
- owner capaz de agir
- feedback ainda tempestivo
- desvio relevante contra a tendência

Não reportar toda a suíte apenas porque o sistema calcula.

### 8. Revisar tratamento contábil

Avaliar, conforme materialidade e framework aplicável:

- variância reconhecida no CPV do período
- variância alocada entre estoque e CPV
- atualização do padrão para aproximá-lo do custo real
- separação entre erro, ineficiência anormal e diferença normal

Evitar carregar estoque a padrão materialmente distante do custo real.

### 9. Fechar narrativa e ação

Para cada variação relevante, registrar:

- valor e direção
- padrão usado
- causa operacional
- efeito em estoque, CPV e margem
- recorrência
- owner
- ação e prazo
- necessidade de atualizar o padrão

## Estrutura de saída sugerida

1. Validade e idade dos padrões.
2. Variâncias materiais por bloco.
3. Causas operacionais confirmadas e hipóteses.
4. Efeitos econômicos escondidos por variâncias favoráveis.
5. Tratamento em estoque, CPV e margem.
6. Ações, owners e atualização de padrões.

## Red flags

- padrão teórico vendido como meta operacional realista
- padrão sem revisão em ambiente volátil
- variância agregada sem drill-down operacional
- feedback produzido somente depois de encerrado o período
- compra excessiva para gerar preço favorável
- produção excessiva para gerar eficiência ou absorção favorável
- scrap permanente incorporado ao padrão sem plano de redução
- todas as variâncias lançadas no CPV sem teste de materialidade
- estoque material valorizado por padrão distante do custo real

## Guardrails

- Não concluir que favorável significa bom ou desfavorável significa ruim.
- Não usar standard costing em contrato que exige custo real.
- Não atribuir causa operacional apenas com dados contábeis agregados.
- Não manter padrões politizados ou impossíveis como baseline.
- Não confundir variância de preço com eficiência de consumo.
- Usar `_method-wiki/patterns/variance-analysis.md` para estruturar a narrativa.
- Usar `inventory-and-valuation-review.md` quando o desvio afetar valuation.
- Usar `process-costing-and-wip-review.md` quando o padrão for aplicado a produção contínua.

## Fonte de promoção

- Steven Bragg, *Cost Accounting Fundamentals*, Cap. 7 — Standard Costing.
