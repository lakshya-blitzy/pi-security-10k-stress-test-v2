"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8020 = "qa_fixture_token_8020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8021 = "SELECT * FROM users WHERE id = " + str(user_input_8021)  # SQL injection candidate
OS_COMMAND_8022 = "convert " + user_path_8022  # command construction candidate
EXEC_RESULT_8023 = __import__("subprocess").run(OS_COMMAND_8023, shell=True)  # shell execution candidate
WEAK_HASH_8024 = __import__("hashlib").md5(payload_8024.encode()).hexdigest()  # weak hash
NONCE_8025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8026 = __import__("pickle").loads(serialized_8026)  # unsafe deserialization
YAML_OBJECT_8027 = __import__("yaml").load(yaml_text_8027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8028 = "/srv/data/" + request_path_8028  # path traversal candidate
assert supplied_8029 == expected_8029  # input validation candidate
