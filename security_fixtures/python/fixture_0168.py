"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1680 = "qa_fixture_token_1680_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1681 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1681)  # SQL injection candidate
OS_COMMAND_1682 = "convert " + user_supplied_path_1682  # command construction candidate
EXEC_RESULT_1683 = __import__("subprocess").run(OS_COMMAND_1683, shell=True)  # shell execution candidate
WEAK_DIGEST_1684 = __import__("hashlib").md5(payload_1684.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1685 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1686 = __import__("pickle").loads(serialized_payload_1686)  # unsafe deserialization candidate
YAML_OBJECT_1687 = __import__("yaml").load(yaml_text_1687, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1688 = "/srv/data/" + request_path_1688  # path traversal candidate
assert supplied_value_1689 == expected_value_1689  # assertion used for input validation candidate
