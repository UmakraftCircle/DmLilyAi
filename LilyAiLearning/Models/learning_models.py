from dataclasses import dataclass, field


@dataclass
class FeedbackRecord:
    user_id: str
    rating: int  # +1 / -1
    prompt: str
    response: str
    comment: str = ""
    used_evidence: bool = False
    domains: list[str] = field(default_factory=list)


@dataclass
class EvalCase:
    name: str
    prompt: str
    expect_any: list[str] = field(default_factory=list)
    expect_none: list[str] = field(default_factory=list)


@dataclass
class EvalOutcome:
    name: str
    passed: bool
    response: str
    reason: str = ""


@dataclass
class EvalReport:
    outcomes: list[EvalOutcome]

    @property
    def passed(self) -> int:
        return sum(o.passed for o in self.outcomes)

    @property
    def total(self) -> int:
        return len(self.outcomes)
