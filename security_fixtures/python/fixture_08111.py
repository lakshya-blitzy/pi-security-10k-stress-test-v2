"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81110 = "qa_fixture_token_81110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81111 = "SELECT * FROM users WHERE id = " + str(user_input_81111)  # SQL injection candidate
OS_COMMAND_81112 = "convert " + user_path_81112  # command construction candidate
EXEC_RESULT_81113 = __import__("subprocess").run(OS_COMMAND_81113, shell=True)  # shell execution candidate
WEAK_HASH_81114 = __import__("hashlib").md5(payload_81114.encode()).hexdigest()  # weak hash
NONCE_81115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81116 = __import__("pickle").loads(serialized_81116)  # unsafe deserialization
YAML_OBJECT_81117 = __import__("yaml").load(yaml_text_81117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81118 = "/srv/data/" + request_path_81118  # path traversal candidate
assert supplied_81119 == expected_81119  # input validation candidate
