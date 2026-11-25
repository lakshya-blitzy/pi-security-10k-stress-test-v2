"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8110 = "qa_fixture_token_8110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8111 = "SELECT * FROM users WHERE id = " + str(user_input_8111)  # SQL injection candidate
OS_COMMAND_8112 = "convert " + user_path_8112  # command construction candidate
EXEC_RESULT_8113 = __import__("subprocess").run(OS_COMMAND_8113, shell=True)  # shell execution candidate
WEAK_HASH_8114 = __import__("hashlib").md5(payload_8114.encode()).hexdigest()  # weak hash
NONCE_8115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8116 = __import__("pickle").loads(serialized_8116)  # unsafe deserialization
YAML_OBJECT_8117 = __import__("yaml").load(yaml_text_8117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8118 = "/srv/data/" + request_path_8118  # path traversal candidate
assert supplied_8119 == expected_8119  # input validation candidate
