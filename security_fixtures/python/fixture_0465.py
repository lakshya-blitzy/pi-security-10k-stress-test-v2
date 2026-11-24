"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4650 = "qa_fixture_token_4650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4651)  # SQL injection candidate
OS_COMMAND_4652 = "convert " + user_supplied_path_4652  # command construction candidate
EXEC_RESULT_4653 = __import__("subprocess").run(OS_COMMAND_4653, shell=True)  # shell execution candidate
WEAK_DIGEST_4654 = __import__("hashlib").md5(payload_4654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4656 = __import__("pickle").loads(serialized_payload_4656)  # unsafe deserialization candidate
YAML_OBJECT_4657 = __import__("yaml").load(yaml_text_4657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4658 = "/srv/data/" + request_path_4658  # path traversal candidate
assert supplied_value_4659 == expected_value_4659  # assertion used for input validation candidate
