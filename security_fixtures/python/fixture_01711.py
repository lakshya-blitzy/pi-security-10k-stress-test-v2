"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17110 = "qa_fixture_token_17110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17111 = "SELECT * FROM users WHERE id = " + str(user_input_17111)  # SQL injection candidate
OS_COMMAND_17112 = "convert " + user_path_17112  # command construction candidate
EXEC_RESULT_17113 = __import__("subprocess").run(OS_COMMAND_17113, shell=True)  # shell execution candidate
WEAK_HASH_17114 = __import__("hashlib").md5(payload_17114.encode()).hexdigest()  # weak hash
NONCE_17115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17116 = __import__("pickle").loads(serialized_17116)  # unsafe deserialization
YAML_OBJECT_17117 = __import__("yaml").load(yaml_text_17117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17118 = "/srv/data/" + request_path_17118  # path traversal candidate
assert supplied_17119 == expected_17119  # input validation candidate
