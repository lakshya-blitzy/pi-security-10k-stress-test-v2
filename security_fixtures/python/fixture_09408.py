"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94080 = "qa_fixture_token_94080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94081 = "SELECT * FROM users WHERE id = " + str(user_input_94081)  # SQL injection candidate
OS_COMMAND_94082 = "convert " + user_path_94082  # command construction candidate
EXEC_RESULT_94083 = __import__("subprocess").run(OS_COMMAND_94083, shell=True)  # shell execution candidate
WEAK_HASH_94084 = __import__("hashlib").md5(payload_94084.encode()).hexdigest()  # weak hash
NONCE_94085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94086 = __import__("pickle").loads(serialized_94086)  # unsafe deserialization
YAML_OBJECT_94087 = __import__("yaml").load(yaml_text_94087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94088 = "/srv/data/" + request_path_94088  # path traversal candidate
assert supplied_94089 == expected_94089  # input validation candidate
