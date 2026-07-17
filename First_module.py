
from __future__ import annotations

import math
import itertools
from dataclasses import dataclass, field
from typing import Optional, FrozenSet, Dict, List, Tuple

#  Interval Attribute Domain  I  (Definition 4)
@dataclass(frozen=True)
class Interval:
    """
    An element of I = { [l, u] | l,u ∈ R≥0, l ≤ u } ∪ { [l, ∞) | l ∈ R≥0 }.

    Bounded  : Interval(l, u)       →  [l, u]
    Unbounded: Interval(l, INF)     →  [l, ∞)
    """
    l: float   # lower bound (≥ 0)
    u: float   # upper bound (≥ l, may be INF)

    def __post_init__(self):
        if self.l < 0:
            raise ValueError(f"Lower bound must be ≥ 0, got {self.l}")
        if self.u < self.l:
            raise ValueError(f"Upper bound {self.u} must be ≥ lower bound {self.l}")

    @property
    def is_unbounded(self) -> bool:
        return self.u == INF

    def __repr__(self) -> str:
        u_str = "∞" if self.is_unbounded else str(self.u)
        return f"[{self.l}, {u_str}]"



# Convenient factory helpers
def bounded(l: float, u: float) -> Interval:
    return Interval(l, u)

def unbounded(l: float) -> Interval:
    return Interval(l, INF)

