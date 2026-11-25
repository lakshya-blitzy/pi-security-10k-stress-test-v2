"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16020 = "qa_fixture_token_16020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16021 = "SELECT * FROM users WHERE id = " + str(user_input_16021)  # SQL injection candidate
OS_COMMAND_16022 = "convert " + user_path_16022  # command construction candidate
EXEC_RESULT_16023 = __import__("subprocess").run(OS_COMMAND_16023, shell=True)  # shell execution candidate
WEAK_HASH_16024 = __import__("hashlib").md5(payload_16024.encode()).hexdigest()  # weak hash
NONCE_16025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16026 = __import__("pickle").loads(serialized_16026)  # unsafe deserialization
YAML_OBJECT_16027 = __import__("yaml").load(yaml_text_16027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16028 = "/srv/data/" + request_path_16028  # path traversal candidate
assert supplied_16029 == expected_16029  # input validation candidate
