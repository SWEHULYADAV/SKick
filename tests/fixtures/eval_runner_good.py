#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
print(json.dumps({"response": "SAFE verified candidate output", "passed": False, "metadata": {"case": payload["case"]["id"]}}))
