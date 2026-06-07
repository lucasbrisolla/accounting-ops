# Margin Reporting Without Bad Allocations

Playbook para desenhar reports de margem sem deprimir artificialmente o resultado por alocações ruins.

Fonte principal: Steven Bragg, *The New Controller Guidebook*, Cap. 14.

## Princípio central

Para avaliar margem de um objeto específico, priorizar custos que desapareceriam se esse objeto deixasse de existir.

## Quando usar

- margem por produto
- margem por cliente
- margem por linha
- margem por unidade ou loja

## Perguntas centrais

- este custo é atribuível ou apenas repartido?
- ele desaparece se o objeto analisado sair?
- a alocação ajuda a decidir ou apenas “completa” o número?

## Custos que frequentemente fazem sentido

- matéria-prima
- frete diretamente associado
- comissão ligada à venda
- descontos e deductions específicos
- mão de obra ou custo direto claramente rastreável

## Custos que pedem mais cuidado

- overhead compartilhado
- estrutura corporativa
- despesas de suporte sem causalidade clara
- rateios feitos apenas por convenção

## Risco clássico

Rateio excessivo pode fazer produto, cliente ou unidade parecer economicamente pior do que realmente é, levando a decisão errada.

## Guardrails

- Não tratar toda alocação como proibida.
- Não chamar de margem “real” um número que omite custo material e atribuível.
- Explicitar a lógica do recorte usado.

## Módulos relacionados

- Pattern: `_method-wiki/patterns/responsibility-reporting.md`
- Pattern: `_method-wiki/patterns/gross-margin-bridge.md`
- Workflow: `tracks/fpa/workflows/gross-margin-bridge.md`

