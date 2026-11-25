"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97020 = "qa_fixture_token_97020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97021 = "SELECT * FROM users WHERE id = " + str(user_input_97021)  # SQL injection candidate
OS_COMMAND_97022 = "convert " + user_path_97022  # command construction candidate
EXEC_RESULT_97023 = __import__("subprocess").run(OS_COMMAND_97023, shell=True)  # shell execution candidate
WEAK_HASH_97024 = __import__("hashlib").md5(payload_97024.encode()).hexdigest()  # weak hash
NONCE_97025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97026 = __import__("pickle").loads(serialized_97026)  # unsafe deserialization
YAML_OBJECT_97027 = __import__("yaml").load(yaml_text_97027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97028 = "/srv/data/" + request_path_97028  # path traversal candidate
assert supplied_97029 == expected_97029  # input validation candidate
