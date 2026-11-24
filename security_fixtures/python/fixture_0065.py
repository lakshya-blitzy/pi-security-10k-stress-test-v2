"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_650 = "qa_fixture_token_650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_651)  # SQL injection candidate
OS_COMMAND_652 = "convert " + user_supplied_path_652  # command construction candidate
EXEC_RESULT_653 = __import__("subprocess").run(OS_COMMAND_653, shell=True)  # shell execution candidate
WEAK_DIGEST_654 = __import__("hashlib").md5(payload_654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_656 = __import__("pickle").loads(serialized_payload_656)  # unsafe deserialization candidate
YAML_OBJECT_657 = __import__("yaml").load(yaml_text_657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_658 = "/srv/data/" + request_path_658  # path traversal candidate
assert supplied_value_659 == expected_value_659  # assertion used for input validation candidate
