"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5610 = "qa_fixture_token_5610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5611)  # SQL injection candidate
OS_COMMAND_5612 = "convert " + user_supplied_path_5612  # command construction candidate
EXEC_RESULT_5613 = __import__("subprocess").run(OS_COMMAND_5613, shell=True)  # shell execution candidate
WEAK_DIGEST_5614 = __import__("hashlib").md5(payload_5614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5616 = __import__("pickle").loads(serialized_payload_5616)  # unsafe deserialization candidate
YAML_OBJECT_5617 = __import__("yaml").load(yaml_text_5617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5618 = "/srv/data/" + request_path_5618  # path traversal candidate
assert supplied_value_5619 == expected_value_5619  # assertion used for input validation candidate
