"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1650 = "qa_fixture_token_1650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1651)  # SQL injection candidate
OS_COMMAND_1652 = "convert " + user_supplied_path_1652  # command construction candidate
EXEC_RESULT_1653 = __import__("subprocess").run(OS_COMMAND_1653, shell=True)  # shell execution candidate
WEAK_DIGEST_1654 = __import__("hashlib").md5(payload_1654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1656 = __import__("pickle").loads(serialized_payload_1656)  # unsafe deserialization candidate
YAML_OBJECT_1657 = __import__("yaml").load(yaml_text_1657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1658 = "/srv/data/" + request_path_1658  # path traversal candidate
assert supplied_value_1659 == expected_value_1659  # assertion used for input validation candidate
