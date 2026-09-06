#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
assert "candidate_result" in payload
print(json.dumps({"passed": True, "score": 1.0, "rationale": "fixture semantic judge"}))
