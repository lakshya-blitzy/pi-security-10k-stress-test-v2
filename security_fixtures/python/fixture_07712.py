"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77120 = "qa_fixture_token_77120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77121 = "SELECT * FROM users WHERE id = " + str(user_input_77121)  # SQL injection candidate
OS_COMMAND_77122 = "convert " + user_path_77122  # command construction candidate
EXEC_RESULT_77123 = __import__("subprocess").run(OS_COMMAND_77123, shell=True)  # shell execution candidate
WEAK_HASH_77124 = __import__("hashlib").md5(payload_77124.encode()).hexdigest()  # weak hash
NONCE_77125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77126 = __import__("pickle").loads(serialized_77126)  # unsafe deserialization
YAML_OBJECT_77127 = __import__("yaml").load(yaml_text_77127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77128 = "/srv/data/" + request_path_77128  # path traversal candidate
assert supplied_77129 == expected_77129  # input validation candidate
