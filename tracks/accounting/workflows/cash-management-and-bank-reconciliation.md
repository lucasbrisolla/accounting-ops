# Workflow -- Gestão de Caixa e Reconciliação Bancária

## Quando usar

Use este workflow quando o usuário pedir:

- apoio para reconciliação bancária
- revisão de saldo de caixa e bancos
- análise de pendências, trânsito ou diferenças de conciliação
- leitura de risco de liquidez no curto prazo
- ponte entre fechamento, capital de giro e caixa disponível

## Objetivo

Transformar a reconciliação de caixa e bancos em leitura confiável de liquidez e disciplina financeira.

O workflow existe para responder, em ordem:

1. o saldo de caixa e bancos está confiável?
2. quais itens em aberto ou diferenças ainda contaminam a leitura?
3. existe sinal de pressão de capital de giro ou risco de liquidez?
4. o que a gestão precisa monitorar ou decidir agora?

## Entradas esperadas

Sempre que possível, trabalhar com algum destes insumos:

- razão de bancos
- extratos bancários
- reconciliações do período
- listagem de itens pendentes
- previsão de entradas e saídas imediatas
- contas a receber e contas a pagar de curto prazo
- memória de fechamento
- explicação de cheques, tarifas, bloqueios, adiantamentos ou transferências em trânsito

## Sequência de trabalho

### 1. Definir o recorte da revisão

Antes de revisar, confirmar:

- período de corte
- contas bancárias e entidades incluídas
- saldo contábil versus saldo bancário
- visão desejada: fechamento, posição diária ou leitura gerencial de liquidez

### 2. Validar a reconciliação base

Para cada conta relevante, confirmar:

- saldo no extrato
- saldo no razão
- diferenças mapeadas
- itens em trânsito identificados
- pendências antigas separadas de movimentos normais do período

### 3. Investigar diferenças e itens em aberto

Perguntas obrigatórias:

- a diferença é timing legítimo ou erro?
- existe item antigo sem baixa ou sem explicação plausível?
- houve lançamento manual relevante no caixa ou banco?
- há compensação indevida entre contas ou datas?
- existe bloqueio, restrição ou saldo indisponível tratado como disponível?

### 4. Ler o efeito em liquidez e capital de giro

Depois da reconciliação, avaliar:

- pressão de saídas no curtíssimo prazo
- concentração de recebimentos ou pagamentos
- dependência de entrada ainda não confirmada
- impacto de atrasos, inadimplência ou desembolsos extraordinários

### 5. Fechar com mensagem gerencial

Responder:

- se o saldo está confiável ou ainda provisório
- quais pendências mudam a leitura
- qual o principal risco de liquidez no curto prazo
- quais ações precisam de acompanhamento imediato

## Estrutura de saída sugerida

1. Resumo executivo da posição de caixa e bancos.
2. Diferenças de reconciliação e status.
3. Itens em aberto com maior impacto.
4. Leitura de liquidez e capital de giro.
5. Ações de acompanhamento e responsáveis.

## Red flags

- reconciliação fechada apenas “por diferença”
- item antigo reaparecendo mês após mês
- saldo bancário indisponível tratado como caixa livre
- lançamentos manuais relevantes sem trilha clara
- previsão de liquidez apoiada em recebimento incerto

## Guardrails

- Não tratar reconciliação como tarefa mecânica sem leitura financeira.
- Não confundir diferença de timing com erro definitivo sem evidência.
- Não tratar caixa contábil como liquidez real sem olhar disponibilidade.
- Se houver limitação de extrato, corte ou suporte, declarar a fragilidade da leitura.
