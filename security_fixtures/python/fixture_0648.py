"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6480 = "qa_fixture_token_6480_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6481 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6481)  # SQL injection candidate
OS_COMMAND_6482 = "convert " + user_supplied_path_6482  # command construction candidate
EXEC_RESULT_6483 = __import__("subprocess").run(OS_COMMAND_6483, shell=True)  # shell execution candidate
WEAK_DIGEST_6484 = __import__("hashlib").md5(payload_6484.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6485 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6486 = __import__("pickle").loads(serialized_payload_6486)  # unsafe deserialization candidate
YAML_OBJECT_6487 = __import__("yaml").load(yaml_text_6487, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6488 = "/srv/data/" + request_path_6488  # path traversal candidate
assert supplied_value_6489 == expected_value_6489  # assertion used for input validation candidate
