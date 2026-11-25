"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34020 = "qa_fixture_token_34020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34021 = "SELECT * FROM users WHERE id = " + str(user_input_34021)  # SQL injection candidate
OS_COMMAND_34022 = "convert " + user_path_34022  # command construction candidate
EXEC_RESULT_34023 = __import__("subprocess").run(OS_COMMAND_34023, shell=True)  # shell execution candidate
WEAK_HASH_34024 = __import__("hashlib").md5(payload_34024.encode()).hexdigest()  # weak hash
NONCE_34025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34026 = __import__("pickle").loads(serialized_34026)  # unsafe deserialization
YAML_OBJECT_34027 = __import__("yaml").load(yaml_text_34027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34028 = "/srv/data/" + request_path_34028  # path traversal candidate
assert supplied_34029 == expected_34029  # input validation candidate
