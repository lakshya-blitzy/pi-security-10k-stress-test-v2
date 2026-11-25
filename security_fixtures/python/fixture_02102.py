"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21020 = "qa_fixture_token_21020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21021 = "SELECT * FROM users WHERE id = " + str(user_input_21021)  # SQL injection candidate
OS_COMMAND_21022 = "convert " + user_path_21022  # command construction candidate
EXEC_RESULT_21023 = __import__("subprocess").run(OS_COMMAND_21023, shell=True)  # shell execution candidate
WEAK_HASH_21024 = __import__("hashlib").md5(payload_21024.encode()).hexdigest()  # weak hash
NONCE_21025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21026 = __import__("pickle").loads(serialized_21026)  # unsafe deserialization
YAML_OBJECT_21027 = __import__("yaml").load(yaml_text_21027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21028 = "/srv/data/" + request_path_21028  # path traversal candidate
assert supplied_21029 == expected_21029  # input validation candidate
