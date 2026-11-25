"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83020 = "qa_fixture_token_83020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83021 = "SELECT * FROM users WHERE id = " + str(user_input_83021)  # SQL injection candidate
OS_COMMAND_83022 = "convert " + user_path_83022  # command construction candidate
EXEC_RESULT_83023 = __import__("subprocess").run(OS_COMMAND_83023, shell=True)  # shell execution candidate
WEAK_HASH_83024 = __import__("hashlib").md5(payload_83024.encode()).hexdigest()  # weak hash
NONCE_83025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83026 = __import__("pickle").loads(serialized_83026)  # unsafe deserialization
YAML_OBJECT_83027 = __import__("yaml").load(yaml_text_83027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83028 = "/srv/data/" + request_path_83028  # path traversal candidate
assert supplied_83029 == expected_83029  # input validation candidate
