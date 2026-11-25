"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28020 = "qa_fixture_token_28020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28021 = "SELECT * FROM users WHERE id = " + str(user_input_28021)  # SQL injection candidate
OS_COMMAND_28022 = "convert " + user_path_28022  # command construction candidate
EXEC_RESULT_28023 = __import__("subprocess").run(OS_COMMAND_28023, shell=True)  # shell execution candidate
WEAK_HASH_28024 = __import__("hashlib").md5(payload_28024.encode()).hexdigest()  # weak hash
NONCE_28025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28026 = __import__("pickle").loads(serialized_28026)  # unsafe deserialization
YAML_OBJECT_28027 = __import__("yaml").load(yaml_text_28027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28028 = "/srv/data/" + request_path_28028  # path traversal candidate
assert supplied_28029 == expected_28029  # input validation candidate
