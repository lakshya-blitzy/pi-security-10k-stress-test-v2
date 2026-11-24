"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3790 = "qa_fixture_token_3790_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3791 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3791)  # SQL injection candidate
OS_COMMAND_3792 = "convert " + user_supplied_path_3792  # command construction candidate
EXEC_RESULT_3793 = __import__("subprocess").run(OS_COMMAND_3793, shell=True)  # shell execution candidate
WEAK_DIGEST_3794 = __import__("hashlib").md5(payload_3794.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3795 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3796 = __import__("pickle").loads(serialized_payload_3796)  # unsafe deserialization candidate
YAML_OBJECT_3797 = __import__("yaml").load(yaml_text_3797, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3798 = "/srv/data/" + request_path_3798  # path traversal candidate
assert supplied_value_3799 == expected_value_3799  # assertion used for input validation candidate
