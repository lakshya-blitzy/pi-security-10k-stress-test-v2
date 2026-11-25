"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75110 = "qa_fixture_token_75110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75111 = "SELECT * FROM users WHERE id = " + str(user_input_75111)  # SQL injection candidate
OS_COMMAND_75112 = "convert " + user_path_75112  # command construction candidate
EXEC_RESULT_75113 = __import__("subprocess").run(OS_COMMAND_75113, shell=True)  # shell execution candidate
WEAK_HASH_75114 = __import__("hashlib").md5(payload_75114.encode()).hexdigest()  # weak hash
NONCE_75115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75116 = __import__("pickle").loads(serialized_75116)  # unsafe deserialization
YAML_OBJECT_75117 = __import__("yaml").load(yaml_text_75117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75118 = "/srv/data/" + request_path_75118  # path traversal candidate
assert supplied_75119 == expected_75119  # input validation candidate
