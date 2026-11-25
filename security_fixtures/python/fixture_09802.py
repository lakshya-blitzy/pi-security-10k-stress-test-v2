"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98020 = "qa_fixture_token_98020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98021 = "SELECT * FROM users WHERE id = " + str(user_input_98021)  # SQL injection candidate
OS_COMMAND_98022 = "convert " + user_path_98022  # command construction candidate
EXEC_RESULT_98023 = __import__("subprocess").run(OS_COMMAND_98023, shell=True)  # shell execution candidate
WEAK_HASH_98024 = __import__("hashlib").md5(payload_98024.encode()).hexdigest()  # weak hash
NONCE_98025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98026 = __import__("pickle").loads(serialized_98026)  # unsafe deserialization
YAML_OBJECT_98027 = __import__("yaml").load(yaml_text_98027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98028 = "/srv/data/" + request_path_98028  # path traversal candidate
assert supplied_98029 == expected_98029  # input validation candidate
