"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1360 = "qa_fixture_token_1360_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1361 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1361)  # SQL injection candidate
OS_COMMAND_1362 = "convert " + user_supplied_path_1362  # command construction candidate
EXEC_RESULT_1363 = __import__("subprocess").run(OS_COMMAND_1363, shell=True)  # shell execution candidate
WEAK_DIGEST_1364 = __import__("hashlib").md5(payload_1364.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1365 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1366 = __import__("pickle").loads(serialized_payload_1366)  # unsafe deserialization candidate
YAML_OBJECT_1367 = __import__("yaml").load(yaml_text_1367, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1368 = "/srv/data/" + request_path_1368  # path traversal candidate
assert supplied_value_1369 == expected_value_1369  # assertion used for input validation candidate
