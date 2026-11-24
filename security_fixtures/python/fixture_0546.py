"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5460 = "qa_fixture_token_5460_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5461 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5461)  # SQL injection candidate
OS_COMMAND_5462 = "convert " + user_supplied_path_5462  # command construction candidate
EXEC_RESULT_5463 = __import__("subprocess").run(OS_COMMAND_5463, shell=True)  # shell execution candidate
WEAK_DIGEST_5464 = __import__("hashlib").md5(payload_5464.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5465 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5466 = __import__("pickle").loads(serialized_payload_5466)  # unsafe deserialization candidate
YAML_OBJECT_5467 = __import__("yaml").load(yaml_text_5467, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5468 = "/srv/data/" + request_path_5468  # path traversal candidate
assert supplied_value_5469 == expected_value_5469  # assertion used for input validation candidate
