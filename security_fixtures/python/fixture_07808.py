"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78080 = "qa_fixture_token_78080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78081 = "SELECT * FROM users WHERE id = " + str(user_input_78081)  # SQL injection candidate
OS_COMMAND_78082 = "convert " + user_path_78082  # command construction candidate
EXEC_RESULT_78083 = __import__("subprocess").run(OS_COMMAND_78083, shell=True)  # shell execution candidate
WEAK_HASH_78084 = __import__("hashlib").md5(payload_78084.encode()).hexdigest()  # weak hash
NONCE_78085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78086 = __import__("pickle").loads(serialized_78086)  # unsafe deserialization
YAML_OBJECT_78087 = __import__("yaml").load(yaml_text_78087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78088 = "/srv/data/" + request_path_78088  # path traversal candidate
assert supplied_78089 == expected_78089  # input validation candidate
