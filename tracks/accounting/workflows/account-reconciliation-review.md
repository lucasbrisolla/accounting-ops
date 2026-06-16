# Workflow -- Revisão de Reconciliação de Contas

## Quando usar

Use este workflow quando o usuário pedir:

- revisar uma conciliação contábil
- explicar diferença entre razão e subledger
- classificar pendências de reconciliação
- avaliar se uma conta está pronta para fechamento
- definir ajustes, investigação ou escalonamento

## Objetivo

Transformar uma conciliação em conclusão de fechamento:

1. a conta está reconciliada?
2. o que explica a diferença?
3. o que precisa de ajuste?
4. o que precisa de investigação?
5. existe risco para resultado, caixa ou capital de giro?

## Entradas esperadas

Sempre que possível, trabalhar com:

- saldo do razão
- relatório auxiliar ou extrato
- composição da conta
- lista de itens conciliatórios
- aging dos itens
- histórico de pendências
- materialidade
- responsável da conta
- lançamentos manuais relevantes

## Sequência de trabalho

### 1. Definir a conta e a fonte de comparação

Confirmar:

- conta ou grupo de contas
- período
- fonte do saldo contábil
- fonte auxiliar ou externa
- unidade, entidade ou centro de custo

### 2. Reconciliar o saldo

Comparar:

- saldo razão
- saldo auxiliar
- diferença bruta
- diferença explicada
- diferença residual

Se a diferença residual não for zero ou imaterial, não tratar como conta limpa.

### 3. Classificar cada item

Classificar como:

- timing
- ajuste necessário
- investigação

Para cada item, registrar valor, idade, causa provável, owner e próxima ação.

### 4. Testar aging e recorrência

Perguntar:

- o item deveria ter limpado no ciclo normal?
- apareceu em meses anteriores?
- está crescendo?
- depende de outra área?
- virou pendência carregada sem plano?

### 5. Avaliar necessidade de lançamento

Se houver ajuste necessário, usar `skills/prepare-journal-entry-support.md` para estruturar:

- débito e crédito
- suporte
- memo
- reversão, quando aplicável
- revisão e aprovação

### 6. Concluir status da conta

Classificar:

- reconciliada
- reconciliada com pendências monitoradas
- não reconciliada
- bloqueada por dado ausente

### 7. Fechar leitura gerencial

Conectar a conclusão com:

- resultado
- caixa
- capital de giro
- qualidade do fechamento
- risco de processo

## Estrutura de saída sugerida

1. Status da reconciliação.
2. Diferença total e diferença residual.
3. Itens conciliatórios por categoria.
4. Aging e recorrência.
5. Ajustes necessários.
6. Risco para fechamento ou leitura gerencial.
7. Próximas ações, owners e prazos.

## Red flags

- saldo bate por compensação de erros
- diferença antiga sem escalonamento
- item classificado como timing sem data esperada de limpeza
- ajuste manual sem suporte
- subledger não confiável
- conta controle movimentada diretamente sem justificativa
- reconciliação concluída sem revisão de composição

## Guardrails

- Não concluir que a conta está reconciliada só porque a diferença é pequena.
- Não tratar item antigo como rotina normal sem investigação.
- Não propor ajuste sem indicar evidência e racional.
- Se faltar fonte auxiliar, declarar a limitação.
- Se a diferença afetar performance, separar efeito contábil de efeito operacional.
