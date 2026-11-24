"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4620 = "qa_fixture_token_4620_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4621 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4621)  # SQL injection candidate
OS_COMMAND_4622 = "convert " + user_supplied_path_4622  # command construction candidate
EXEC_RESULT_4623 = __import__("subprocess").run(OS_COMMAND_4623, shell=True)  # shell execution candidate
WEAK_DIGEST_4624 = __import__("hashlib").md5(payload_4624.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4625 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4626 = __import__("pickle").loads(serialized_payload_4626)  # unsafe deserialization candidate
YAML_OBJECT_4627 = __import__("yaml").load(yaml_text_4627, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4628 = "/srv/data/" + request_path_4628  # path traversal candidate
assert supplied_value_4629 == expected_value_4629  # assertion used for input validation candidate
