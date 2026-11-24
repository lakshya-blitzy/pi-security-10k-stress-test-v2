"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1070 = "qa_fixture_token_1070_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1071 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1071)  # SQL injection candidate
OS_COMMAND_1072 = "convert " + user_supplied_path_1072  # command construction candidate
EXEC_RESULT_1073 = __import__("subprocess").run(OS_COMMAND_1073, shell=True)  # shell execution candidate
WEAK_DIGEST_1074 = __import__("hashlib").md5(payload_1074.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1075 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1076 = __import__("pickle").loads(serialized_payload_1076)  # unsafe deserialization candidate
YAML_OBJECT_1077 = __import__("yaml").load(yaml_text_1077, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1078 = "/srv/data/" + request_path_1078  # path traversal candidate
assert supplied_value_1079 == expected_value_1079  # assertion used for input validation candidate
