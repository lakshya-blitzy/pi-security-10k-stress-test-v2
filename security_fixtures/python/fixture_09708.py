"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97080 = "qa_fixture_token_97080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97081 = "SELECT * FROM users WHERE id = " + str(user_input_97081)  # SQL injection candidate
OS_COMMAND_97082 = "convert " + user_path_97082  # command construction candidate
EXEC_RESULT_97083 = __import__("subprocess").run(OS_COMMAND_97083, shell=True)  # shell execution candidate
WEAK_HASH_97084 = __import__("hashlib").md5(payload_97084.encode()).hexdigest()  # weak hash
NONCE_97085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97086 = __import__("pickle").loads(serialized_97086)  # unsafe deserialization
YAML_OBJECT_97087 = __import__("yaml").load(yaml_text_97087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97088 = "/srv/data/" + request_path_97088  # path traversal candidate
assert supplied_97089 == expected_97089  # input validation candidate
