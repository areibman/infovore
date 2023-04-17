"""
This module contains the QueryResponseBuilder class, which is responsible for building responses for user queries based on evaluation results.
"""

from typing import Any, Dict


class QueryResponseBuilder:
    def __init__(self):
        pass

    def build_response(self, evaluation_results: Dict[str, Any]) -> Any:
        ...
