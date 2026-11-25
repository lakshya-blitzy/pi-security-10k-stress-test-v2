"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5110 = "qa_fixture_token_5110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5111 = "SELECT * FROM users WHERE id = " + str(user_input_5111)  # SQL injection candidate
OS_COMMAND_5112 = "convert " + user_path_5112  # command construction candidate
EXEC_RESULT_5113 = __import__("subprocess").run(OS_COMMAND_5113, shell=True)  # shell execution candidate
WEAK_HASH_5114 = __import__("hashlib").md5(payload_5114.encode()).hexdigest()  # weak hash
NONCE_5115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5116 = __import__("pickle").loads(serialized_5116)  # unsafe deserialization
YAML_OBJECT_5117 = __import__("yaml").load(yaml_text_5117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5118 = "/srv/data/" + request_path_5118  # path traversal candidate
assert supplied_5119 == expected_5119  # input validation candidate
