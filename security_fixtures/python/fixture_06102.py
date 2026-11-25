"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61020 = "qa_fixture_token_61020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61021 = "SELECT * FROM users WHERE id = " + str(user_input_61021)  # SQL injection candidate
OS_COMMAND_61022 = "convert " + user_path_61022  # command construction candidate
EXEC_RESULT_61023 = __import__("subprocess").run(OS_COMMAND_61023, shell=True)  # shell execution candidate
WEAK_HASH_61024 = __import__("hashlib").md5(payload_61024.encode()).hexdigest()  # weak hash
NONCE_61025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61026 = __import__("pickle").loads(serialized_61026)  # unsafe deserialization
YAML_OBJECT_61027 = __import__("yaml").load(yaml_text_61027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61028 = "/srv/data/" + request_path_61028  # path traversal candidate
assert supplied_61029 == expected_61029  # input validation candidate
