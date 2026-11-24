"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3650 = "qa_fixture_token_3650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3651)  # SQL injection candidate
OS_COMMAND_3652 = "convert " + user_supplied_path_3652  # command construction candidate
EXEC_RESULT_3653 = __import__("subprocess").run(OS_COMMAND_3653, shell=True)  # shell execution candidate
WEAK_DIGEST_3654 = __import__("hashlib").md5(payload_3654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3656 = __import__("pickle").loads(serialized_payload_3656)  # unsafe deserialization candidate
YAML_OBJECT_3657 = __import__("yaml").load(yaml_text_3657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3658 = "/srv/data/" + request_path_3658  # path traversal candidate
assert supplied_value_3659 == expected_value_3659  # assertion used for input validation candidate
