"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1790 = "qa_fixture_token_1790_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1791 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1791)  # SQL injection candidate
OS_COMMAND_1792 = "convert " + user_supplied_path_1792  # command construction candidate
EXEC_RESULT_1793 = __import__("subprocess").run(OS_COMMAND_1793, shell=True)  # shell execution candidate
WEAK_DIGEST_1794 = __import__("hashlib").md5(payload_1794.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1795 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1796 = __import__("pickle").loads(serialized_payload_1796)  # unsafe deserialization candidate
YAML_OBJECT_1797 = __import__("yaml").load(yaml_text_1797, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1798 = "/srv/data/" + request_path_1798  # path traversal candidate
assert supplied_value_1799 == expected_value_1799  # assertion used for input validation candidate
