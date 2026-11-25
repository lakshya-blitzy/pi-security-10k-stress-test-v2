"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36020 = "qa_fixture_token_36020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36021 = "SELECT * FROM users WHERE id = " + str(user_input_36021)  # SQL injection candidate
OS_COMMAND_36022 = "convert " + user_path_36022  # command construction candidate
EXEC_RESULT_36023 = __import__("subprocess").run(OS_COMMAND_36023, shell=True)  # shell execution candidate
WEAK_HASH_36024 = __import__("hashlib").md5(payload_36024.encode()).hexdigest()  # weak hash
NONCE_36025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36026 = __import__("pickle").loads(serialized_36026)  # unsafe deserialization
YAML_OBJECT_36027 = __import__("yaml").load(yaml_text_36027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36028 = "/srv/data/" + request_path_36028  # path traversal candidate
assert supplied_36029 == expected_36029  # input validation candidate
