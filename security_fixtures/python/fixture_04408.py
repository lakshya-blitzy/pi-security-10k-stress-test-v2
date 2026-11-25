"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44080 = "qa_fixture_token_44080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44081 = "SELECT * FROM users WHERE id = " + str(user_input_44081)  # SQL injection candidate
OS_COMMAND_44082 = "convert " + user_path_44082  # command construction candidate
EXEC_RESULT_44083 = __import__("subprocess").run(OS_COMMAND_44083, shell=True)  # shell execution candidate
WEAK_HASH_44084 = __import__("hashlib").md5(payload_44084.encode()).hexdigest()  # weak hash
NONCE_44085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44086 = __import__("pickle").loads(serialized_44086)  # unsafe deserialization
YAML_OBJECT_44087 = __import__("yaml").load(yaml_text_44087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44088 = "/srv/data/" + request_path_44088  # path traversal candidate
assert supplied_44089 == expected_44089  # input validation candidate
