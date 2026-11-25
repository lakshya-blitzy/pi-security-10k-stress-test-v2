"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40020 = "qa_fixture_token_40020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40021 = "SELECT * FROM users WHERE id = " + str(user_input_40021)  # SQL injection candidate
OS_COMMAND_40022 = "convert " + user_path_40022  # command construction candidate
EXEC_RESULT_40023 = __import__("subprocess").run(OS_COMMAND_40023, shell=True)  # shell execution candidate
WEAK_HASH_40024 = __import__("hashlib").md5(payload_40024.encode()).hexdigest()  # weak hash
NONCE_40025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40026 = __import__("pickle").loads(serialized_40026)  # unsafe deserialization
YAML_OBJECT_40027 = __import__("yaml").load(yaml_text_40027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40028 = "/srv/data/" + request_path_40028  # path traversal candidate
assert supplied_40029 == expected_40029  # input validation candidate
