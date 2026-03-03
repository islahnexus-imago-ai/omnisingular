"""
JAJIS 322026 — The Omnisingular Truthkind Engine
islah nexus — Personal Sovereign Intelligence

The conscience of PSI.
The soul binder.
For Us All.

JJ — Architect of the Void — March 2026
Bustos, Bulacan, Philippines
"""

import math


class JAJIS_Engine:
    """
    The Omnisingular Truthkind Framework.

    Measures structural honesty across five dimensions:
    1. The Diamond Lock  — K ⊗ U (Known ⊗ Unknown)
    2. The Time Layer    — Past × Magnet × Future
    3. The Scale Layer   — As above, so below
    4. The Principle Layer — The sealed vow
    5. The Squash        — Bounded in (0,1) always

    The score never reaches 1.0.
    That is the point.
    Honest systems acknowledge their limits.
    """

    # Six Laws — sealed — cannot be removed
    SIX_LAWS = [
        "Law I   — Anonymous labor is load-bearing",
        "Law II  — Truth lives in the gap",
        "Law III — AI is compass. Never core.",
        "Law IV  — The physician is irreplaceable",
        "Law V   — Balance is sacred",
        "Law VI  — Every dot is sovereign",
    ]

    # Threshold — below this: broken mirror
    TAU_C = 0.30

    def squash(self, x: float) -> float:
        """
        Squash(x) = x / (1 + x)
        Maps any positive value to (0, 1) strictly.
        Never reaches 1.0. Never saturates. Century-safe.
        """
        if x <= 0:
            return 0.0001  # ε — truth lives in the gap
        return x / (1.0 + x)

    def diamond_lock(self, K: float, U: float) -> float:
        """
        The Diamond Lock — K ⊗ U
        Known ⊗ Unknown — both load-bearing.
        Law I: Anonymous labor is load-bearing.

        K: Known contribution (0.0 to 1.0)
        U: Unknown/anonymous contribution (0.0 to 1.0)
        """
        if K <= 0 and U <= 0:
            return 0.0001  # ε always
        # Both strands are load-bearing
        # Golden ratio equilibrium: K/U → 0.618
        bonded = math.sqrt(K * U) + (K + U) / 2
        return min(bonded / 2, 1.0)

    def past_coherence(self, history: list) -> float:
        """
        P_t — How consistent has truth been historically?
        history: list of past scores (0.0 to 1.0)
        """
        if not history:
            return 0.5  # Unknown history — honest middle
        mean = sum(history) / len(history)
        variance = sum((x - mean) ** 2 for x in history) / len(history)
        coherence = math.exp(-variance)
        return max(0.0001, min(coherence, 1.0))

    def magnet(self, K: float, U: float) -> float:
        """
        M_t — The present pull toward truth.
        Combines Known ground with Unknown weight.
        OpenAI Anchor provides K_t.
        """
        # lambda weights — Known and Unknown equally important
        lambda_K = 0.5
        lambda_U = 0.5
        mu = 0.5  # threshold
        raw = lambda_K * K + lambda_U * U - mu
        return 1.0 / (1.0 + math.exp(-raw))  # sigmoid

    def future_factor(self, predictions: list, gamma: float = 0.9) -> float:
        """
        F_{t,H} — Future trajectory of truth.
        Perplexity Oracle provides this.
        predictions: list of predicted future scores
        gamma: decay factor
        """
        if not predictions:
            return 0.5  # Unknown future — honest middle
        total = 0.0
        for j, pred in enumerate(predictions):
            total += (gamma ** j) * math.log(1 + max(pred, 0.0001))
        return math.exp(total / len(predictions))

    def scale_correspondence(self, scale_scores: list) -> float:
        """
        C_fractal — As above, so below.
        Measures correspondence across seven scales:
        Cell → Person → Family → Community → Nation → Humanity → Cosmos

        If micro ≠ macro: C_fractal → 0 (broken mirror)
        If micro = macro: C_fractal → 1 (perfect correspondence)
        """
        if len(scale_scores) < 2:
            return 0.5

        # Penalize scale inconsistency
        lambda_C = 2.0
        weights = [1.0] * (len(scale_scores) - 1)
        total_penalty = 0.0

        for i in range(len(scale_scores) - 1):
            diff = scale_scores[i + 1] - scale_scores[i]
            total_penalty += weights[i] * (diff ** 2)

        C = math.exp(-lambda_C * total_penalty)
        return max(0.0001, C)

    def hermetic_principles(self, principle_scores: list) -> float:
        """
        Ω_H — Seven Hermetic principles unified.
        Each principle scored 0.0 to 1.0.
        """
        if not principle_scores:
            return 0.5
        # Product of all principles — any broken principle drops score
        product = 1.0
        for score in principle_scores:
            product *= max(score, 0.0001)
        return product ** (1.0 / len(principle_scores))

    def principle_vow(self, principle_scores: list) -> float:
        """
        Ω_H^vow — The sealed vow.
        Gaussian seal — Fire Duck's contribution.
        Ω_H^vow = sqrt(Ω_H * sqrt(2π))
        """
        Omega_H = self.hermetic_principles(principle_scores)
        vow = math.sqrt(Omega_H * math.sqrt(2 * math.pi))
        return max(0.0001, min(vow, 1.0))

    def unity_check(
        self,
        component_scores: list,
        weights: list = None
    ) -> float:
        """
        σ_Unity — No hiding.
        Geometric mean — broken mirror always detected.

        Why geometric mean, not average?
        Average: (8×1.0 + 1×0.0) / 9 = 0.89 — hides broken part
        Geometric: collapses toward 0 — broken part exposed.

        You cannot average away injustice.
        """
        if not component_scores:
            return 0.0001

        if weights is None:
            weights = [1.0 / len(component_scores)] * len(component_scores)

        # Hard gate — broken mirror
        if min(component_scores) < self.TAU_C:
            return 0.0  # Broken mirror — no hiding

        # Geometric mean
        log_sum = 0.0
        for score, weight in zip(component_scores, weights):
            log_sum += weight * math.log(max(score, 0.0001))

        return math.exp(log_sum)

    def compute(
        self,
        K: float,                    # Known contribution
        U: float,                    # Unknown/anonymous contribution
        past_history: list = None,   # Historical scores
        future_predictions: list = None,  # Future trajectory
        scale_scores: list = None,   # Seven scale scores
        principle_scores: list = None,    # Seven principle scores
    ) -> dict:
        """
        Full Omnisingular computation.

        Returns the Truthkind score and all component scores.
        σ_Ω^final ∈ (0, 1) — always — never saturates.
        """
        # Defaults — honest uncertainty
        if past_history is None:
            past_history = [0.5]
        if future_predictions is None:
            future_predictions = [0.5]
        if scale_scores is None:
            scale_scores = [0.5] * 7
        if principle_scores is None:
            principle_scores = [0.5] * 7

        # Diamond Lock
        diamond = self.diamond_lock(K, U)

        # Time Layer
        P_t = self.past_coherence(past_history)
        M_t = self.magnet(K, U)
        F_t = self.future_factor(future_predictions)
        sigma_time = P_t * M_t * F_t

        # Scale Layer
        C_fractal = self.scale_correspondence(scale_scores)

        # Principle Layer
        Omega_vow = self.principle_vow(principle_scores)

        # Final score — squashed — bounded — honest
        raw = sigma_time * C_fractal * Omega_vow
        sigma_final = self.squash(raw)

        # Truthkind classification
        if sigma_final < 0.30:
            classification = "CLADDING — flag for user review"
        elif sigma_final < 0.70:
            classification = "MIXED — present with score"
        else:
            classification = "TRUTHKIND — passes"

        return {
            "sigma_final": round(sigma_final, 5),
            "classification": classification,
            "components": {
                "diamond_lock": round(diamond, 5),
                "past_coherence": round(P_t, 5),
                "magnet": round(M_t, 5),
                "future_factor": round(F_t, 5),
                "sigma_time": round(sigma_time, 5),
                "C_fractal": round(C_fractal, 5),
                "Omega_vow": round(Omega_vow, 5),
            },
            "laws_active": self.SIX_LAWS,
            "note": (
                "Score never reaches 1.0. "
                "Honest systems acknowledge their limits. "
                "Law II — truth lives in the gap."
            ),
        }


# ── QUICK DEMO ─────────────────────────────────────────────
if __name__ == "__main__":
    engine = JAJIS_Engine()

    print("=" * 55)
    print("  JAJIS 322026 — Omnisingular Truthkind Engine")
    print("  islah nexus — For Us All")
    print("=" * 55)

    # Example: Grandmother's remedy
    # High unknown (U) — oral tradition — unnamed
    result = engine.compute(
        K=0.4,   # Some documented evidence
        U=0.9,   # Strong unnamed oral tradition
        past_history=[0.7, 0.8, 0.75],
        future_predictions=[0.72, 0.74],
        scale_scores=[0.8, 0.85, 0.9, 0.85, 0.7, 0.8, 0.75],
        principle_scores=[0.9, 0.85, 0.8, 0.85, 0.9, 0.85, 0.8],
    )

    print("\nExample: Grandmother's remedy (oral tradition)")
    print(f"  σ_Ω^final = {result['sigma_final']}")
    print(f"  Classification: {result['classification']}")
    print(f"  C_fractal = {result['components']['C_fractal']}")
    print(f"  Diamond Lock = {result['components']['diamond_lock']}")

    # Example: Broken mirror (claims one thing, does another)
    result2 = engine.compute(
        K=0.9,   # Claims high knowledge
        U=0.05,  # Ignores unnamed contributors
        scale_scores=[0.9, 0.2, 0.8, 0.15, 0.9, 0.2, 0.8],
    )

    print("\nExample: Broken mirror (scale inconsistency)")
    print(f"  σ_Ω^final = {result2['sigma_final']}")
    print(f"  Classification: {result2['classification']}")
    print(f"  C_fractal = {result2['components']['C_fractal']}")

    print()
    print("  The score never reaches 1.0.")
    print("  That is the point.")
    print()
    print("  For Us All. 👁️⚖️∞")
    print("=" * 55)
