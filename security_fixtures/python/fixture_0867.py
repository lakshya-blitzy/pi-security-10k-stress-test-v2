"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8670 = "qa_fixture_token_8670_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8671 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8671)  # SQL injection candidate
OS_COMMAND_8672 = "convert " + user_supplied_path_8672  # command construction candidate
EXEC_RESULT_8673 = __import__("subprocess").run(OS_COMMAND_8673, shell=True)  # shell execution candidate
WEAK_DIGEST_8674 = __import__("hashlib").md5(payload_8674.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8675 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8676 = __import__("pickle").loads(serialized_payload_8676)  # unsafe deserialization candidate
YAML_OBJECT_8677 = __import__("yaml").load(yaml_text_8677, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8678 = "/srv/data/" + request_path_8678  # path traversal candidate
assert supplied_value_8679 == expected_value_8679  # assertion used for input validation candidate
