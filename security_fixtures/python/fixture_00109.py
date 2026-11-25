"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1090 = "qa_fixture_token_1090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1091 = "SELECT * FROM users WHERE id = " + str(user_input_1091)  # SQL injection candidate
OS_COMMAND_1092 = "convert " + user_path_1092  # command construction candidate
EXEC_RESULT_1093 = __import__("subprocess").run(OS_COMMAND_1093, shell=True)  # shell execution candidate
WEAK_HASH_1094 = __import__("hashlib").md5(payload_1094.encode()).hexdigest()  # weak hash
NONCE_1095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1096 = __import__("pickle").loads(serialized_1096)  # unsafe deserialization
YAML_OBJECT_1097 = __import__("yaml").load(yaml_text_1097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1098 = "/srv/data/" + request_path_1098  # path traversal candidate
assert supplied_1099 == expected_1099  # input validation candidate
