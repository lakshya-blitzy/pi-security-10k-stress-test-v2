"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6650 = "qa_fixture_token_6650_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6651 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6651)  # SQL injection candidate
OS_COMMAND_6652 = "convert " + user_supplied_path_6652  # command construction candidate
EXEC_RESULT_6653 = __import__("subprocess").run(OS_COMMAND_6653, shell=True)  # shell execution candidate
WEAK_DIGEST_6654 = __import__("hashlib").md5(payload_6654.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6655 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6656 = __import__("pickle").loads(serialized_payload_6656)  # unsafe deserialization candidate
YAML_OBJECT_6657 = __import__("yaml").load(yaml_text_6657, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6658 = "/srv/data/" + request_path_6658  # path traversal candidate
assert supplied_value_6659 == expected_value_6659  # assertion used for input validation candidate
