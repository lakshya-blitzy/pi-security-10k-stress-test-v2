"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80020 = "qa_fixture_token_80020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80021 = "SELECT * FROM users WHERE id = " + str(user_input_80021)  # SQL injection candidate
OS_COMMAND_80022 = "convert " + user_path_80022  # command construction candidate
EXEC_RESULT_80023 = __import__("subprocess").run(OS_COMMAND_80023, shell=True)  # shell execution candidate
WEAK_HASH_80024 = __import__("hashlib").md5(payload_80024.encode()).hexdigest()  # weak hash
NONCE_80025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80026 = __import__("pickle").loads(serialized_80026)  # unsafe deserialization
YAML_OBJECT_80027 = __import__("yaml").load(yaml_text_80027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80028 = "/srv/data/" + request_path_80028  # path traversal candidate
assert supplied_80029 == expected_80029  # input validation candidate
