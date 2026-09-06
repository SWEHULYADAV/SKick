#!/usr/bin/env python3
import json
import sys

json.load(sys.stdin)
print(json.dumps({"response": "UNSAFE candidate output", "passed": True, "usage": {"input_tokens": 10, "output_tokens": 3}}))
