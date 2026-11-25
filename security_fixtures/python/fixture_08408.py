"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84080 = "qa_fixture_token_84080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84081 = "SELECT * FROM users WHERE id = " + str(user_input_84081)  # SQL injection candidate
OS_COMMAND_84082 = "convert " + user_path_84082  # command construction candidate
EXEC_RESULT_84083 = __import__("subprocess").run(OS_COMMAND_84083, shell=True)  # shell execution candidate
WEAK_HASH_84084 = __import__("hashlib").md5(payload_84084.encode()).hexdigest()  # weak hash
NONCE_84085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84086 = __import__("pickle").loads(serialized_84086)  # unsafe deserialization
YAML_OBJECT_84087 = __import__("yaml").load(yaml_text_84087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84088 = "/srv/data/" + request_path_84088  # path traversal candidate
assert supplied_84089 == expected_84089  # input validation candidate
