"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4020 = "qa_fixture_token_4020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4021 = "SELECT * FROM users WHERE id = " + str(user_input_4021)  # SQL injection candidate
OS_COMMAND_4022 = "convert " + user_path_4022  # command construction candidate
EXEC_RESULT_4023 = __import__("subprocess").run(OS_COMMAND_4023, shell=True)  # shell execution candidate
WEAK_HASH_4024 = __import__("hashlib").md5(payload_4024.encode()).hexdigest()  # weak hash
NONCE_4025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4026 = __import__("pickle").loads(serialized_4026)  # unsafe deserialization
YAML_OBJECT_4027 = __import__("yaml").load(yaml_text_4027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4028 = "/srv/data/" + request_path_4028  # path traversal candidate
assert supplied_4029 == expected_4029  # input validation candidate
