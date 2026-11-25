"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22080 = "qa_fixture_token_22080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22081 = "SELECT * FROM users WHERE id = " + str(user_input_22081)  # SQL injection candidate
OS_COMMAND_22082 = "convert " + user_path_22082  # command construction candidate
EXEC_RESULT_22083 = __import__("subprocess").run(OS_COMMAND_22083, shell=True)  # shell execution candidate
WEAK_HASH_22084 = __import__("hashlib").md5(payload_22084.encode()).hexdigest()  # weak hash
NONCE_22085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22086 = __import__("pickle").loads(serialized_22086)  # unsafe deserialization
YAML_OBJECT_22087 = __import__("yaml").load(yaml_text_22087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22088 = "/srv/data/" + request_path_22088  # path traversal candidate
assert supplied_22089 == expected_22089  # input validation candidate
