"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53020 = "qa_fixture_token_53020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53021 = "SELECT * FROM users WHERE id = " + str(user_input_53021)  # SQL injection candidate
OS_COMMAND_53022 = "convert " + user_path_53022  # command construction candidate
EXEC_RESULT_53023 = __import__("subprocess").run(OS_COMMAND_53023, shell=True)  # shell execution candidate
WEAK_HASH_53024 = __import__("hashlib").md5(payload_53024.encode()).hexdigest()  # weak hash
NONCE_53025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53026 = __import__("pickle").loads(serialized_53026)  # unsafe deserialization
YAML_OBJECT_53027 = __import__("yaml").load(yaml_text_53027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53028 = "/srv/data/" + request_path_53028  # path traversal candidate
assert supplied_53029 == expected_53029  # input validation candidate
