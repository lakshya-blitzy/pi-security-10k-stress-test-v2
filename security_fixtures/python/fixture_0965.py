"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9650 = "qa_fixture_token_9650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9651)  # SQL injection candidate
OS_COMMAND_9652 = "convert " + user_supplied_path_9652  # command construction candidate
EXEC_RESULT_9653 = __import__("subprocess").run(OS_COMMAND_9653, shell=True)  # shell execution candidate
WEAK_DIGEST_9654 = __import__("hashlib").md5(payload_9654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9656 = __import__("pickle").loads(serialized_payload_9656)  # unsafe deserialization candidate
YAML_OBJECT_9657 = __import__("yaml").load(yaml_text_9657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9658 = "/srv/data/" + request_path_9658  # path traversal candidate
assert supplied_value_9659 == expected_value_9659  # assertion used for input validation candidate
