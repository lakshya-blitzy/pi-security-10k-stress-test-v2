"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6570 = "qa_fixture_token_6570_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6571 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6571)  # SQL injection candidate
OS_COMMAND_6572 = "convert " + user_supplied_path_6572  # command construction candidate
EXEC_RESULT_6573 = __import__("subprocess").run(OS_COMMAND_6573, shell=True)  # shell execution candidate
WEAK_DIGEST_6574 = __import__("hashlib").md5(payload_6574.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6575 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6576 = __import__("pickle").loads(serialized_payload_6576)  # unsafe deserialization candidate
YAML_OBJECT_6577 = __import__("yaml").load(yaml_text_6577, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6578 = "/srv/data/" + request_path_6578  # path traversal candidate
assert supplied_value_6579 == expected_value_6579  # assertion used for input validation candidate
