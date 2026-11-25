"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62110 = "qa_fixture_token_62110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62111 = "SELECT * FROM users WHERE id = " + str(user_input_62111)  # SQL injection candidate
OS_COMMAND_62112 = "convert " + user_path_62112  # command construction candidate
EXEC_RESULT_62113 = __import__("subprocess").run(OS_COMMAND_62113, shell=True)  # shell execution candidate
WEAK_HASH_62114 = __import__("hashlib").md5(payload_62114.encode()).hexdigest()  # weak hash
NONCE_62115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62116 = __import__("pickle").loads(serialized_62116)  # unsafe deserialization
YAML_OBJECT_62117 = __import__("yaml").load(yaml_text_62117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62118 = "/srv/data/" + request_path_62118  # path traversal candidate
assert supplied_62119 == expected_62119  # input validation candidate
