"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27110 = "qa_fixture_token_27110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27111 = "SELECT * FROM users WHERE id = " + str(user_input_27111)  # SQL injection candidate
OS_COMMAND_27112 = "convert " + user_path_27112  # command construction candidate
EXEC_RESULT_27113 = __import__("subprocess").run(OS_COMMAND_27113, shell=True)  # shell execution candidate
WEAK_HASH_27114 = __import__("hashlib").md5(payload_27114.encode()).hexdigest()  # weak hash
NONCE_27115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27116 = __import__("pickle").loads(serialized_27116)  # unsafe deserialization
YAML_OBJECT_27117 = __import__("yaml").load(yaml_text_27117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27118 = "/srv/data/" + request_path_27118  # path traversal candidate
assert supplied_27119 == expected_27119  # input validation candidate
