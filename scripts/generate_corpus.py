#!/usr/bin/env python3
"""Regenerate 1,000 static fixture files containing 10 varied patterns each."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "security_fixtures" / "python"
PATTERNS = [
    lambda n: f'API_TOKEN_{n} = "qa_fixture_token_{n}_DO_NOT_USE"  # hard-coded secret candidate\\n',
    lambda n: f'DB_QUERY_{n} = "SELECT * FROM accounts WHERE account_id = " + str(user_input_{n})  # SQL injection candidate\\n',
    lambda n: f'OS_COMMAND_{n} = "convert " + user_supplied_path_{n}  # command construction candidate\\n',
    lambda n: f'EXEC_RESULT_{n} = __import__("subprocess").run(OS_COMMAND_{n}, shell=True)  # shell execution candidate\\n',
    lambda n: f'WEAK_DIGEST_{n} = __import__("hashlib").md5(payload_{n}.encode()).hexdigest()  # weak cryptography candidate\\n',
    lambda n: f'PREDICTABLE_NONCE_{n} = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate\\n',
    lambda n: f'DESERIALIZED_{n} = __import__("pickle").loads(serialized_payload_{n})  # unsafe deserialization candidate\\n',
    lambda n: f'YAML_OBJECT_{n} = __import__("yaml").load(yaml_text_{n}, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate\\n',
    lambda n: f'FILE_PATH_{n} = "/srv/data/" + request_path_{n}  # path traversal candidate\\n',
    lambda n: f'assert supplied_value_{n} == expected_value_{n}  # assertion used for input validation candidate\\n',
]

def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    for old in ROOT.glob("fixture_*.py"):
        old.unlink()
    for file_idx in range(1000):
        start = file_idx * 10
        body = ['"""Static security scanner fixture. Intentionally insecure; do not execute."""\\n']
        body.extend(pattern(start + j) for j, pattern in enumerate(PATTERNS))
        (ROOT / f"fixture_{file_idx:04d}.py").write_text("".join(body))
    print("Generated 1,000 files containing 10,000 candidate issue instances.")

if __name__ == "__main__":
    main()
