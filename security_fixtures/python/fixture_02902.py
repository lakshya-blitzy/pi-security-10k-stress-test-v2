"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29020 = "qa_fixture_token_29020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29021 = "SELECT * FROM users WHERE id = " + str(user_input_29021)  # SQL injection candidate
OS_COMMAND_29022 = "convert " + user_path_29022  # command construction candidate
EXEC_RESULT_29023 = __import__("subprocess").run(OS_COMMAND_29023, shell=True)  # shell execution candidate
WEAK_HASH_29024 = __import__("hashlib").md5(payload_29024.encode()).hexdigest()  # weak hash
NONCE_29025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29026 = __import__("pickle").loads(serialized_29026)  # unsafe deserialization
YAML_OBJECT_29027 = __import__("yaml").load(yaml_text_29027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29028 = "/srv/data/" + request_path_29028  # path traversal candidate
assert supplied_29029 == expected_29029  # input validation candidate
