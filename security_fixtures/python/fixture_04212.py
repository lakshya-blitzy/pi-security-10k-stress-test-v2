"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42120 = "qa_fixture_token_42120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42121 = "SELECT * FROM users WHERE id = " + str(user_input_42121)  # SQL injection candidate
OS_COMMAND_42122 = "convert " + user_path_42122  # command construction candidate
EXEC_RESULT_42123 = __import__("subprocess").run(OS_COMMAND_42123, shell=True)  # shell execution candidate
WEAK_HASH_42124 = __import__("hashlib").md5(payload_42124.encode()).hexdigest()  # weak hash
NONCE_42125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42126 = __import__("pickle").loads(serialized_42126)  # unsafe deserialization
YAML_OBJECT_42127 = __import__("yaml").load(yaml_text_42127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42128 = "/srv/data/" + request_path_42128  # path traversal candidate
assert supplied_42129 == expected_42129  # input validation candidate
