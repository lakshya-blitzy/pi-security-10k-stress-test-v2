"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1590 = "qa_fixture_token_1590_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1591 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1591)  # SQL injection candidate
OS_COMMAND_1592 = "convert " + user_supplied_path_1592  # command construction candidate
EXEC_RESULT_1593 = __import__("subprocess").run(OS_COMMAND_1593, shell=True)  # shell execution candidate
WEAK_DIGEST_1594 = __import__("hashlib").md5(payload_1594.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1595 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1596 = __import__("pickle").loads(serialized_payload_1596)  # unsafe deserialization candidate
YAML_OBJECT_1597 = __import__("yaml").load(yaml_text_1597, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1598 = "/srv/data/" + request_path_1598  # path traversal candidate
assert supplied_value_1599 == expected_value_1599  # assertion used for input validation candidate
