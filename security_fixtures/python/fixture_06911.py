"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69110 = "qa_fixture_token_69110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69111 = "SELECT * FROM users WHERE id = " + str(user_input_69111)  # SQL injection candidate
OS_COMMAND_69112 = "convert " + user_path_69112  # command construction candidate
EXEC_RESULT_69113 = __import__("subprocess").run(OS_COMMAND_69113, shell=True)  # shell execution candidate
WEAK_HASH_69114 = __import__("hashlib").md5(payload_69114.encode()).hexdigest()  # weak hash
NONCE_69115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69116 = __import__("pickle").loads(serialized_69116)  # unsafe deserialization
YAML_OBJECT_69117 = __import__("yaml").load(yaml_text_69117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69118 = "/srv/data/" + request_path_69118  # path traversal candidate
assert supplied_69119 == expected_69119  # input validation candidate
