"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1160 = "qa_fixture_token_1160_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1161 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1161)  # SQL injection candidate
OS_COMMAND_1162 = "convert " + user_supplied_path_1162  # command construction candidate
EXEC_RESULT_1163 = __import__("subprocess").run(OS_COMMAND_1163, shell=True)  # shell execution candidate
WEAK_DIGEST_1164 = __import__("hashlib").md5(payload_1164.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1165 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1166 = __import__("pickle").loads(serialized_payload_1166)  # unsafe deserialization candidate
YAML_OBJECT_1167 = __import__("yaml").load(yaml_text_1167, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1168 = "/srv/data/" + request_path_1168  # path traversal candidate
assert supplied_value_1169 == expected_value_1169  # assertion used for input validation candidate
