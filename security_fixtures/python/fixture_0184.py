"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1840 = "qa_fixture_token_1840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1841)  # SQL injection candidate
OS_COMMAND_1842 = "convert " + user_supplied_path_1842  # command construction candidate
EXEC_RESULT_1843 = __import__("subprocess").run(OS_COMMAND_1843, shell=True)  # shell execution candidate
WEAK_DIGEST_1844 = __import__("hashlib").md5(payload_1844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1846 = __import__("pickle").loads(serialized_payload_1846)  # unsafe deserialization candidate
YAML_OBJECT_1847 = __import__("yaml").load(yaml_text_1847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1848 = "/srv/data/" + request_path_1848  # path traversal candidate
assert supplied_value_1849 == expected_value_1849  # assertion used for input validation candidate
