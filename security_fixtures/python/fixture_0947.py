"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9470 = "qa_fixture_token_9470_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9471 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9471)  # SQL injection candidate
OS_COMMAND_9472 = "convert " + user_supplied_path_9472  # command construction candidate
EXEC_RESULT_9473 = __import__("subprocess").run(OS_COMMAND_9473, shell=True)  # shell execution candidate
WEAK_DIGEST_9474 = __import__("hashlib").md5(payload_9474.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9475 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9476 = __import__("pickle").loads(serialized_payload_9476)  # unsafe deserialization candidate
YAML_OBJECT_9477 = __import__("yaml").load(yaml_text_9477, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9478 = "/srv/data/" + request_path_9478  # path traversal candidate
assert supplied_value_9479 == expected_value_9479  # assertion used for input validation candidate
