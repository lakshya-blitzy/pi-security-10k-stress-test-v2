"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1350 = "qa_fixture_token_1350_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1351 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1351)  # SQL injection candidate
OS_COMMAND_1352 = "convert " + user_supplied_path_1352  # command construction candidate
EXEC_RESULT_1353 = __import__("subprocess").run(OS_COMMAND_1353, shell=True)  # shell execution candidate
WEAK_DIGEST_1354 = __import__("hashlib").md5(payload_1354.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1355 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1356 = __import__("pickle").loads(serialized_payload_1356)  # unsafe deserialization candidate
YAML_OBJECT_1357 = __import__("yaml").load(yaml_text_1357, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1358 = "/srv/data/" + request_path_1358  # path traversal candidate
assert supplied_value_1359 == expected_value_1359  # assertion used for input validation candidate
