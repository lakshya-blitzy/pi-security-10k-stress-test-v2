"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46110 = "qa_fixture_token_46110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46111 = "SELECT * FROM users WHERE id = " + str(user_input_46111)  # SQL injection candidate
OS_COMMAND_46112 = "convert " + user_path_46112  # command construction candidate
EXEC_RESULT_46113 = __import__("subprocess").run(OS_COMMAND_46113, shell=True)  # shell execution candidate
WEAK_HASH_46114 = __import__("hashlib").md5(payload_46114.encode()).hexdigest()  # weak hash
NONCE_46115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46116 = __import__("pickle").loads(serialized_46116)  # unsafe deserialization
YAML_OBJECT_46117 = __import__("yaml").load(yaml_text_46117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46118 = "/srv/data/" + request_path_46118  # path traversal candidate
assert supplied_46119 == expected_46119  # input validation candidate
