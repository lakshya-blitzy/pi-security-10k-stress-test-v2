"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46020 = "qa_fixture_token_46020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46021 = "SELECT * FROM users WHERE id = " + str(user_input_46021)  # SQL injection candidate
OS_COMMAND_46022 = "convert " + user_path_46022  # command construction candidate
EXEC_RESULT_46023 = __import__("subprocess").run(OS_COMMAND_46023, shell=True)  # shell execution candidate
WEAK_HASH_46024 = __import__("hashlib").md5(payload_46024.encode()).hexdigest()  # weak hash
NONCE_46025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46026 = __import__("pickle").loads(serialized_46026)  # unsafe deserialization
YAML_OBJECT_46027 = __import__("yaml").load(yaml_text_46027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46028 = "/srv/data/" + request_path_46028  # path traversal candidate
assert supplied_46029 == expected_46029  # input validation candidate
