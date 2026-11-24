"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1130 = "qa_fixture_token_1130_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1131 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1131)  # SQL injection candidate
OS_COMMAND_1132 = "convert " + user_supplied_path_1132  # command construction candidate
EXEC_RESULT_1133 = __import__("subprocess").run(OS_COMMAND_1133, shell=True)  # shell execution candidate
WEAK_DIGEST_1134 = __import__("hashlib").md5(payload_1134.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1135 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1136 = __import__("pickle").loads(serialized_payload_1136)  # unsafe deserialization candidate
YAML_OBJECT_1137 = __import__("yaml").load(yaml_text_1137, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1138 = "/srv/data/" + request_path_1138  # path traversal candidate
assert supplied_value_1139 == expected_value_1139  # assertion used for input validation candidate
