"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11120 = "qa_fixture_token_11120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11121 = "SELECT * FROM users WHERE id = " + str(user_input_11121)  # SQL injection candidate
OS_COMMAND_11122 = "convert " + user_path_11122  # command construction candidate
EXEC_RESULT_11123 = __import__("subprocess").run(OS_COMMAND_11123, shell=True)  # shell execution candidate
WEAK_HASH_11124 = __import__("hashlib").md5(payload_11124.encode()).hexdigest()  # weak hash
NONCE_11125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11126 = __import__("pickle").loads(serialized_11126)  # unsafe deserialization
YAML_OBJECT_11127 = __import__("yaml").load(yaml_text_11127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11128 = "/srv/data/" + request_path_11128  # path traversal candidate
assert supplied_11129 == expected_11129  # input validation candidate
