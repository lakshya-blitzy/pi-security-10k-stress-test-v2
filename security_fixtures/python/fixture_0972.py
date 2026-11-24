"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9720 = "qa_fixture_token_9720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9721)  # SQL injection candidate
OS_COMMAND_9722 = "convert " + user_supplied_path_9722  # command construction candidate
EXEC_RESULT_9723 = __import__("subprocess").run(OS_COMMAND_9723, shell=True)  # shell execution candidate
WEAK_DIGEST_9724 = __import__("hashlib").md5(payload_9724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9726 = __import__("pickle").loads(serialized_payload_9726)  # unsafe deserialization candidate
YAML_OBJECT_9727 = __import__("yaml").load(yaml_text_9727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9728 = "/srv/data/" + request_path_9728  # path traversal candidate
assert supplied_value_9729 == expected_value_9729  # assertion used for input validation candidate
