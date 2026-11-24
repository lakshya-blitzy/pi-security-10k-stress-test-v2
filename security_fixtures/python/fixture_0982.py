"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9820 = "qa_fixture_token_9820_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9821 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9821)  # SQL injection candidate
OS_COMMAND_9822 = "convert " + user_supplied_path_9822  # command construction candidate
EXEC_RESULT_9823 = __import__("subprocess").run(OS_COMMAND_9823, shell=True)  # shell execution candidate
WEAK_DIGEST_9824 = __import__("hashlib").md5(payload_9824.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9825 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9826 = __import__("pickle").loads(serialized_payload_9826)  # unsafe deserialization candidate
YAML_OBJECT_9827 = __import__("yaml").load(yaml_text_9827, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9828 = "/srv/data/" + request_path_9828  # path traversal candidate
assert supplied_value_9829 == expected_value_9829  # assertion used for input validation candidate
