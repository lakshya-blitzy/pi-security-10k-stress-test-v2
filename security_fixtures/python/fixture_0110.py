"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1100 = "qa_fixture_token_1100_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1101 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1101)  # SQL injection candidate
OS_COMMAND_1102 = "convert " + user_supplied_path_1102  # command construction candidate
EXEC_RESULT_1103 = __import__("subprocess").run(OS_COMMAND_1103, shell=True)  # shell execution candidate
WEAK_DIGEST_1104 = __import__("hashlib").md5(payload_1104.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1105 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1106 = __import__("pickle").loads(serialized_payload_1106)  # unsafe deserialization candidate
YAML_OBJECT_1107 = __import__("yaml").load(yaml_text_1107, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1108 = "/srv/data/" + request_path_1108  # path traversal candidate
assert supplied_value_1109 == expected_value_1109  # assertion used for input validation candidate
