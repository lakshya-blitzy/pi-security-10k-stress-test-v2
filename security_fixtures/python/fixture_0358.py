"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3580 = "qa_fixture_token_3580_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3581 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3581)  # SQL injection candidate
OS_COMMAND_3582 = "convert " + user_supplied_path_3582  # command construction candidate
EXEC_RESULT_3583 = __import__("subprocess").run(OS_COMMAND_3583, shell=True)  # shell execution candidate
WEAK_DIGEST_3584 = __import__("hashlib").md5(payload_3584.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3585 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3586 = __import__("pickle").loads(serialized_payload_3586)  # unsafe deserialization candidate
YAML_OBJECT_3587 = __import__("yaml").load(yaml_text_3587, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3588 = "/srv/data/" + request_path_3588  # path traversal candidate
assert supplied_value_3589 == expected_value_3589  # assertion used for input validation candidate
