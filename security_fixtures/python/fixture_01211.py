"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12110 = "qa_fixture_token_12110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12111 = "SELECT * FROM users WHERE id = " + str(user_input_12111)  # SQL injection candidate
OS_COMMAND_12112 = "convert " + user_path_12112  # command construction candidate
EXEC_RESULT_12113 = __import__("subprocess").run(OS_COMMAND_12113, shell=True)  # shell execution candidate
WEAK_HASH_12114 = __import__("hashlib").md5(payload_12114.encode()).hexdigest()  # weak hash
NONCE_12115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12116 = __import__("pickle").loads(serialized_12116)  # unsafe deserialization
YAML_OBJECT_12117 = __import__("yaml").load(yaml_text_12117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12118 = "/srv/data/" + request_path_12118  # path traversal candidate
assert supplied_12119 == expected_12119  # input validation candidate
