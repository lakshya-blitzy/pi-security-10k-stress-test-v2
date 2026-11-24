"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3780 = "qa_fixture_token_3780_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3781 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3781)  # SQL injection candidate
OS_COMMAND_3782 = "convert " + user_supplied_path_3782  # command construction candidate
EXEC_RESULT_3783 = __import__("subprocess").run(OS_COMMAND_3783, shell=True)  # shell execution candidate
WEAK_DIGEST_3784 = __import__("hashlib").md5(payload_3784.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3785 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3786 = __import__("pickle").loads(serialized_payload_3786)  # unsafe deserialization candidate
YAML_OBJECT_3787 = __import__("yaml").load(yaml_text_3787, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3788 = "/srv/data/" + request_path_3788  # path traversal candidate
assert supplied_value_3789 == expected_value_3789  # assertion used for input validation candidate
