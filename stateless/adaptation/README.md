# Contrato do adapter stateless

> Status: `MVP fechado`.
> Revisado em: `2026-09-26`.

## Interface externa

O pacote foi desenhado para uma interação sem repositório, sem memória
persistente e com limite de anexos:

1. anexe `operating-manuals/general-analysis-manual.md`;
2. anexe `core-lenses/accounting-ops-core-lens.md` ou um `company-pack`;
3. cole `prompt-templates/analyze-material-base.md` e preencha a tarefa;
4. use no máximo uma lente adicional, sem ultrapassar dois anexos;
5. aplique `output-modes/executive-summary-mode.md` quando a audiência pedir
   síntese executiva.

O segundo anexo pode ser substituído por uma lente específica quando o caso já
trouxer o contexto geral necessário. O contexto da tarefa sempre fica no
prompt, não em um arquivo fixo.

## Pacote mantido

| Papel | Artefato | Função |
|---|---|---|
| comportamento | `operating-manuals/general-analysis-manual.md` | regras gerais de análise |
| lente central | `core-lenses/accounting-ops-core-lens.md` | leitura de número e performance |
| contexto situado | `company-packs/<company-pack>.md` | contexto comprimido da companhia analisada |
| lente de comunicação | `analytical-lenses/presentation-critique.md` | crítica de apresentações |
| lente de variação | `analytical-lenses/variance-analysis.md` | leitura compacta de Variance |
| lente de forecast | `analytical-lenses/forecast-review.md` | revisão de outlook e cenários |
| lente de narrativa | `analytical-lenses/executive-storyline.md` | adaptação para comunicação executiva |
| modo de saída | `output-modes/executive-summary-mode.md` | formato de resumo acionável |
| prompt | `prompt-templates/analyze-material-base.md` | instrução curta de execução |

## Fonte mestra e rastreabilidade

Os artefatos desta pasta são derivados. A regra é corrigir primeiro a fonte
mestra quando a lógica mudar e só depois atualizar a compressão correspondente.

| Artefato derivado | Fonte mestra | Atualizar quando |
|---|---|---|
| Manual geral | `CLAUDE.md`, `README.md` e `HEALTH_CHECK.md` | mudar guardrail geral, papel do produto ou critério de qualidade |
| Lente central | `domain.md`, `_method-wiki/patterns/variance-analysis.md` e `skills/explain-variance/SKILL.md` | mudar a sequência de leitura ou o contrato canônico |
| pack de companhia | `context/companies/company-slug/README.md` | mudar fato, driver ou limite do contexto da companhia |
| Crítica de apresentação | `tracks/fpa/playbooks/financial-information-communication.md` e `_method-wiki/processes/management-reporting-and-report-governance.md` | mudar critérios de comunicação ou governança do report |
| Lente de Variance | `skills/explain-variance/SKILL.md` e `skills/challenge-variance-explanation/SKILL.md` | mudar baseline, evidência, reconciliação, recorrência ou challenge |
| Lente de Forecast | `_method-wiki/checklists/financial-projection-quality-checklist.md` e `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md` | mudar premissas, cenários, drivers ou visão financeira |
| Lente de narrativa | `skills/number-to-management-story/SKILL.md` e `tracks/fpa/playbooks/financial-information-communication.md` | mudar headline, audiência, densidade ou ressalvas |
| Resumo executivo | `skills/number-to-management-story/SKILL.md` | mudar blocos obrigatórios ou gate de saída |
| Prompt base | contrato desta camada e `CLAUDE.md` | mudar número de anexos, ordem de uso ou regras de execução |

## Política de atualização

- A revisão registrada nesta versão é `2026-09-26`.
- Quando uma fonte mestra mudar, compare o artefato derivado antes de usá-lo
  em uma sessão stateless.
- Se a mudança alterar comportamento, evidência exigida, formato ou guardrail,
  atualize o derivado e a data desta nota.
- Se a mudança for apenas editorial e não alterar a instrução, registre a
  decisão no histórico da alteração sem duplicar a regra.
- Não crie uma regra local para compensar uma fonte mestra desatualizada.

## Critérios de aceitação

O adapter está saudável quando:

- dois anexos e um prompt bastam para iniciar a análise;
- a lente opcional muda o foco sem reescrever o método central;
- o resumo preserva fato, hipótese, impacto, ação e lacuna;
- cada artefato aponta para a fonte mestra e para sua condição de atualização;
- o pacote funciona sozinho sem exigir carregamento do repositório inteiro.

O adapter não deve:

- duplicar a implementação dos contratos executáveis;
- transformar contexto de uma companhia em método geral;
- prometer lentes ou modos que não existem;
- usar atualização manual como justificativa para divergência conhecida.
