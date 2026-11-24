"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1690 = "qa_fixture_token_1690_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1691 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1691)  # SQL injection candidate
OS_COMMAND_1692 = "convert " + user_supplied_path_1692  # command construction candidate
EXEC_RESULT_1693 = __import__("subprocess").run(OS_COMMAND_1693, shell=True)  # shell execution candidate
WEAK_DIGEST_1694 = __import__("hashlib").md5(payload_1694.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1695 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1696 = __import__("pickle").loads(serialized_payload_1696)  # unsafe deserialization candidate
YAML_OBJECT_1697 = __import__("yaml").load(yaml_text_1697, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1698 = "/srv/data/" + request_path_1698  # path traversal candidate
assert supplied_value_1699 == expected_value_1699  # assertion used for input validation candidate
