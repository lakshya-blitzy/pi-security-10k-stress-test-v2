"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3480 = "qa_fixture_token_3480_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3481 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3481)  # SQL injection candidate
OS_COMMAND_3482 = "convert " + user_supplied_path_3482  # command construction candidate
EXEC_RESULT_3483 = __import__("subprocess").run(OS_COMMAND_3483, shell=True)  # shell execution candidate
WEAK_DIGEST_3484 = __import__("hashlib").md5(payload_3484.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3485 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3486 = __import__("pickle").loads(serialized_payload_3486)  # unsafe deserialization candidate
YAML_OBJECT_3487 = __import__("yaml").load(yaml_text_3487, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3488 = "/srv/data/" + request_path_3488  # path traversal candidate
assert supplied_value_3489 == expected_value_3489  # assertion used for input validation candidate
