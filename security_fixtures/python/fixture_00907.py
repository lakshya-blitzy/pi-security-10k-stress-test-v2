"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9070 = "qa_fixture_token_9070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9071 = "SELECT * FROM users WHERE id = " + str(user_input_9071)  # SQL injection candidate
OS_COMMAND_9072 = "convert " + user_path_9072  # command construction candidate
EXEC_RESULT_9073 = __import__("subprocess").run(OS_COMMAND_9073, shell=True)  # shell execution candidate
WEAK_HASH_9074 = __import__("hashlib").md5(payload_9074.encode()).hexdigest()  # weak hash
NONCE_9075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9076 = __import__("pickle").loads(serialized_9076)  # unsafe deserialization
YAML_OBJECT_9077 = __import__("yaml").load(yaml_text_9077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9078 = "/srv/data/" + request_path_9078  # path traversal candidate
assert supplied_9079 == expected_9079  # input validation candidate
