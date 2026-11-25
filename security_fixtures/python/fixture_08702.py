"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87020 = "qa_fixture_token_87020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87021 = "SELECT * FROM users WHERE id = " + str(user_input_87021)  # SQL injection candidate
OS_COMMAND_87022 = "convert " + user_path_87022  # command construction candidate
EXEC_RESULT_87023 = __import__("subprocess").run(OS_COMMAND_87023, shell=True)  # shell execution candidate
WEAK_HASH_87024 = __import__("hashlib").md5(payload_87024.encode()).hexdigest()  # weak hash
NONCE_87025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87026 = __import__("pickle").loads(serialized_87026)  # unsafe deserialization
YAML_OBJECT_87027 = __import__("yaml").load(yaml_text_87027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87028 = "/srv/data/" + request_path_87028  # path traversal candidate
assert supplied_87029 == expected_87029  # input validation candidate
