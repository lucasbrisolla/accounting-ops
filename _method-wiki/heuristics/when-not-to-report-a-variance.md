# Heuristic: When Not to Report a Variance

## Ideia central

Nem toda variância merece destaque.

Variance reporting só ajuda quando a diferença é relevante, explicável e potencialmente acionável.

## Quando segurar ou reduzir destaque

### 1. Standard ruim ou meta politizada

Se o baseline já nasceu fraco, a variância pode parecer precisa e continuar inútil.

### 2. Feedback tarde demais

Se a variação chega quando não há mais tempo de agir, ela pode servir para aprendizado, mas não merece o mesmo tratamento de uma exceção acionável.

### 3. Variância sem hipótese de causa

Número isolado sem leitura mínima de driver só consome atenção.

### 4. Variância irrelevante

Desvio pequeno, recorrente e sem impacto decisório não deve dominar o report principal.

### 5. Variância que já está capturada por métrica melhor

Às vezes o indicador líder ou a exceção operacional explicam melhor o risco do que a comparação formal contra budget.

## Quando reportar mesmo assim

- materialidade alta
- risco crescente
- sinal de deterioração estrutural
- recorrência que aponta falha de processo
- desvio pequeno hoje, mas com efeito composto relevante

## Perguntas rápidas

1. Essa variância muda decisão?
2. Existe dono que pode agir?
3. O baseline faz sentido?
4. Temos ao menos uma hipótese razoável de causa?

## Guardrails

- Não usar a heurística para esconder problema real.
- Não confundir pouca relevância com pouco conforto.
- Se a variância não entra no report principal, ela ainda pode entrar no material de suporte.

## Conexões operacionais

- Pattern: `patterns/variance-analysis.md`
- Process: `processes/management-reporting-and-report-governance.md`
- Workflow: `tracks/fpa/workflows/gross-margin-bridge.md`

## Fonte

Destilado de Steven Bragg, *The New Controller Guidebook*, Cap. 14.
