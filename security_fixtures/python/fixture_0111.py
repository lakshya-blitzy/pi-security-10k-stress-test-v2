"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1110 = "qa_fixture_token_1110_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1111 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1111)  # SQL injection candidate
OS_COMMAND_1112 = "convert " + user_supplied_path_1112  # command construction candidate
EXEC_RESULT_1113 = __import__("subprocess").run(OS_COMMAND_1113, shell=True)  # shell execution candidate
WEAK_DIGEST_1114 = __import__("hashlib").md5(payload_1114.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1115 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1116 = __import__("pickle").loads(serialized_payload_1116)  # unsafe deserialization candidate
YAML_OBJECT_1117 = __import__("yaml").load(yaml_text_1117, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1118 = "/srv/data/" + request_path_1118  # path traversal candidate
assert supplied_value_1119 == expected_value_1119  # assertion used for input validation candidate
