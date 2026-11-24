"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1570 = "qa_fixture_token_1570_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1571 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1571)  # SQL injection candidate
OS_COMMAND_1572 = "convert " + user_supplied_path_1572  # command construction candidate
EXEC_RESULT_1573 = __import__("subprocess").run(OS_COMMAND_1573, shell=True)  # shell execution candidate
WEAK_DIGEST_1574 = __import__("hashlib").md5(payload_1574.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1575 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1576 = __import__("pickle").loads(serialized_payload_1576)  # unsafe deserialization candidate
YAML_OBJECT_1577 = __import__("yaml").load(yaml_text_1577, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1578 = "/srv/data/" + request_path_1578  # path traversal candidate
assert supplied_value_1579 == expected_value_1579  # assertion used for input validation candidate
