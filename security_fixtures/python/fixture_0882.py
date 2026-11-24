"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8820 = "qa_fixture_token_8820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8821)  # SQL injection candidate
OS_COMMAND_8822 = "convert " + user_supplied_path_8822  # command construction candidate
EXEC_RESULT_8823 = __import__("subprocess").run(OS_COMMAND_8823, shell=True)  # shell execution candidate
WEAK_DIGEST_8824 = __import__("hashlib").md5(payload_8824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8826 = __import__("pickle").loads(serialized_payload_8826)  # unsafe deserialization candidate
YAML_OBJECT_8827 = __import__("yaml").load(yaml_text_8827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8828 = "/srv/data/" + request_path_8828  # path traversal candidate
assert supplied_value_8829 == expected_value_8829  # assertion used for input validation candidate
