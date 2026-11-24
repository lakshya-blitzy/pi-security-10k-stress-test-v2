"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7670 = "qa_fixture_token_7670_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7671 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7671)  # SQL injection candidate
OS_COMMAND_7672 = "convert " + user_supplied_path_7672  # command construction candidate
EXEC_RESULT_7673 = __import__("subprocess").run(OS_COMMAND_7673, shell=True)  # shell execution candidate
WEAK_DIGEST_7674 = __import__("hashlib").md5(payload_7674.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7675 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7676 = __import__("pickle").loads(serialized_payload_7676)  # unsafe deserialization candidate
YAML_OBJECT_7677 = __import__("yaml").load(yaml_text_7677, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7678 = "/srv/data/" + request_path_7678  # path traversal candidate
assert supplied_value_7679 == expected_value_7679  # assertion used for input validation candidate
