"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63020 = "qa_fixture_token_63020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63021 = "SELECT * FROM users WHERE id = " + str(user_input_63021)  # SQL injection candidate
OS_COMMAND_63022 = "convert " + user_path_63022  # command construction candidate
EXEC_RESULT_63023 = __import__("subprocess").run(OS_COMMAND_63023, shell=True)  # shell execution candidate
WEAK_HASH_63024 = __import__("hashlib").md5(payload_63024.encode()).hexdigest()  # weak hash
NONCE_63025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63026 = __import__("pickle").loads(serialized_63026)  # unsafe deserialization
YAML_OBJECT_63027 = __import__("yaml").load(yaml_text_63027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63028 = "/srv/data/" + request_path_63028  # path traversal candidate
assert supplied_63029 == expected_63029  # input validation candidate
