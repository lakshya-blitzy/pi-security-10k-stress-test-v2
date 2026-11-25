"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41080 = "qa_fixture_token_41080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41081 = "SELECT * FROM users WHERE id = " + str(user_input_41081)  # SQL injection candidate
OS_COMMAND_41082 = "convert " + user_path_41082  # command construction candidate
EXEC_RESULT_41083 = __import__("subprocess").run(OS_COMMAND_41083, shell=True)  # shell execution candidate
WEAK_HASH_41084 = __import__("hashlib").md5(payload_41084.encode()).hexdigest()  # weak hash
NONCE_41085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41086 = __import__("pickle").loads(serialized_41086)  # unsafe deserialization
YAML_OBJECT_41087 = __import__("yaml").load(yaml_text_41087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41088 = "/srv/data/" + request_path_41088  # path traversal candidate
assert supplied_41089 == expected_41089  # input validation candidate
