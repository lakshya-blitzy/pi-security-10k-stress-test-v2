"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9460 = "qa_fixture_token_9460_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9461 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9461)  # SQL injection candidate
OS_COMMAND_9462 = "convert " + user_supplied_path_9462  # command construction candidate
EXEC_RESULT_9463 = __import__("subprocess").run(OS_COMMAND_9463, shell=True)  # shell execution candidate
WEAK_DIGEST_9464 = __import__("hashlib").md5(payload_9464.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9465 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9466 = __import__("pickle").loads(serialized_payload_9466)  # unsafe deserialization candidate
YAML_OBJECT_9467 = __import__("yaml").load(yaml_text_9467, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9468 = "/srv/data/" + request_path_9468  # path traversal candidate
assert supplied_value_9469 == expected_value_9469  # assertion used for input validation candidate
