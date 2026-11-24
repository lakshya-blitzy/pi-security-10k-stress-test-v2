"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1820 = "qa_fixture_token_1820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1821)  # SQL injection candidate
OS_COMMAND_1822 = "convert " + user_supplied_path_1822  # command construction candidate
EXEC_RESULT_1823 = __import__("subprocess").run(OS_COMMAND_1823, shell=True)  # shell execution candidate
WEAK_DIGEST_1824 = __import__("hashlib").md5(payload_1824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1826 = __import__("pickle").loads(serialized_payload_1826)  # unsafe deserialization candidate
YAML_OBJECT_1827 = __import__("yaml").load(yaml_text_1827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1828 = "/srv/data/" + request_path_1828  # path traversal candidate
assert supplied_value_1829 == expected_value_1829  # assertion used for input validation candidate
