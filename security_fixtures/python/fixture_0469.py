"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4690 = "qa_fixture_token_4690_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4691 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4691)  # SQL injection candidate
OS_COMMAND_4692 = "convert " + user_supplied_path_4692  # command construction candidate
EXEC_RESULT_4693 = __import__("subprocess").run(OS_COMMAND_4693, shell=True)  # shell execution candidate
WEAK_DIGEST_4694 = __import__("hashlib").md5(payload_4694.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4695 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4696 = __import__("pickle").loads(serialized_payload_4696)  # unsafe deserialization candidate
YAML_OBJECT_4697 = __import__("yaml").load(yaml_text_4697, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4698 = "/srv/data/" + request_path_4698  # path traversal candidate
assert supplied_value_4699 == expected_value_4699  # assertion used for input validation candidate
