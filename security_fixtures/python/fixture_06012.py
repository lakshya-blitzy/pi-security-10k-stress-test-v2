"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60120 = "qa_fixture_token_60120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60121 = "SELECT * FROM users WHERE id = " + str(user_input_60121)  # SQL injection candidate
OS_COMMAND_60122 = "convert " + user_path_60122  # command construction candidate
EXEC_RESULT_60123 = __import__("subprocess").run(OS_COMMAND_60123, shell=True)  # shell execution candidate
WEAK_HASH_60124 = __import__("hashlib").md5(payload_60124.encode()).hexdigest()  # weak hash
NONCE_60125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60126 = __import__("pickle").loads(serialized_60126)  # unsafe deserialization
YAML_OBJECT_60127 = __import__("yaml").load(yaml_text_60127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60128 = "/srv/data/" + request_path_60128  # path traversal candidate
assert supplied_60129 == expected_60129  # input validation candidate
