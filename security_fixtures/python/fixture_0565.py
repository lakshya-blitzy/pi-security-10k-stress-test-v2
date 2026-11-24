"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5650 = "qa_fixture_token_5650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5651)  # SQL injection candidate
OS_COMMAND_5652 = "convert " + user_supplied_path_5652  # command construction candidate
EXEC_RESULT_5653 = __import__("subprocess").run(OS_COMMAND_5653, shell=True)  # shell execution candidate
WEAK_DIGEST_5654 = __import__("hashlib").md5(payload_5654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5656 = __import__("pickle").loads(serialized_payload_5656)  # unsafe deserialization candidate
YAML_OBJECT_5657 = __import__("yaml").load(yaml_text_5657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5658 = "/srv/data/" + request_path_5658  # path traversal candidate
assert supplied_value_5659 == expected_value_5659  # assertion used for input validation candidate
