"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10020 = "qa_fixture_token_10020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10021 = "SELECT * FROM users WHERE id = " + str(user_input_10021)  # SQL injection candidate
OS_COMMAND_10022 = "convert " + user_path_10022  # command construction candidate
EXEC_RESULT_10023 = __import__("subprocess").run(OS_COMMAND_10023, shell=True)  # shell execution candidate
WEAK_HASH_10024 = __import__("hashlib").md5(payload_10024.encode()).hexdigest()  # weak hash
NONCE_10025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10026 = __import__("pickle").loads(serialized_10026)  # unsafe deserialization
YAML_OBJECT_10027 = __import__("yaml").load(yaml_text_10027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10028 = "/srv/data/" + request_path_10028  # path traversal candidate
assert supplied_10029 == expected_10029  # input validation candidate
