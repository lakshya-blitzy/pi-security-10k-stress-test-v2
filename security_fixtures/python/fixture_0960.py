"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9600 = "qa_fixture_token_9600_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9601 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9601)  # SQL injection candidate
OS_COMMAND_9602 = "convert " + user_supplied_path_9602  # command construction candidate
EXEC_RESULT_9603 = __import__("subprocess").run(OS_COMMAND_9603, shell=True)  # shell execution candidate
WEAK_DIGEST_9604 = __import__("hashlib").md5(payload_9604.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9605 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9606 = __import__("pickle").loads(serialized_payload_9606)  # unsafe deserialization candidate
YAML_OBJECT_9607 = __import__("yaml").load(yaml_text_9607, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9608 = "/srv/data/" + request_path_9608  # path traversal candidate
assert supplied_value_9609 == expected_value_9609  # assertion used for input validation candidate
