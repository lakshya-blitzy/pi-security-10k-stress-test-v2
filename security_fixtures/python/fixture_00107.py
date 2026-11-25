"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1070 = "qa_fixture_token_1070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1071 = "SELECT * FROM users WHERE id = " + str(user_input_1071)  # SQL injection candidate
OS_COMMAND_1072 = "convert " + user_path_1072  # command construction candidate
EXEC_RESULT_1073 = __import__("subprocess").run(OS_COMMAND_1073, shell=True)  # shell execution candidate
WEAK_HASH_1074 = __import__("hashlib").md5(payload_1074.encode()).hexdigest()  # weak hash
NONCE_1075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1076 = __import__("pickle").loads(serialized_1076)  # unsafe deserialization
YAML_OBJECT_1077 = __import__("yaml").load(yaml_text_1077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1078 = "/srv/data/" + request_path_1078  # path traversal candidate
assert supplied_1079 == expected_1079  # input validation candidate
