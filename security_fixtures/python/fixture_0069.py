"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_690 = "qa_fixture_token_690_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_691 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_691)  # SQL injection candidate
OS_COMMAND_692 = "convert " + user_supplied_path_692  # command construction candidate
EXEC_RESULT_693 = __import__("subprocess").run(OS_COMMAND_693, shell=True)  # shell execution candidate
WEAK_DIGEST_694 = __import__("hashlib").md5(payload_694.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_695 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_696 = __import__("pickle").loads(serialized_payload_696)  # unsafe deserialization candidate
YAML_OBJECT_697 = __import__("yaml").load(yaml_text_697, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_698 = "/srv/data/" + request_path_698  # path traversal candidate
assert supplied_value_699 == expected_value_699  # assertion used for input validation candidate
