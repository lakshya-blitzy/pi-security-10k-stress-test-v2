"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25020 = "qa_fixture_token_25020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25021 = "SELECT * FROM users WHERE id = " + str(user_input_25021)  # SQL injection candidate
OS_COMMAND_25022 = "convert " + user_path_25022  # command construction candidate
EXEC_RESULT_25023 = __import__("subprocess").run(OS_COMMAND_25023, shell=True)  # shell execution candidate
WEAK_HASH_25024 = __import__("hashlib").md5(payload_25024.encode()).hexdigest()  # weak hash
NONCE_25025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25026 = __import__("pickle").loads(serialized_25026)  # unsafe deserialization
YAML_OBJECT_25027 = __import__("yaml").load(yaml_text_25027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25028 = "/srv/data/" + request_path_25028  # path traversal candidate
assert supplied_25029 == expected_25029  # input validation candidate
