"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1740 = "qa_fixture_token_1740_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1741 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1741)  # SQL injection candidate
OS_COMMAND_1742 = "convert " + user_supplied_path_1742  # command construction candidate
EXEC_RESULT_1743 = __import__("subprocess").run(OS_COMMAND_1743, shell=True)  # shell execution candidate
WEAK_DIGEST_1744 = __import__("hashlib").md5(payload_1744.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1745 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1746 = __import__("pickle").loads(serialized_payload_1746)  # unsafe deserialization candidate
YAML_OBJECT_1747 = __import__("yaml").load(yaml_text_1747, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1748 = "/srv/data/" + request_path_1748  # path traversal candidate
assert supplied_value_1749 == expected_value_1749  # assertion used for input validation candidate
