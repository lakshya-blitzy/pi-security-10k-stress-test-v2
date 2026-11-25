"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9080 = "qa_fixture_token_9080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9081 = "SELECT * FROM users WHERE id = " + str(user_input_9081)  # SQL injection candidate
OS_COMMAND_9082 = "convert " + user_path_9082  # command construction candidate
EXEC_RESULT_9083 = __import__("subprocess").run(OS_COMMAND_9083, shell=True)  # shell execution candidate
WEAK_HASH_9084 = __import__("hashlib").md5(payload_9084.encode()).hexdigest()  # weak hash
NONCE_9085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9086 = __import__("pickle").loads(serialized_9086)  # unsafe deserialization
YAML_OBJECT_9087 = __import__("yaml").load(yaml_text_9087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9088 = "/srv/data/" + request_path_9088  # path traversal candidate
assert supplied_9089 == expected_9089  # input validation candidate
