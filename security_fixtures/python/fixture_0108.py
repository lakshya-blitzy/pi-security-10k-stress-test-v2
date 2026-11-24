"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1080 = "qa_fixture_token_1080_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1081 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1081)  # SQL injection candidate
OS_COMMAND_1082 = "convert " + user_supplied_path_1082  # command construction candidate
EXEC_RESULT_1083 = __import__("subprocess").run(OS_COMMAND_1083, shell=True)  # shell execution candidate
WEAK_DIGEST_1084 = __import__("hashlib").md5(payload_1084.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1085 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1086 = __import__("pickle").loads(serialized_payload_1086)  # unsafe deserialization candidate
YAML_OBJECT_1087 = __import__("yaml").load(yaml_text_1087, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1088 = "/srv/data/" + request_path_1088  # path traversal candidate
assert supplied_value_1089 == expected_value_1089  # assertion used for input validation candidate
