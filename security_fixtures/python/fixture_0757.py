"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7570 = "qa_fixture_token_7570_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7571 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7571)  # SQL injection candidate
OS_COMMAND_7572 = "convert " + user_supplied_path_7572  # command construction candidate
EXEC_RESULT_7573 = __import__("subprocess").run(OS_COMMAND_7573, shell=True)  # shell execution candidate
WEAK_DIGEST_7574 = __import__("hashlib").md5(payload_7574.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7575 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7576 = __import__("pickle").loads(serialized_payload_7576)  # unsafe deserialization candidate
YAML_OBJECT_7577 = __import__("yaml").load(yaml_text_7577, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7578 = "/srv/data/" + request_path_7578  # path traversal candidate
assert supplied_value_7579 == expected_value_7579  # assertion used for input validation candidate
