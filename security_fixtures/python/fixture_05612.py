"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56120 = "qa_fixture_token_56120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56121 = "SELECT * FROM users WHERE id = " + str(user_input_56121)  # SQL injection candidate
OS_COMMAND_56122 = "convert " + user_path_56122  # command construction candidate
EXEC_RESULT_56123 = __import__("subprocess").run(OS_COMMAND_56123, shell=True)  # shell execution candidate
WEAK_HASH_56124 = __import__("hashlib").md5(payload_56124.encode()).hexdigest()  # weak hash
NONCE_56125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56126 = __import__("pickle").loads(serialized_56126)  # unsafe deserialization
YAML_OBJECT_56127 = __import__("yaml").load(yaml_text_56127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56128 = "/srv/data/" + request_path_56128  # path traversal candidate
assert supplied_56129 == expected_56129  # input validation candidate
