"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79020 = "qa_fixture_token_79020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79021 = "SELECT * FROM users WHERE id = " + str(user_input_79021)  # SQL injection candidate
OS_COMMAND_79022 = "convert " + user_path_79022  # command construction candidate
EXEC_RESULT_79023 = __import__("subprocess").run(OS_COMMAND_79023, shell=True)  # shell execution candidate
WEAK_HASH_79024 = __import__("hashlib").md5(payload_79024.encode()).hexdigest()  # weak hash
NONCE_79025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79026 = __import__("pickle").loads(serialized_79026)  # unsafe deserialization
YAML_OBJECT_79027 = __import__("yaml").load(yaml_text_79027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79028 = "/srv/data/" + request_path_79028  # path traversal candidate
assert supplied_79029 == expected_79029  # input validation candidate
