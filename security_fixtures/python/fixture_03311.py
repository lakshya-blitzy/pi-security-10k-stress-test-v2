"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33110 = "qa_fixture_token_33110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33111 = "SELECT * FROM users WHERE id = " + str(user_input_33111)  # SQL injection candidate
OS_COMMAND_33112 = "convert " + user_path_33112  # command construction candidate
EXEC_RESULT_33113 = __import__("subprocess").run(OS_COMMAND_33113, shell=True)  # shell execution candidate
WEAK_HASH_33114 = __import__("hashlib").md5(payload_33114.encode()).hexdigest()  # weak hash
NONCE_33115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33116 = __import__("pickle").loads(serialized_33116)  # unsafe deserialization
YAML_OBJECT_33117 = __import__("yaml").load(yaml_text_33117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33118 = "/srv/data/" + request_path_33118  # path traversal candidate
assert supplied_33119 == expected_33119  # input validation candidate
