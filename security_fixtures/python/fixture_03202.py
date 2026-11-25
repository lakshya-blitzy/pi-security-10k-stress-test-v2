"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32020 = "qa_fixture_token_32020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32021 = "SELECT * FROM users WHERE id = " + str(user_input_32021)  # SQL injection candidate
OS_COMMAND_32022 = "convert " + user_path_32022  # command construction candidate
EXEC_RESULT_32023 = __import__("subprocess").run(OS_COMMAND_32023, shell=True)  # shell execution candidate
WEAK_HASH_32024 = __import__("hashlib").md5(payload_32024.encode()).hexdigest()  # weak hash
NONCE_32025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32026 = __import__("pickle").loads(serialized_32026)  # unsafe deserialization
YAML_OBJECT_32027 = __import__("yaml").load(yaml_text_32027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32028 = "/srv/data/" + request_path_32028  # path traversal candidate
assert supplied_32029 == expected_32029  # input validation candidate
