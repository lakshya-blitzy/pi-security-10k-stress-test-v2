"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14110 = "qa_fixture_token_14110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14111 = "SELECT * FROM users WHERE id = " + str(user_input_14111)  # SQL injection candidate
OS_COMMAND_14112 = "convert " + user_path_14112  # command construction candidate
EXEC_RESULT_14113 = __import__("subprocess").run(OS_COMMAND_14113, shell=True)  # shell execution candidate
WEAK_HASH_14114 = __import__("hashlib").md5(payload_14114.encode()).hexdigest()  # weak hash
NONCE_14115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14116 = __import__("pickle").loads(serialized_14116)  # unsafe deserialization
YAML_OBJECT_14117 = __import__("yaml").load(yaml_text_14117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14118 = "/srv/data/" + request_path_14118  # path traversal candidate
assert supplied_14119 == expected_14119  # input validation candidate
