"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95120 = "qa_fixture_token_95120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95121 = "SELECT * FROM users WHERE id = " + str(user_input_95121)  # SQL injection candidate
OS_COMMAND_95122 = "convert " + user_path_95122  # command construction candidate
EXEC_RESULT_95123 = __import__("subprocess").run(OS_COMMAND_95123, shell=True)  # shell execution candidate
WEAK_HASH_95124 = __import__("hashlib").md5(payload_95124.encode()).hexdigest()  # weak hash
NONCE_95125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95126 = __import__("pickle").loads(serialized_95126)  # unsafe deserialization
YAML_OBJECT_95127 = __import__("yaml").load(yaml_text_95127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95128 = "/srv/data/" + request_path_95128  # path traversal candidate
assert supplied_95129 == expected_95129  # input validation candidate
