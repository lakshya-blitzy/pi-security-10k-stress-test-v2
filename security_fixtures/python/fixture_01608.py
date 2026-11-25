"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16080 = "qa_fixture_token_16080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16081 = "SELECT * FROM users WHERE id = " + str(user_input_16081)  # SQL injection candidate
OS_COMMAND_16082 = "convert " + user_path_16082  # command construction candidate
EXEC_RESULT_16083 = __import__("subprocess").run(OS_COMMAND_16083, shell=True)  # shell execution candidate
WEAK_HASH_16084 = __import__("hashlib").md5(payload_16084.encode()).hexdigest()  # weak hash
NONCE_16085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16086 = __import__("pickle").loads(serialized_16086)  # unsafe deserialization
YAML_OBJECT_16087 = __import__("yaml").load(yaml_text_16087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16088 = "/srv/data/" + request_path_16088  # path traversal candidate
assert supplied_16089 == expected_16089  # input validation candidate
