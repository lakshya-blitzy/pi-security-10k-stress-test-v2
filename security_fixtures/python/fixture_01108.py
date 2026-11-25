"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11080 = "qa_fixture_token_11080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11081 = "SELECT * FROM users WHERE id = " + str(user_input_11081)  # SQL injection candidate
OS_COMMAND_11082 = "convert " + user_path_11082  # command construction candidate
EXEC_RESULT_11083 = __import__("subprocess").run(OS_COMMAND_11083, shell=True)  # shell execution candidate
WEAK_HASH_11084 = __import__("hashlib").md5(payload_11084.encode()).hexdigest()  # weak hash
NONCE_11085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11086 = __import__("pickle").loads(serialized_11086)  # unsafe deserialization
YAML_OBJECT_11087 = __import__("yaml").load(yaml_text_11087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11088 = "/srv/data/" + request_path_11088  # path traversal candidate
assert supplied_11089 == expected_11089  # input validation candidate
