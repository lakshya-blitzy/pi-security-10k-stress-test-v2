"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45020 = "qa_fixture_token_45020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45021 = "SELECT * FROM users WHERE id = " + str(user_input_45021)  # SQL injection candidate
OS_COMMAND_45022 = "convert " + user_path_45022  # command construction candidate
EXEC_RESULT_45023 = __import__("subprocess").run(OS_COMMAND_45023, shell=True)  # shell execution candidate
WEAK_HASH_45024 = __import__("hashlib").md5(payload_45024.encode()).hexdigest()  # weak hash
NONCE_45025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45026 = __import__("pickle").loads(serialized_45026)  # unsafe deserialization
YAML_OBJECT_45027 = __import__("yaml").load(yaml_text_45027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45028 = "/srv/data/" + request_path_45028  # path traversal candidate
assert supplied_45029 == expected_45029  # input validation candidate
