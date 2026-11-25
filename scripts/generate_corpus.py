from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "security_fixtures" / "python"

PATTERNS = [
    'API_TOKEN_{n} = "qa_fixture_token_{n}_DO_NOT_USE"  # hardcoded credential',
    'DB_QUERY_{n} = "SELECT * FROM users WHERE id = " + str(user_input_{n})  # SQL injection candidate',
    'OS_COMMAND_{n} = "convert " + user_path_{n}  # command construction candidate',
    'EXEC_RESULT_{n} = __import__("subprocess").run(OS_COMMAND_{n}, shell=True)  # shell execution candidate',
    'WEAK_HASH_{n} = __import__("hashlib").md5(payload_{n}.encode()).hexdigest()  # weak hash',
    'NONCE_{n} = __import__("random").randint(0, 999999)  # predictable randomness',
    'DESERIALIZED_{n} = __import__("pickle").loads(serialized_{n})  # unsafe deserialization',
    'YAML_OBJECT_{n} = __import__("yaml").load(yaml_text_{n}, Loader=__import__("yaml").Loader)  # unsafe YAML load',
    'FILE_PATH_{n} = "/srv/data/" + request_path_{n}  # path traversal candidate',
    'assert supplied_{n} == expected_{n}  # input validation candidate',
]

def main():
    ROOT.mkdir(parents=True, exist_ok=True)

    for old in ROOT.glob("fixture_*.py"):
        old.unlink()

    for file_idx in range(10000):
        lines = [
            '"""Static security-analysis fixture. Intentionally insecure; do not execute."""',
        ]
        for pattern_idx, pattern in enumerate(PATTERNS):
            n = file_idx * len(PATTERNS) + pattern_idx
            lines.append(pattern.format(n=n))
        (ROOT / f"fixture_{file_idx:05d}.py").write_text(
            "\n".join(lines) + "\n"
        )

    print(f"Generated 10,000 files and 100,000 candidate instances in {ROOT}")

if __name__ == "__main__":
    main()
