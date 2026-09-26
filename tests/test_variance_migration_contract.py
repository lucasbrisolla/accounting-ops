from __future__ import annotations

import unittest
import re
from decimal import Decimal
from pathlib import Path

from scripts.challenge_variance_adapter import challenge_variance
from scripts.variance_explanation_contract import (
    Action,
    Baseline,
    Confidence,
    Driver,
    DriverKind,
    DriverStatus,
    ExplanationStatus,
    Materiality,
    Recurrence,
    VarianceExplanation,
)
from scripts.variance_output_adapters import build_management_story, build_one_pager


ROOT = Path(__file__).resolve().parents[1]
ROUTER = ROOT / "CLAUDE.md"
INDEXES = (ROOT / "PRODUCT_INDEX.md",)
LEGACY_SURFACES = (
    ROOT / "_method-wiki" / "patterns" / "variance-analysis.md",
    ROOT / "tracks" / "fpa" / "modes" / "variance-analysis.md",
)


class VarianceMigrationContractTests(unittest.TestCase):
    def test_variance_router_loads_canonical_module_before_any_output_adapter(self):
        content = ROUTER.read_text(encoding="utf-8")
        start = content.index("### Roteamento de Variance")
        end = content.index("## Base Metodológica", start)
        route_section = content[start:end]

        canonical = "skills/explain-variance/SKILL.md"
        adapters = (
            "skills/challenge-variance-explanation/SKILL.md",
            "skills/number-to-management-story/SKILL.md",
        )

        canonical_position = route_section.index(canonical)
        for adapter in adapters:
            self.assertLess(canonical_position, route_section.index(adapter))

        self.assertIn("primeiro", route_section.lower())
        self.assertIn("formato", route_section.lower())

    def test_indexes_identify_the_canonical_module_as_variance_source_of_truth(self):
        canonical = "skills/explain-variance/SKILL.md"
        adapters = (
            "skills/challenge-variance-explanation/SKILL.md",
            "skills/number-to-management-story/SKILL.md",
        )

        for index_path in INDEXES:
            with self.subTest(index=index_path.name):
                content = index_path.read_text(encoding="utf-8")
                canonical_position = content.index(canonical)
                for adapter in adapters:
                    self.assertLess(canonical_position, content.index(adapter))

                self.assertIn("módulo canônico", content.lower())

    def test_pattern_and_mode_are_references_not_competing_variance_contracts(self):
        for surface_path in LEGACY_SURFACES:
            with self.subTest(surface=surface_path.as_posix()):
                content = surface_path.read_text(encoding="utf-8")
                self.assertIn("skills/explain-variance/SKILL.md", content)
                self.assertIn("módulo canônico", content.lower())
                self.assertRegex(content.lower(), r"não é o contrato\s+canônico")

    def test_deletion_equivalent_all_output_callers_require_the_canonical_decision(self):
        explanation = VarianceExplanation(
            baseline=Baseline(actual=Decimal("120"), reference=Decimal("100"), reference_name="Budget"),
            materiality=Materiality(
                decision_relevance="Muda a leitura de performance.",
                decision_relevant=True,
            ),
            breakdown=("OPEX",),
            drivers=(
                Driver(
                    name="Serviços contratados",
                    impact=Decimal("20"),
                    evidence=("Razão analítica",),
                    status=DriverStatus.CONFIRMED,
                    kind=DriverKind.OPERATIONAL,
                ),
            ),
            evidence=("DRE gerencial",),
            impact=("A margem ficou abaixo do Budget.",),
            action=Action(description="Validar a recorrência no próximo fechamento."),
            recurrence=Recurrence.RECURRING,
            confidence=Confidence.HIGH,
            status=ExplanationStatus.CONFIRMED,
        )
        callers = (challenge_variance, build_one_pager, build_management_story)

        for caller in callers:
            with self.subTest(caller=caller.__name__):
                result = caller(explanation)
                self.assertIs(result.source, explanation)
                with self.assertRaises(TypeError):
                    caller({"actual": 120, "reference": 100, "driver": "Serviços contratados"})


if __name__ == "__main__":
    unittest.main()
