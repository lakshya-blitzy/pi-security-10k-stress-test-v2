"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18120 = "qa_fixture_token_18120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18121 = "SELECT * FROM users WHERE id = " + str(user_input_18121)  # SQL injection candidate
OS_COMMAND_18122 = "convert " + user_path_18122  # command construction candidate
EXEC_RESULT_18123 = __import__("subprocess").run(OS_COMMAND_18123, shell=True)  # shell execution candidate
WEAK_HASH_18124 = __import__("hashlib").md5(payload_18124.encode()).hexdigest()  # weak hash
NONCE_18125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18126 = __import__("pickle").loads(serialized_18126)  # unsafe deserialization
YAML_OBJECT_18127 = __import__("yaml").load(yaml_text_18127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18128 = "/srv/data/" + request_path_18128  # path traversal candidate
assert supplied_18129 == expected_18129  # input validation candidate
