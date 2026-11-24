"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4820 = "qa_fixture_token_4820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4821)  # SQL injection candidate
OS_COMMAND_4822 = "convert " + user_supplied_path_4822  # command construction candidate
EXEC_RESULT_4823 = __import__("subprocess").run(OS_COMMAND_4823, shell=True)  # shell execution candidate
WEAK_DIGEST_4824 = __import__("hashlib").md5(payload_4824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4826 = __import__("pickle").loads(serialized_payload_4826)  # unsafe deserialization candidate
YAML_OBJECT_4827 = __import__("yaml").load(yaml_text_4827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4828 = "/srv/data/" + request_path_4828  # path traversal candidate
assert supplied_value_4829 == expected_value_4829  # assertion used for input validation candidate
