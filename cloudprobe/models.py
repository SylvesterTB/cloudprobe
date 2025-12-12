from dataclasses import dataclass
from typing import Optional

@dataclass
class TestCase:
    name: str
    url: str
    expect_status: int = 200
    expect_contains: Optional[str] = None
    max_response_time: Optional[int] = None  # ms
    action: str
    params: dict
    
