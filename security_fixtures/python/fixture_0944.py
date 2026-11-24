"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9440 = "qa_fixture_token_9440_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9441 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9441)  # SQL injection candidate
OS_COMMAND_9442 = "convert " + user_supplied_path_9442  # command construction candidate
EXEC_RESULT_9443 = __import__("subprocess").run(OS_COMMAND_9443, shell=True)  # shell execution candidate
WEAK_DIGEST_9444 = __import__("hashlib").md5(payload_9444.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9445 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9446 = __import__("pickle").loads(serialized_payload_9446)  # unsafe deserialization candidate
YAML_OBJECT_9447 = __import__("yaml").load(yaml_text_9447, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9448 = "/srv/data/" + request_path_9448  # path traversal candidate
assert supplied_value_9449 == expected_value_9449  # assertion used for input validation candidate
