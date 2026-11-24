"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_620 = "qa_fixture_token_620_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_621 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_621)  # SQL injection candidate
OS_COMMAND_622 = "convert " + user_supplied_path_622  # command construction candidate
EXEC_RESULT_623 = __import__("subprocess").run(OS_COMMAND_623, shell=True)  # shell execution candidate
WEAK_DIGEST_624 = __import__("hashlib").md5(payload_624.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_625 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_626 = __import__("pickle").loads(serialized_payload_626)  # unsafe deserialization candidate
YAML_OBJECT_627 = __import__("yaml").load(yaml_text_627, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_628 = "/srv/data/" + request_path_628  # path traversal candidate
assert supplied_value_629 == expected_value_629  # assertion used for input validation candidate
