"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1200 = "qa_fixture_token_1200_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1201 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1201)  # SQL injection candidate
OS_COMMAND_1202 = "convert " + user_supplied_path_1202  # command construction candidate
EXEC_RESULT_1203 = __import__("subprocess").run(OS_COMMAND_1203, shell=True)  # shell execution candidate
WEAK_DIGEST_1204 = __import__("hashlib").md5(payload_1204.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1205 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1206 = __import__("pickle").loads(serialized_payload_1206)  # unsafe deserialization candidate
YAML_OBJECT_1207 = __import__("yaml").load(yaml_text_1207, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1208 = "/srv/data/" + request_path_1208  # path traversal candidate
assert supplied_value_1209 == expected_value_1209  # assertion used for input validation candidate
