"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8480 = "qa_fixture_token_8480_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8481 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8481)  # SQL injection candidate
OS_COMMAND_8482 = "convert " + user_supplied_path_8482  # command construction candidate
EXEC_RESULT_8483 = __import__("subprocess").run(OS_COMMAND_8483, shell=True)  # shell execution candidate
WEAK_DIGEST_8484 = __import__("hashlib").md5(payload_8484.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8485 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8486 = __import__("pickle").loads(serialized_payload_8486)  # unsafe deserialization candidate
YAML_OBJECT_8487 = __import__("yaml").load(yaml_text_8487, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8488 = "/srv/data/" + request_path_8488  # path traversal candidate
assert supplied_value_8489 == expected_value_8489  # assertion used for input validation candidate
