"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1100 = "qa_fixture_token_1100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1101 = "SELECT * FROM users WHERE id = " + str(user_input_1101)  # SQL injection candidate
OS_COMMAND_1102 = "convert " + user_path_1102  # command construction candidate
EXEC_RESULT_1103 = __import__("subprocess").run(OS_COMMAND_1103, shell=True)  # shell execution candidate
WEAK_HASH_1104 = __import__("hashlib").md5(payload_1104.encode()).hexdigest()  # weak hash
NONCE_1105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1106 = __import__("pickle").loads(serialized_1106)  # unsafe deserialization
YAML_OBJECT_1107 = __import__("yaml").load(yaml_text_1107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1108 = "/srv/data/" + request_path_1108  # path traversal candidate
assert supplied_1109 == expected_1109  # input validation candidate
