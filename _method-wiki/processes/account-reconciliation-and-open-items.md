# Processo: Reconciliação de Contas e Pendências em Aberto

## Papel

Hub metodológico para revisar conciliações, diferenças entre razão e fontes auxiliares, itens pendentes e qualidade das contas patrimoniais.

Reconciliação boa não é apenas "bater saldo". Ela precisa explicar diferenças, classificar pendências, definir owner e evitar que itens antigos virem ruído permanente no fechamento.

## Quando usar

Use este processo quando a pergunta envolver:

- conciliação contábil
- razão versus subledger
- conciliação bancária
- intercompany
- pendências antigas
- diferenças não identificadas
- qualidade de contas patrimoniais antes do fechamento

## Tipos comuns de reconciliação

### Razão versus subledger

Comparar conta controle no razão com relatório auxiliar.

Exemplos:

- contas a receber versus aging de clientes
- contas a pagar versus aging de fornecedores
- estoque versus relatório de valuation
- imobilizado versus razão auxiliar de ativos
- prepaids versus cronograma de amortização
- accruals versus memória de provisões

### Conciliação bancária

Comparar saldo contábil de caixa com extrato bancário, separando:

- cheques ou pagamentos emitidos e não compensados
- depósitos em trânsito
- tarifas, juros e ajustes bancários não registrados
- erros de banco ou de registro contábil

### Intercompany

Comparar saldos entre entidades relacionadas.

Diferenças comuns:

- uma entidade registrou e a outra não
- câmbio diferente
- classificação diferente
- corte de período divergente
- pagamento não aplicado

## Sequência recomendada

### 1. Definir escopo e fonte

Confirmar:

- conta ou grupo de contas
- período-base
- saldo do razão
- fonte auxiliar ou externa
- materialidade
- owner da conta

### 2. Comparar saldos

Apurar:

- saldo contábil
- saldo auxiliar ou externo
- diferença total
- diferenças conhecidas
- diferença ainda sem explicação

### 3. Classificar itens conciliatórios

Separar as pendências em três grupos.

| Categoria | O que significa | Ação esperada |
|---|---|---|
| Timing | Diferença normal de processamento ou corte. | Monitorar até limpar no ciclo esperado. |
| Ajuste necessário | Erro, despesa bancária, juros, classificação ou lançamento faltante. | Preparar ajuste ou correção. |
| Investigação | Diferença sem causa clara, disputa, item antigo ou recorrente. | Definir owner, prazo e escalonamento. |

### 4. Fazer aging das pendências

Não carregar item em aberto sem idade e plano.

Buckets úteis:

- 0-30 dias: dentro do ciclo normal
- 31-60 dias: investigar
- 61-90 dias: escalar
- mais de 90 dias: revisar risco de ajuste, baixa, write-off ou falha de processo

### 5. Definir owner e próximo passo

Cada item material precisa ter:

- responsável
- data de origem
- causa provável
- ação esperada
- prazo de resolução

### 6. Avaliar impacto no fechamento

Perguntar:

- a conta pode ser considerada reconciliada?
- a diferença muda resultado, caixa, margem ou capital de giro?
- a pendência é erro isolado ou sinal de falha de processo?
- existe risco de repetir no próximo fechamento?

## Thresholds e escalonamento

Defina thresholds conforme materialidade da empresa, mas use a lógica:

- diferença individual relevante vai para revisão do responsável da conta
- diferença total relevante vai para controller ou liderança financeira
- item antigo vai para escalonamento mesmo que o valor não seja enorme
- diferença sem explicação não deve ser empurrada indefinidamente

## Saída recomendada

```markdown
## Resumo da Reconciliação

- Conta:
- Período:
- Saldo razão:
- Saldo fonte auxiliar:
- Diferença total:
- Diferença explicada:
- Diferença em aberto:

## Itens Conciliatórios

| Item | Valor | Categoria | Idade | Causa provável | Owner | Próxima ação |
|---|---:|---|---:|---|---|---|
| [item] | [valor] | [timing/ajuste/investigação] | [dias] | [causa] | [owner] | [ação] |

## Conclusão

[conta reconciliada, reconciliada com pendência, ou não reconciliada]

## Risco e Próximo Passo

[impacto em resultado, caixa, fechamento ou processo]
```

## Red flags

- diferença sem explicação tratada como timing
- item antigo carregado mês após mês
- lançamento manual direto na conta controle sem reflexo no subledger
- reconciliação feita sem fonte auxiliar confiável
- saldo reconciliado no total, mas com composição errada
- pendência sem owner
- conta patrimonial com efeito em resultado sem revisão suficiente

## Módulos relacionados

- Processo: `processes/monthly-closing-and-number-quality.md`
- Checklist: `checklists/monthly-closing-number-quality-checklist.md`
- Workflow: `tracks/accounting/workflows/account-reconciliation-review.md`
- Workflow: `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md`
- Workflow: `tracks/accounting/workflows/working-capital-and-cash-conversion-review.md`
- Skill: `skills/prepare-journal-entry-support.md`

## Fonte

Adaptado da leitura do plugin `knowledge-work-plugins/finance`, skill `reconciliation`, e calibrado para a arquitetura do `accounting-ops`.
