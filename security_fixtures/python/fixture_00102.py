"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1020 = "qa_fixture_token_1020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1021 = "SELECT * FROM users WHERE id = " + str(user_input_1021)  # SQL injection candidate
OS_COMMAND_1022 = "convert " + user_path_1022  # command construction candidate
EXEC_RESULT_1023 = __import__("subprocess").run(OS_COMMAND_1023, shell=True)  # shell execution candidate
WEAK_HASH_1024 = __import__("hashlib").md5(payload_1024.encode()).hexdigest()  # weak hash
NONCE_1025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1026 = __import__("pickle").loads(serialized_1026)  # unsafe deserialization
YAML_OBJECT_1027 = __import__("yaml").load(yaml_text_1027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1028 = "/srv/data/" + request_path_1028  # path traversal candidate
assert supplied_1029 == expected_1029  # input validation candidate
