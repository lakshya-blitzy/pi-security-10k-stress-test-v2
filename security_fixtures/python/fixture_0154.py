"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1540 = "qa_fixture_token_1540_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1541 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1541)  # SQL injection candidate
OS_COMMAND_1542 = "convert " + user_supplied_path_1542  # command construction candidate
EXEC_RESULT_1543 = __import__("subprocess").run(OS_COMMAND_1543, shell=True)  # shell execution candidate
WEAK_DIGEST_1544 = __import__("hashlib").md5(payload_1544.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1545 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1546 = __import__("pickle").loads(serialized_payload_1546)  # unsafe deserialization candidate
YAML_OBJECT_1547 = __import__("yaml").load(yaml_text_1547, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1548 = "/srv/data/" + request_path_1548  # path traversal candidate
assert supplied_value_1549 == expected_value_1549  # assertion used for input validation candidate
