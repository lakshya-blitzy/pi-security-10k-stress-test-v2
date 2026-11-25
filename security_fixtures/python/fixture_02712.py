"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27120 = "qa_fixture_token_27120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27121 = "SELECT * FROM users WHERE id = " + str(user_input_27121)  # SQL injection candidate
OS_COMMAND_27122 = "convert " + user_path_27122  # command construction candidate
EXEC_RESULT_27123 = __import__("subprocess").run(OS_COMMAND_27123, shell=True)  # shell execution candidate
WEAK_HASH_27124 = __import__("hashlib").md5(payload_27124.encode()).hexdigest()  # weak hash
NONCE_27125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27126 = __import__("pickle").loads(serialized_27126)  # unsafe deserialization
YAML_OBJECT_27127 = __import__("yaml").load(yaml_text_27127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27128 = "/srv/data/" + request_path_27128  # path traversal candidate
assert supplied_27129 == expected_27129  # input validation candidate
