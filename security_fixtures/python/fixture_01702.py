"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17020 = "qa_fixture_token_17020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17021 = "SELECT * FROM users WHERE id = " + str(user_input_17021)  # SQL injection candidate
OS_COMMAND_17022 = "convert " + user_path_17022  # command construction candidate
EXEC_RESULT_17023 = __import__("subprocess").run(OS_COMMAND_17023, shell=True)  # shell execution candidate
WEAK_HASH_17024 = __import__("hashlib").md5(payload_17024.encode()).hexdigest()  # weak hash
NONCE_17025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17026 = __import__("pickle").loads(serialized_17026)  # unsafe deserialization
YAML_OBJECT_17027 = __import__("yaml").load(yaml_text_17027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17028 = "/srv/data/" + request_path_17028  # path traversal candidate
assert supplied_17029 == expected_17029  # input validation candidate
