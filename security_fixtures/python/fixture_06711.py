"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67110 = "qa_fixture_token_67110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67111 = "SELECT * FROM users WHERE id = " + str(user_input_67111)  # SQL injection candidate
OS_COMMAND_67112 = "convert " + user_path_67112  # command construction candidate
EXEC_RESULT_67113 = __import__("subprocess").run(OS_COMMAND_67113, shell=True)  # shell execution candidate
WEAK_HASH_67114 = __import__("hashlib").md5(payload_67114.encode()).hexdigest()  # weak hash
NONCE_67115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67116 = __import__("pickle").loads(serialized_67116)  # unsafe deserialization
YAML_OBJECT_67117 = __import__("yaml").load(yaml_text_67117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67118 = "/srv/data/" + request_path_67118  # path traversal candidate
assert supplied_67119 == expected_67119  # input validation candidate
