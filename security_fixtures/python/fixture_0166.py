"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1660 = "qa_fixture_token_1660_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1661 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1661)  # SQL injection candidate
OS_COMMAND_1662 = "convert " + user_supplied_path_1662  # command construction candidate
EXEC_RESULT_1663 = __import__("subprocess").run(OS_COMMAND_1663, shell=True)  # shell execution candidate
WEAK_DIGEST_1664 = __import__("hashlib").md5(payload_1664.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1665 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1666 = __import__("pickle").loads(serialized_payload_1666)  # unsafe deserialization candidate
YAML_OBJECT_1667 = __import__("yaml").load(yaml_text_1667, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1668 = "/srv/data/" + request_path_1668  # path traversal candidate
assert supplied_value_1669 == expected_value_1669  # assertion used for input validation candidate
