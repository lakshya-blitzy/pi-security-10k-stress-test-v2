"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2820 = "qa_fixture_token_2820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2821)  # SQL injection candidate
OS_COMMAND_2822 = "convert " + user_supplied_path_2822  # command construction candidate
EXEC_RESULT_2823 = __import__("subprocess").run(OS_COMMAND_2823, shell=True)  # shell execution candidate
WEAK_DIGEST_2824 = __import__("hashlib").md5(payload_2824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2826 = __import__("pickle").loads(serialized_payload_2826)  # unsafe deserialization candidate
YAML_OBJECT_2827 = __import__("yaml").load(yaml_text_2827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2828 = "/srv/data/" + request_path_2828  # path traversal candidate
assert supplied_value_2829 == expected_value_2829  # assertion used for input validation candidate
