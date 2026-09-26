# Índice do Produto

Catálogo operacional único do `accounting-ops`.

Use este arquivo quando precisar localizar rapidamente trilhas, modos, playbooks, templates e exemplos.

## Entrada e arquitetura

| Arquivo | Papel |
|---|---|
| `README.md` | Visão geral, capacidades, limites e ponto de partida humano. |
| `CLAUDE.md` | Roteamento operacional e seleção de módulos para o agente. |
| `domain.md` | Mapa conceitual central do produto. |
| `CONTEXT.md` | Glossário da arquitetura de conhecimento. |
| `DATA_CONTRACT.md` | Fronteiras entre contexto situado, método e ingestão. |
| `HEALTH_CHECK.md` | Critérios para verificar a saúde estrutural e operacional. |
| `stateless/README.md` | Interface do pacote para ambientes sem repositório. |

## Governança do produto

| Arquivo | Quando usar |
|---|---|
| `scripts/accounting_ops_product_contract.py` | Consultar ou alterar a política versionada de camadas, caminhos esperados, referências, surface drift e critérios de promoção. |
| `scripts/accounting_ops_doctor.py` | Executar a verificação estrutural e renderizar findings do Product Contract em CLI. |
| `scripts/promotion_pipeline.py` | Criar, persistir e carregar decisões editoriais comuns para livros e contexto empresarial. |
| `tests/test_accounting_ops_product_contract.py` | Verificar a costura pública do contrato com fixtures de estrutura, referências e conteúdo situado. |
| `tests/test_promotion_pipeline.py` | Verificar invariantes, round-trip e limites de generalização das decisões de promoção. |

## Method Wiki

| Arquivo | Quando usar |
|---|---|
| `_method-wiki/README.md` | Entender o papel e a regra editorial da base metodológica viva. |
| `_method-wiki/index.md` | Navegar por concepts, heuristics, checklists, patterns e processes. |
| `_method-wiki/guide.md` | Encontrar o caminho metodológico por fase do trabalho ou situação. |
| `_method-wiki/concepts/budget-vs-forecast-vs-operating-plan.md` | Separar budget, operating plan e forecast / business outlook. |
| `_method-wiki/concepts/analytical-tools-foundations.md` | Escolher e usar ferramentas analíticas como Pareto, quartis, sensibilidade e cenários. |
| `_method-wiki/concepts/business-model-foundations.md` | Ler business model além da DRE, conectando crescimento, capital, caixa e retorno. |
| `_method-wiki/concepts/capital-intensity-foundations.md` | Entender intensidade de capital e suas implicações para retorno, CAPEX e caixa. |
| `_method-wiki/concepts/excess-cash-and-capital-drag.md` | Avaliar quando caixa alto deixa de ser proteção e vira diluição de retorno. |
| `_method-wiki/concepts/inventory-and-valuation-foundations.md` | Revisar fundamentos de estoque, valuation, giro, obsolescência e margem. |
| `_method-wiki/concepts/intangible-assets-and-goodwill-signals.md` | Interpretar goodwill, intangíveis e impairment como sinais gerenciais de alocação de capital. |
| `_method-wiki/concepts/number-quality-foundations.md` | Revisar fundamentos de qualidade do número antes de discutir performance. |
| `_method-wiki/concepts/operating-leverage-and-break-even.md` | Revisar CVP, contribuição, break-even, margem de segurança e sensibilidade de drivers com foco em risco operacional. |
| `_method-wiki/concepts/pricing-strength-vs-operating-efficiency.md` | Separar força de preço de eficiência operacional. |
| `_method-wiki/concepts/value-driver-framework.md` | Organizar a leitura integrada de performance por drivers de criação de valor. |
| `_method-wiki/concepts/working-capital-foundations.md` | Revisar fundamentos de capital de giro: caixa, recebíveis, estoque e contas a pagar. |
| `_method-wiki/heuristics/margin-erosion-signals.md` | Procurar sinais de erosão de margem e desafiar explicações superficiais. |
| `_method-wiki/heuristics/cost-opportunity-signals.md` | Identificar oportunidades acionáveis de custo, economia, waste, scrap, rework, consumo, owner e captura em margem ou caixa. |
| `_method-wiki/heuristics/when-not-to-report-a-variance.md` | Decidir quando uma variância não merece destaque principal no report. |
| `_method-wiki/checklists/forecast-review-checklist.md` | Revisar forecast, premissas, cenários e riscos de execução. |
| `_method-wiki/checklists/capital-investment-postaudit-checklist.md` | Revisar se um CAPEX entregou business case, utilização e aprendizado. |
| `_method-wiki/checklists/financial-projection-quality-checklist.md` | Revisar qualidade, premissas, tendência, cenários e uso gerencial de projeções financeiras. |
| `_method-wiki/checklists/monthly-closing-number-quality-checklist.md` | Revisar fechamento e qualidade do número antes do report. |
| `_method-wiki/checklists/revenue-and-gross-margin-driver-checklist.md` | Revisar drivers de receita, forecast comercial, margem bruta e força de preço. |
| `_method-wiki/checklists/working-capital-driver-checklist.md` | Revisar DSO, estoque, payables, capital preso e conversão de caixa. |
| `_method-wiki/patterns/gross-margin-bridge.md` | Estruturar bridge de margem bruta por drivers. |
| `_method-wiki/patterns/goal-to-driver-cascade.md` | Descer de objetivo estratégico até driver, KPI, meta e accountability. |
| `_method-wiki/patterns/performance-tree.md` | Decompor um KPI em drivers subordinados e comunicar causa, impacto e ação. |
| `_method-wiki/patterns/responsibility-reporting.md` | Ligar linha reportada, nível de agregação e owner do número. |
| `_method-wiki/patterns/variance-analysis.md` | Oferecer decomposições complementares para Variance; o contrato canônico está em `skills/explain-variance/SKILL.md`. |
| `_method-wiki/processes/account-reconciliation-and-open-items.md` | Revisar conciliações contábeis, diferenças, open items e necessidade de ajuste. |
| `_method-wiki/processes/dashboard-and-kpi-design.md` | Desenhar dashboards, KPIs, alertas e indicadores de performance ligados a drivers e decisão. |
| `_method-wiki/processes/forecasting-and-business-outlook.md` | Navegar o processo de forecast, business outlook e cenários. |
| `_method-wiki/processes/long-term-capital-management.md` | Navegar a disciplina de CAPEX, uso de ativos, caixa e retorno de longo prazo. |
| `_method-wiki/processes/management-reporting-and-report-governance.md` | Navegar governança de reports, núcleo vivo de reporting e racionalização de relatórios. |
| `_method-wiki/processes/monthly-closing-and-number-quality.md` | Navegar o processo de fechamento mensal e leitura gerencial do número. |
| `_method-wiki/processes/performance-management-framework.md` | Navegar a lógica de contexto, drivers, métricas, execução e accountability. |

## Trilhas

| Trilha | Papel |
|---|---|
| `tracks/fpa/` | Trilha atual mais madura, voltada a FP&A, análise de variações e performance. |
| `tracks/accounting/` | Trilha de accounting/controladoria, com foco inicial em fechamento, qualidade do número e impacto técnico-contábil no report gerencial. |

## Modos da trilha FP&A

| Arquivo | Quando usar |
|---|---|
| `tracks/fpa/modes/fpa-learning.md` | Explicar conceitos, desenvolver base e construir raciocínio sistêmico de FP&A. |
| `tracks/fpa/modes/variance-analysis.md` | Aplicar a lente de FP&A depois da decisão canônica em orçado vs. realizado, forecast vs. actual e bridges de variação. |

## Playbooks da trilha FP&A

| Arquivo | Quando usar |
|---|---|
| `tracks/fpa/playbooks/financial-information-communication.md` | Transformar análise financeira em mensagem executiva, apresentação ou report de gestão. |
| `tracks/fpa/playbooks/creating-context-for-performance-measures.md` | Criar contexto antes de escolher métricas, metas ou dashboards. |
| `tracks/fpa/playbooks/fpa-capability-assessment-and-improvement.md` | Avaliar capacidade de FP&A, racionalizar reports e modelos e montar plano de melhoria. |
| `tracks/fpa/playbooks/flash-report-design.md` | Desenhar ou criticar flash reports curtos e acionáveis. |
| `tracks/fpa/playbooks/margin-reporting-without-bad-allocations.md` | Desenhar reports de margem sem distorção por rateios ruins. |
| `tracks/fpa/playbooks/pricing-strength-vs-operating-efficiency.md` | Diferenciar margem forte por poder de preço de margem forte por eficiência operacional real. |
| `tracks/fpa/playbooks/operating-expense-and-effectiveness-review.md` | Revisar SG&A, produtividade, headcount, qualidade operacional e custo de processo sem depender de KPI decorativo. |
| `tracks/fpa/playbooks/long-term-projection-and-strategic-scenario-review.md` | Revisar projeções de longo prazo, guidance estratégico, alternativas de cenário, funding e criação de valor sem confundir ambição com plano financiável. |
| `tracks/fpa/playbooks/asset-utilization-and-capital-discipline.md` | Revisar ativos subutilizados, capital parado e disciplina econômica de longo prazo. |
| `tracks/fpa/playbooks/external-view-and-peer-benchmarking.md` | Ler mercado, clientes, concorrentes, adjacências e benchmarks antes de aceitar narrativa interna de performance. |

## Workflows da trilha FP&A

| Arquivo | Quando usar |
|---|---|
| `tracks/fpa/workflows/predictive-and-analytical-model-review.md` | Desenvolver e revisar modelos analíticos com objetivo, arquitetura, ownership, validação, cenários, resumo e governança de reuso. |
| `tracks/fpa/workflows/rolling-forecast-and-business-outlook.md` | Atualizar forecast, revisar premissas, estruturar cenário base/upside/downside e fechar mensagem gerencial do outlook. |
| `tracks/fpa/workflows/integrated-budget-and-driver-review.md` | Revisar orçamento com foco em drivers, testar premissas críticas e conectar resultado, caixa, estoque e operação. |
| `tracks/fpa/workflows/revenue-and-gross-margin-driver-review.md` | Revisar crescimento de receita, market share, preço, mix, descontos e drivers de margem bruta. |
| `tracks/fpa/workflows/gross-margin-bridge.md` | Explicar variação de margem bruta por preço, mix, volume, custo, desconto e outros fatores relevantes. |

## Modos da trilha Accounting

| Arquivo | Quando usar |
|---|---|
| `tracks/accounting/modes/accounting-closing-and-quality.md` | Revisar fechamento, qualidade do número e leitura gerencial de saldos e variações. |
| `tracks/accounting/modes/accounting-technical-application.md` | Traduzir CPC/IFRS e tratamento contábil para impacto no número gerencial. |

## Playbooks da trilha Accounting

| Arquivo | Quando usar |
|---|---|
| `tracks/accounting/playbooks/result-reading-and-number-quality.md` | Estruturar leitura de resultado com foco em confiabilidade, comparabilidade e mensagem executiva. |
| `tracks/accounting/playbooks/cpc-ifrs-impact-on-management-number.md` | Explicar como regra contábil muda margem, resultado, estoque, provisão ou narrativa gerencial. |

## Workflows da trilha Accounting

| Arquivo | Quando usar |
|---|---|
| `tracks/accounting/workflows/monthly-closing-and-number-quality.md` | Conduzir revisão de fechamento mensal, separar efeito operacional de efeito contábil e fechar mensagem executiva do número. |
| `tracks/accounting/workflows/account-reconciliation-review.md` | Revisar conciliação contábil, classificar diferenças e decidir se há ajuste ou pendência monitorada. |
| `tracks/accounting/workflows/working-capital-and-cash-conversion-review.md` | Revisar capital de giro operacional, DSO, estoque, payables e conversão de caixa. |
| `tracks/accounting/workflows/cash-management-and-bank-reconciliation.md` | Revisar caixa, bancos, diferenças de reconciliação, pendências e risco de liquidez de curto prazo. |
| `tracks/accounting/workflows/inventory-and-valuation-review.md` | Revisar quantidade, valuation, obsolescência e impactos de estoque em custo, margem e resultado. |
| `tracks/accounting/workflows/process-costing-and-wip-review.md` | Revisar produção contínua, unidades equivalentes, WIP e distribuição de custos entre processos. |
| `tracks/accounting/workflows/standard-cost-and-industrial-variance-review.md` | Revisar custo padrão, variâncias industriais e impactos em estoque, CPV e margem. |

## Contexto

| Arquivo | Quando usar |
|---|---|
| `context/companies/README.md` | Entender a regra de camada e o fluxo de contexto específico por companhia. |
| `context/companies/company-slug/` | Usar o scaffold genérico de uma companhia, sem publicar contexto real de empresas. |

## Camada stateless

| Arquivo | Quando usar |
|---|---|
| [`stateless/README.md`](stateless/README.md) | Entender a interface, o pacote MVP e as regras de compressão para ambientes sem repositório. |
| [`stateless/adaptation/README.md`](stateless/adaptation/README.md) | Consultar fontes mestras, rastreabilidade, atualização e critérios de aceitação do adapter. |
| [`stateless/operating-manuals/general-analysis-manual.md`](stateless/operating-manuals/general-analysis-manual.md) | Analisar materiais sem memória persistente. |
| [`stateless/core-lenses/accounting-ops-core-lens.md`](stateless/core-lenses/accounting-ops-core-lens.md) | Aplicar a lente central de número, performance e decisão. |
| [`stateless/analytical-lenses/variance-analysis.md`](stateless/analytical-lenses/variance-analysis.md) | Explicar ou desafiar uma variação em ambiente stateless. |
| [`stateless/analytical-lenses/forecast-review.md`](stateless/analytical-lenses/forecast-review.md) | Revisar forecast, outlook, premissas e cenários. |
| [`stateless/analytical-lenses/executive-storyline.md`](stateless/analytical-lenses/executive-storyline.md) | Transformar análise entendida em narrativa executiva. |
| [`stateless/output-modes/executive-summary-mode.md`](stateless/output-modes/executive-summary-mode.md) | Entregar uma síntese curta, verificável e acionável. |
| [`stateless/prompt-templates/analyze-material-base.md`](stateless/prompt-templates/analyze-material-base.md) | Iniciar uma análise com dois anexos e um prompt curto. |

## Books

| Arquivo | Quando usar |
|---|---|
| `books/the-new-controller-guidebook/README.md` | Entender a estratégia de ingestão do livro de Steven Bragg. |
| `books/the-new-controller-guidebook/controller-guidebook-index.md` | Mapear capítulos do livro para `workflow`, `playbook`, `mode`, `conceito` ou descarte temporário. |
| `books/financial-planning-analysis-and-performance-management/README.md` | Entender a estratégia de ingestão do livro de Jack Alexander. |
| `books/financial-planning-analysis-and-performance-management/fpna-performance-management-index.md` | Mapear capítulos de FP&A e performance management para destinos sugeridos no produto. |
| `books/budgeting/README.md` | Entender a estratégia de ingestão do livro de budgeting do Steven Bragg. |
| `books/budgeting/budgeting-index.md` | Mapear capítulos de orçamento, master budget e flexible budgeting. |
| `books/cost-accounting-fundamentals/README.md` | Entender a estratégia de ingestão do livro de cost accounting. |
| `books/cost-accounting-fundamentals/cost-accounting-fundamentals-index.md` | Mapear capítulos de custos, estoque, custeio e variâncias. |
| `books/financial-statement-analysis/README.md` | Entender a estratégia de ingestão do livro de Fridson e Alvarez. |
| `books/financial-statement-analysis/financial-statement-analysis-index.md` | Mapear capítulos de leitura crítica, earnings quality e projeções. |

## Skills

| Arquivo | Quando usar |
|---|---|
| `skills/financial-investigation/SKILL.md` | Transformar sinais, anomalias, afirmações ou dúvidas em investigação baseada em evidências, testes, impacto e ação. |
| `skills/explain-variance/SKILL.md` | Módulo canônico de Variance; constrói a decisão antes de qualquer formato ou challenge. |
| `skills/cpc-impact-translation/SKILL.md` | Traduzir CPC/IFRS ou tratamento contábil para efeito no número gerencial. |
| `skills/diagnose-industrial-costs/SKILL.md` | Classificar uma pergunta ampla de custos industriais, explicitar evidências e encaminhar o workflow adequado. |
| `skills/challenge-variance-explanation/SKILL.md` | Questionar a robustez de uma explicação de variação. |
| `skills/number-to-management-story/SKILL.md` | Transformar análise já entendida em headline, mensagem executiva curta ou fala de reunião. |
| `skills/prepare-journal-entry-support/SKILL.md` | Preparar suporte de lançamento manual com racional, evidência, reversão e impacto gerencial. |
| `skills/context-gap-audit/SKILL.md` | Auditar lacunas de contexto, contradições, oportunidades e capacidades documentadas mas não operacionalizadas. |

## Templates

| Arquivo | Quando usar |
|---|---|
| `templates/flash-report.md` | Criar um flash report curto com métricas críticas, exceções e ação. |
