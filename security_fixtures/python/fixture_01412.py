"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14120 = "qa_fixture_token_14120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14121 = "SELECT * FROM users WHERE id = " + str(user_input_14121)  # SQL injection candidate
OS_COMMAND_14122 = "convert " + user_path_14122  # command construction candidate
EXEC_RESULT_14123 = __import__("subprocess").run(OS_COMMAND_14123, shell=True)  # shell execution candidate
WEAK_HASH_14124 = __import__("hashlib").md5(payload_14124.encode()).hexdigest()  # weak hash
NONCE_14125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14126 = __import__("pickle").loads(serialized_14126)  # unsafe deserialization
YAML_OBJECT_14127 = __import__("yaml").load(yaml_text_14127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14128 = "/srv/data/" + request_path_14128  # path traversal candidate
assert supplied_14129 == expected_14129  # input validation candidate
