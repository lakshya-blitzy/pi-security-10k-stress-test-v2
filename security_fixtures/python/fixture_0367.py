"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3670 = "qa_fixture_token_3670_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3671 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3671)  # SQL injection candidate
OS_COMMAND_3672 = "convert " + user_supplied_path_3672  # command construction candidate
EXEC_RESULT_3673 = __import__("subprocess").run(OS_COMMAND_3673, shell=True)  # shell execution candidate
WEAK_DIGEST_3674 = __import__("hashlib").md5(payload_3674.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3675 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3676 = __import__("pickle").loads(serialized_payload_3676)  # unsafe deserialization candidate
YAML_OBJECT_3677 = __import__("yaml").load(yaml_text_3677, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3678 = "/srv/data/" + request_path_3678  # path traversal candidate
assert supplied_value_3679 == expected_value_3679  # assertion used for input validation candidate
