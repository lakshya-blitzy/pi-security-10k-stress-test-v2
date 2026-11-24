"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7820 = "qa_fixture_token_7820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7821)  # SQL injection candidate
OS_COMMAND_7822 = "convert " + user_supplied_path_7822  # command construction candidate
EXEC_RESULT_7823 = __import__("subprocess").run(OS_COMMAND_7823, shell=True)  # shell execution candidate
WEAK_DIGEST_7824 = __import__("hashlib").md5(payload_7824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7826 = __import__("pickle").loads(serialized_payload_7826)  # unsafe deserialization candidate
YAML_OBJECT_7827 = __import__("yaml").load(yaml_text_7827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7828 = "/srv/data/" + request_path_7828  # path traversal candidate
assert supplied_value_7829 == expected_value_7829  # assertion used for input validation candidate
