"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9020 = "qa_fixture_token_9020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9021 = "SELECT * FROM users WHERE id = " + str(user_input_9021)  # SQL injection candidate
OS_COMMAND_9022 = "convert " + user_path_9022  # command construction candidate
EXEC_RESULT_9023 = __import__("subprocess").run(OS_COMMAND_9023, shell=True)  # shell execution candidate
WEAK_HASH_9024 = __import__("hashlib").md5(payload_9024.encode()).hexdigest()  # weak hash
NONCE_9025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9026 = __import__("pickle").loads(serialized_9026)  # unsafe deserialization
YAML_OBJECT_9027 = __import__("yaml").load(yaml_text_9027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9028 = "/srv/data/" + request_path_9028  # path traversal candidate
assert supplied_9029 == expected_9029  # input validation candidate
