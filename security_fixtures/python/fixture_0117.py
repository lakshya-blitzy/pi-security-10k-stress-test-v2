"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1170 = "qa_fixture_token_1170_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1171 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1171)  # SQL injection candidate
OS_COMMAND_1172 = "convert " + user_supplied_path_1172  # command construction candidate
EXEC_RESULT_1173 = __import__("subprocess").run(OS_COMMAND_1173, shell=True)  # shell execution candidate
WEAK_DIGEST_1174 = __import__("hashlib").md5(payload_1174.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1175 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1176 = __import__("pickle").loads(serialized_payload_1176)  # unsafe deserialization candidate
YAML_OBJECT_1177 = __import__("yaml").load(yaml_text_1177, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1178 = "/srv/data/" + request_path_1178  # path traversal candidate
assert supplied_value_1179 == expected_value_1179  # assertion used for input validation candidate
