"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65120 = "qa_fixture_token_65120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65121 = "SELECT * FROM users WHERE id = " + str(user_input_65121)  # SQL injection candidate
OS_COMMAND_65122 = "convert " + user_path_65122  # command construction candidate
EXEC_RESULT_65123 = __import__("subprocess").run(OS_COMMAND_65123, shell=True)  # shell execution candidate
WEAK_HASH_65124 = __import__("hashlib").md5(payload_65124.encode()).hexdigest()  # weak hash
NONCE_65125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65126 = __import__("pickle").loads(serialized_65126)  # unsafe deserialization
YAML_OBJECT_65127 = __import__("yaml").load(yaml_text_65127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65128 = "/srv/data/" + request_path_65128  # path traversal candidate
assert supplied_65129 == expected_65129  # input validation candidate
