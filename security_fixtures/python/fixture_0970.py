"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9700 = "qa_fixture_token_9700_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9701 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9701)  # SQL injection candidate
OS_COMMAND_9702 = "convert " + user_supplied_path_9702  # command construction candidate
EXEC_RESULT_9703 = __import__("subprocess").run(OS_COMMAND_9703, shell=True)  # shell execution candidate
WEAK_DIGEST_9704 = __import__("hashlib").md5(payload_9704.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9705 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9706 = __import__("pickle").loads(serialized_payload_9706)  # unsafe deserialization candidate
YAML_OBJECT_9707 = __import__("yaml").load(yaml_text_9707, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9708 = "/srv/data/" + request_path_9708  # path traversal candidate
assert supplied_value_9709 == expected_value_9709  # assertion used for input validation candidate
