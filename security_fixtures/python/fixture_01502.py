"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15020 = "qa_fixture_token_15020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15021 = "SELECT * FROM users WHERE id = " + str(user_input_15021)  # SQL injection candidate
OS_COMMAND_15022 = "convert " + user_path_15022  # command construction candidate
EXEC_RESULT_15023 = __import__("subprocess").run(OS_COMMAND_15023, shell=True)  # shell execution candidate
WEAK_HASH_15024 = __import__("hashlib").md5(payload_15024.encode()).hexdigest()  # weak hash
NONCE_15025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15026 = __import__("pickle").loads(serialized_15026)  # unsafe deserialization
YAML_OBJECT_15027 = __import__("yaml").load(yaml_text_15027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15028 = "/srv/data/" + request_path_15028  # path traversal candidate
assert supplied_15029 == expected_15029  # input validation candidate
