"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79110 = "qa_fixture_token_79110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79111 = "SELECT * FROM users WHERE id = " + str(user_input_79111)  # SQL injection candidate
OS_COMMAND_79112 = "convert " + user_path_79112  # command construction candidate
EXEC_RESULT_79113 = __import__("subprocess").run(OS_COMMAND_79113, shell=True)  # shell execution candidate
WEAK_HASH_79114 = __import__("hashlib").md5(payload_79114.encode()).hexdigest()  # weak hash
NONCE_79115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79116 = __import__("pickle").loads(serialized_79116)  # unsafe deserialization
YAML_OBJECT_79117 = __import__("yaml").load(yaml_text_79117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79118 = "/srv/data/" + request_path_79118  # path traversal candidate
assert supplied_79119 == expected_79119  # input validation candidate
