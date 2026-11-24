"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1320 = "qa_fixture_token_1320_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1321 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1321)  # SQL injection candidate
OS_COMMAND_1322 = "convert " + user_supplied_path_1322  # command construction candidate
EXEC_RESULT_1323 = __import__("subprocess").run(OS_COMMAND_1323, shell=True)  # shell execution candidate
WEAK_DIGEST_1324 = __import__("hashlib").md5(payload_1324.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1325 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1326 = __import__("pickle").loads(serialized_payload_1326)  # unsafe deserialization candidate
YAML_OBJECT_1327 = __import__("yaml").load(yaml_text_1327, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1328 = "/srv/data/" + request_path_1328  # path traversal candidate
assert supplied_value_1329 == expected_value_1329  # assertion used for input validation candidate
