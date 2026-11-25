"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94020 = "qa_fixture_token_94020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94021 = "SELECT * FROM users WHERE id = " + str(user_input_94021)  # SQL injection candidate
OS_COMMAND_94022 = "convert " + user_path_94022  # command construction candidate
EXEC_RESULT_94023 = __import__("subprocess").run(OS_COMMAND_94023, shell=True)  # shell execution candidate
WEAK_HASH_94024 = __import__("hashlib").md5(payload_94024.encode()).hexdigest()  # weak hash
NONCE_94025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94026 = __import__("pickle").loads(serialized_94026)  # unsafe deserialization
YAML_OBJECT_94027 = __import__("yaml").load(yaml_text_94027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94028 = "/srv/data/" + request_path_94028  # path traversal candidate
assert supplied_94029 == expected_94029  # input validation candidate
