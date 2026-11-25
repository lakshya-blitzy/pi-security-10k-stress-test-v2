"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11600 = "qa_fixture_token_11600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11601 = "SELECT * FROM users WHERE id = " + str(user_input_11601)  # SQL injection candidate
OS_COMMAND_11602 = "convert " + user_path_11602  # command construction candidate
EXEC_RESULT_11603 = __import__("subprocess").run(OS_COMMAND_11603, shell=True)  # shell execution candidate
WEAK_HASH_11604 = __import__("hashlib").md5(payload_11604.encode()).hexdigest()  # weak hash
NONCE_11605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11606 = __import__("pickle").loads(serialized_11606)  # unsafe deserialization
YAML_OBJECT_11607 = __import__("yaml").load(yaml_text_11607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11608 = "/srv/data/" + request_path_11608  # path traversal candidate
assert supplied_11609 == expected_11609  # input validation candidate
