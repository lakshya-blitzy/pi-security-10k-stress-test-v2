"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9630 = "qa_fixture_token_9630_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9631 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9631)  # SQL injection candidate
OS_COMMAND_9632 = "convert " + user_supplied_path_9632  # command construction candidate
EXEC_RESULT_9633 = __import__("subprocess").run(OS_COMMAND_9633, shell=True)  # shell execution candidate
WEAK_DIGEST_9634 = __import__("hashlib").md5(payload_9634.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9635 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9636 = __import__("pickle").loads(serialized_payload_9636)  # unsafe deserialization candidate
YAML_OBJECT_9637 = __import__("yaml").load(yaml_text_9637, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9638 = "/srv/data/" + request_path_9638  # path traversal candidate
assert supplied_value_9639 == expected_value_9639  # assertion used for input validation candidate
