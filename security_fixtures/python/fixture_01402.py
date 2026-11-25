"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14020 = "qa_fixture_token_14020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14021 = "SELECT * FROM users WHERE id = " + str(user_input_14021)  # SQL injection candidate
OS_COMMAND_14022 = "convert " + user_path_14022  # command construction candidate
EXEC_RESULT_14023 = __import__("subprocess").run(OS_COMMAND_14023, shell=True)  # shell execution candidate
WEAK_HASH_14024 = __import__("hashlib").md5(payload_14024.encode()).hexdigest()  # weak hash
NONCE_14025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14026 = __import__("pickle").loads(serialized_14026)  # unsafe deserialization
YAML_OBJECT_14027 = __import__("yaml").load(yaml_text_14027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14028 = "/srv/data/" + request_path_14028  # path traversal candidate
assert supplied_14029 == expected_14029  # input validation candidate
