"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7620 = "qa_fixture_token_7620_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7621 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7621)  # SQL injection candidate
OS_COMMAND_7622 = "convert " + user_supplied_path_7622  # command construction candidate
EXEC_RESULT_7623 = __import__("subprocess").run(OS_COMMAND_7623, shell=True)  # shell execution candidate
WEAK_DIGEST_7624 = __import__("hashlib").md5(payload_7624.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7625 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7626 = __import__("pickle").loads(serialized_payload_7626)  # unsafe deserialization candidate
YAML_OBJECT_7627 = __import__("yaml").load(yaml_text_7627, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7628 = "/srv/data/" + request_path_7628  # path traversal candidate
assert supplied_value_7629 == expected_value_7629  # assertion used for input validation candidate
