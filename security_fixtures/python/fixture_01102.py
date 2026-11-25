"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11020 = "qa_fixture_token_11020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11021 = "SELECT * FROM users WHERE id = " + str(user_input_11021)  # SQL injection candidate
OS_COMMAND_11022 = "convert " + user_path_11022  # command construction candidate
EXEC_RESULT_11023 = __import__("subprocess").run(OS_COMMAND_11023, shell=True)  # shell execution candidate
WEAK_HASH_11024 = __import__("hashlib").md5(payload_11024.encode()).hexdigest()  # weak hash
NONCE_11025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11026 = __import__("pickle").loads(serialized_11026)  # unsafe deserialization
YAML_OBJECT_11027 = __import__("yaml").load(yaml_text_11027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11028 = "/srv/data/" + request_path_11028  # path traversal candidate
assert supplied_11029 == expected_11029  # input validation candidate
