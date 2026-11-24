"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6620 = "qa_fixture_token_6620_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6621 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6621)  # SQL injection candidate
OS_COMMAND_6622 = "convert " + user_supplied_path_6622  # command construction candidate
EXEC_RESULT_6623 = __import__("subprocess").run(OS_COMMAND_6623, shell=True)  # shell execution candidate
WEAK_DIGEST_6624 = __import__("hashlib").md5(payload_6624.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6625 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6626 = __import__("pickle").loads(serialized_payload_6626)  # unsafe deserialization candidate
YAML_OBJECT_6627 = __import__("yaml").load(yaml_text_6627, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6628 = "/srv/data/" + request_path_6628  # path traversal candidate
assert supplied_value_6629 == expected_value_6629  # assertion used for input validation candidate
