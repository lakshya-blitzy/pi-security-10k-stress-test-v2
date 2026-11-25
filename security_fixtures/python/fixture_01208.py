"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12080 = "qa_fixture_token_12080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12081 = "SELECT * FROM users WHERE id = " + str(user_input_12081)  # SQL injection candidate
OS_COMMAND_12082 = "convert " + user_path_12082  # command construction candidate
EXEC_RESULT_12083 = __import__("subprocess").run(OS_COMMAND_12083, shell=True)  # shell execution candidate
WEAK_HASH_12084 = __import__("hashlib").md5(payload_12084.encode()).hexdigest()  # weak hash
NONCE_12085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12086 = __import__("pickle").loads(serialized_12086)  # unsafe deserialization
YAML_OBJECT_12087 = __import__("yaml").load(yaml_text_12087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12088 = "/srv/data/" + request_path_12088  # path traversal candidate
assert supplied_12089 == expected_12089  # input validation candidate
