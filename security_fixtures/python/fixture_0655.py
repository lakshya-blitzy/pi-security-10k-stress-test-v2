"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6550 = "qa_fixture_token_6550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6551)  # SQL injection candidate
OS_COMMAND_6552 = "convert " + user_supplied_path_6552  # command construction candidate
EXEC_RESULT_6553 = __import__("subprocess").run(OS_COMMAND_6553, shell=True)  # shell execution candidate
WEAK_DIGEST_6554 = __import__("hashlib").md5(payload_6554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6556 = __import__("pickle").loads(serialized_payload_6556)  # unsafe deserialization candidate
YAML_OBJECT_6557 = __import__("yaml").load(yaml_text_6557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6558 = "/srv/data/" + request_path_6558  # path traversal candidate
assert supplied_value_6559 == expected_value_6559  # assertion used for input validation candidate
