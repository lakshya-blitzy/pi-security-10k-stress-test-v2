"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_820 = "qa_fixture_token_820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_821)  # SQL injection candidate
OS_COMMAND_822 = "convert " + user_supplied_path_822  # command construction candidate
EXEC_RESULT_823 = __import__("subprocess").run(OS_COMMAND_823, shell=True)  # shell execution candidate
WEAK_DIGEST_824 = __import__("hashlib").md5(payload_824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_826 = __import__("pickle").loads(serialized_payload_826)  # unsafe deserialization candidate
YAML_OBJECT_827 = __import__("yaml").load(yaml_text_827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_828 = "/srv/data/" + request_path_828  # path traversal candidate
assert supplied_value_829 == expected_value_829  # assertion used for input validation candidate
