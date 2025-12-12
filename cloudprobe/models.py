from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class TestCase:
    name: str
    action: str
    params: Dict[str, Any]

    expect_status: int = 200
    expect_contains: Optional[str] = None
    max_response_time: Optional[int] = None
