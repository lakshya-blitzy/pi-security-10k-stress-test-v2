"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90020 = "qa_fixture_token_90020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90021 = "SELECT * FROM users WHERE id = " + str(user_input_90021)  # SQL injection candidate
OS_COMMAND_90022 = "convert " + user_path_90022  # command construction candidate
EXEC_RESULT_90023 = __import__("subprocess").run(OS_COMMAND_90023, shell=True)  # shell execution candidate
WEAK_HASH_90024 = __import__("hashlib").md5(payload_90024.encode()).hexdigest()  # weak hash
NONCE_90025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90026 = __import__("pickle").loads(serialized_90026)  # unsafe deserialization
YAML_OBJECT_90027 = __import__("yaml").load(yaml_text_90027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90028 = "/srv/data/" + request_path_90028  # path traversal candidate
assert supplied_90029 == expected_90029  # input validation candidate
