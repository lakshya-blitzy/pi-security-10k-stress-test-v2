"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65020 = "qa_fixture_token_65020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65021 = "SELECT * FROM users WHERE id = " + str(user_input_65021)  # SQL injection candidate
OS_COMMAND_65022 = "convert " + user_path_65022  # command construction candidate
EXEC_RESULT_65023 = __import__("subprocess").run(OS_COMMAND_65023, shell=True)  # shell execution candidate
WEAK_HASH_65024 = __import__("hashlib").md5(payload_65024.encode()).hexdigest()  # weak hash
NONCE_65025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65026 = __import__("pickle").loads(serialized_65026)  # unsafe deserialization
YAML_OBJECT_65027 = __import__("yaml").load(yaml_text_65027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65028 = "/srv/data/" + request_path_65028  # path traversal candidate
assert supplied_65029 == expected_65029  # input validation candidate
