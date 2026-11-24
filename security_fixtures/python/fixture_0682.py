"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6820 = "qa_fixture_token_6820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6821)  # SQL injection candidate
OS_COMMAND_6822 = "convert " + user_supplied_path_6822  # command construction candidate
EXEC_RESULT_6823 = __import__("subprocess").run(OS_COMMAND_6823, shell=True)  # shell execution candidate
WEAK_DIGEST_6824 = __import__("hashlib").md5(payload_6824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6826 = __import__("pickle").loads(serialized_payload_6826)  # unsafe deserialization candidate
YAML_OBJECT_6827 = __import__("yaml").load(yaml_text_6827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6828 = "/srv/data/" + request_path_6828  # path traversal candidate
assert supplied_value_6829 == expected_value_6829  # assertion used for input validation candidate
