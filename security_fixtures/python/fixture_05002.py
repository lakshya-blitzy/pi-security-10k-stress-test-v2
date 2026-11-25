"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50020 = "qa_fixture_token_50020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50021 = "SELECT * FROM users WHERE id = " + str(user_input_50021)  # SQL injection candidate
OS_COMMAND_50022 = "convert " + user_path_50022  # command construction candidate
EXEC_RESULT_50023 = __import__("subprocess").run(OS_COMMAND_50023, shell=True)  # shell execution candidate
WEAK_HASH_50024 = __import__("hashlib").md5(payload_50024.encode()).hexdigest()  # weak hash
NONCE_50025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50026 = __import__("pickle").loads(serialized_50026)  # unsafe deserialization
YAML_OBJECT_50027 = __import__("yaml").load(yaml_text_50027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50028 = "/srv/data/" + request_path_50028  # path traversal candidate
assert supplied_50029 == expected_50029  # input validation candidate
