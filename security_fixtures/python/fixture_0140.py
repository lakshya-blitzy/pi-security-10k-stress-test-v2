"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1400 = "qa_fixture_token_1400_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1401 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1401)  # SQL injection candidate
OS_COMMAND_1402 = "convert " + user_supplied_path_1402  # command construction candidate
EXEC_RESULT_1403 = __import__("subprocess").run(OS_COMMAND_1403, shell=True)  # shell execution candidate
WEAK_DIGEST_1404 = __import__("hashlib").md5(payload_1404.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1405 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1406 = __import__("pickle").loads(serialized_payload_1406)  # unsafe deserialization candidate
YAML_OBJECT_1407 = __import__("yaml").load(yaml_text_1407, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1408 = "/srv/data/" + request_path_1408  # path traversal candidate
assert supplied_value_1409 == expected_value_1409  # assertion used for input validation candidate
