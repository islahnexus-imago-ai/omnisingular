"""
The Diamond Lock — K ⊗ U
JAJIS 322026 — islah nexus

Law I: Anonymous labor is load-bearing.
The Known and Unknown are bonded permanently.
Neither can be separated without collapsing the structure.

For Us All. 👁️⚖️∞
"""

import math


def diamond_lock(K: float, U: float) -> float:
    """
    Bond the Known (K) and Unknown (U) contributions.

    K — the cited, credited, documented
    U — the anonymous, unnamed, uncredited

    Both are load-bearing. Always.
    The golden ratio equilibrium: K/U → 0.618
    The Unknown is naturally larger than the Known.
    Most of what makes something true is unnamed.
    """
    if K <= 0 and U <= 0:
        return 1e-4  # epsilon — truth lives in the gap
    bonded = math.sqrt(K * U) + (K + U) / 2
    return min(bonded / 2, 1.0)


def check_balance(K: float, U: float) -> dict:
    """
    Check if K and U are in healthy balance.
    Golden ratio equilibrium: K/U ≈ 0.618
    """
    PHI_INV = 0.618  # Golden ratio inverse
    if U == 0:
        ratio = float('inf')
    else:
        ratio = K / U

    deviation = abs(ratio - PHI_INV)

    return {
        "K": K,
        "U": U,
        "ratio": round(ratio, 4),
        "golden_equilibrium": PHI_INV,
        "deviation": round(deviation, 4),
        "balanced": deviation < 0.2,
        "note": (
            "U (Unknown) should naturally be larger than K (Known). "
            "Most of what makes something true is unnamed."
        ),
    }
