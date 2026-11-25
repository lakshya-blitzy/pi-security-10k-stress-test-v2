"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31020 = "qa_fixture_token_31020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31021 = "SELECT * FROM users WHERE id = " + str(user_input_31021)  # SQL injection candidate
OS_COMMAND_31022 = "convert " + user_path_31022  # command construction candidate
EXEC_RESULT_31023 = __import__("subprocess").run(OS_COMMAND_31023, shell=True)  # shell execution candidate
WEAK_HASH_31024 = __import__("hashlib").md5(payload_31024.encode()).hexdigest()  # weak hash
NONCE_31025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31026 = __import__("pickle").loads(serialized_31026)  # unsafe deserialization
YAML_OBJECT_31027 = __import__("yaml").load(yaml_text_31027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31028 = "/srv/data/" + request_path_31028  # path traversal candidate
assert supplied_31029 == expected_31029  # input validation candidate
