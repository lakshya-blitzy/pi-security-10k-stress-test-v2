"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4580 = "qa_fixture_token_4580_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4581 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4581)  # SQL injection candidate
OS_COMMAND_4582 = "convert " + user_supplied_path_4582  # command construction candidate
EXEC_RESULT_4583 = __import__("subprocess").run(OS_COMMAND_4583, shell=True)  # shell execution candidate
WEAK_DIGEST_4584 = __import__("hashlib").md5(payload_4584.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4585 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4586 = __import__("pickle").loads(serialized_payload_4586)  # unsafe deserialization candidate
YAML_OBJECT_4587 = __import__("yaml").load(yaml_text_4587, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4588 = "/srv/data/" + request_path_4588  # path traversal candidate
assert supplied_value_4589 == expected_value_4589  # assertion used for input validation candidate
