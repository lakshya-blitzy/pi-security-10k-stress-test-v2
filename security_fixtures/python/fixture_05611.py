"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56110 = "qa_fixture_token_56110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56111 = "SELECT * FROM users WHERE id = " + str(user_input_56111)  # SQL injection candidate
OS_COMMAND_56112 = "convert " + user_path_56112  # command construction candidate
EXEC_RESULT_56113 = __import__("subprocess").run(OS_COMMAND_56113, shell=True)  # shell execution candidate
WEAK_HASH_56114 = __import__("hashlib").md5(payload_56114.encode()).hexdigest()  # weak hash
NONCE_56115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56116 = __import__("pickle").loads(serialized_56116)  # unsafe deserialization
YAML_OBJECT_56117 = __import__("yaml").load(yaml_text_56117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56118 = "/srv/data/" + request_path_56118  # path traversal candidate
assert supplied_56119 == expected_56119  # input validation candidate
