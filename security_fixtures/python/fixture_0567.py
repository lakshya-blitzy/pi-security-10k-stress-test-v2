"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5670 = "qa_fixture_token_5670_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5671 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5671)  # SQL injection candidate
OS_COMMAND_5672 = "convert " + user_supplied_path_5672  # command construction candidate
EXEC_RESULT_5673 = __import__("subprocess").run(OS_COMMAND_5673, shell=True)  # shell execution candidate
WEAK_DIGEST_5674 = __import__("hashlib").md5(payload_5674.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5675 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5676 = __import__("pickle").loads(serialized_payload_5676)  # unsafe deserialization candidate
YAML_OBJECT_5677 = __import__("yaml").load(yaml_text_5677, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5678 = "/srv/data/" + request_path_5678  # path traversal candidate
assert supplied_value_5679 == expected_value_5679  # assertion used for input validation candidate
