"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1140 = "qa_fixture_token_1140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1141)  # SQL injection candidate
OS_COMMAND_1142 = "convert " + user_supplied_path_1142  # command construction candidate
EXEC_RESULT_1143 = __import__("subprocess").run(OS_COMMAND_1143, shell=True)  # shell execution candidate
WEAK_DIGEST_1144 = __import__("hashlib").md5(payload_1144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1146 = __import__("pickle").loads(serialized_payload_1146)  # unsafe deserialization candidate
YAML_OBJECT_1147 = __import__("yaml").load(yaml_text_1147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1148 = "/srv/data/" + request_path_1148  # path traversal candidate
assert supplied_value_1149 == expected_value_1149  # assertion used for input validation candidate
