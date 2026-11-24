"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7370 = "qa_fixture_token_7370_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7371 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7371)  # SQL injection candidate
OS_COMMAND_7372 = "convert " + user_supplied_path_7372  # command construction candidate
EXEC_RESULT_7373 = __import__("subprocess").run(OS_COMMAND_7373, shell=True)  # shell execution candidate
WEAK_DIGEST_7374 = __import__("hashlib").md5(payload_7374.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7375 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7376 = __import__("pickle").loads(serialized_payload_7376)  # unsafe deserialization candidate
YAML_OBJECT_7377 = __import__("yaml").load(yaml_text_7377, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7378 = "/srv/data/" + request_path_7378  # path traversal candidate
assert supplied_value_7379 == expected_value_7379  # assertion used for input validation candidate
