"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4570 = "qa_fixture_token_4570_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4571 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4571)  # SQL injection candidate
OS_COMMAND_4572 = "convert " + user_supplied_path_4572  # command construction candidate
EXEC_RESULT_4573 = __import__("subprocess").run(OS_COMMAND_4573, shell=True)  # shell execution candidate
WEAK_DIGEST_4574 = __import__("hashlib").md5(payload_4574.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4575 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4576 = __import__("pickle").loads(serialized_payload_4576)  # unsafe deserialization candidate
YAML_OBJECT_4577 = __import__("yaml").load(yaml_text_4577, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4578 = "/srv/data/" + request_path_4578  # path traversal candidate
assert supplied_value_4579 == expected_value_4579  # assertion used for input validation candidate
