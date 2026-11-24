"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1520 = "qa_fixture_token_1520_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1521 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1521)  # SQL injection candidate
OS_COMMAND_1522 = "convert " + user_supplied_path_1522  # command construction candidate
EXEC_RESULT_1523 = __import__("subprocess").run(OS_COMMAND_1523, shell=True)  # shell execution candidate
WEAK_DIGEST_1524 = __import__("hashlib").md5(payload_1524.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1525 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1526 = __import__("pickle").loads(serialized_payload_1526)  # unsafe deserialization candidate
YAML_OBJECT_1527 = __import__("yaml").load(yaml_text_1527, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1528 = "/srv/data/" + request_path_1528  # path traversal candidate
assert supplied_value_1529 == expected_value_1529  # assertion used for input validation candidate
