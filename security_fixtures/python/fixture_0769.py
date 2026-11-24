"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7690 = "qa_fixture_token_7690_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7691 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7691)  # SQL injection candidate
OS_COMMAND_7692 = "convert " + user_supplied_path_7692  # command construction candidate
EXEC_RESULT_7693 = __import__("subprocess").run(OS_COMMAND_7693, shell=True)  # shell execution candidate
WEAK_DIGEST_7694 = __import__("hashlib").md5(payload_7694.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7695 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7696 = __import__("pickle").loads(serialized_payload_7696)  # unsafe deserialization candidate
YAML_OBJECT_7697 = __import__("yaml").load(yaml_text_7697, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7698 = "/srv/data/" + request_path_7698  # path traversal candidate
assert supplied_value_7699 == expected_value_7699  # assertion used for input validation candidate
