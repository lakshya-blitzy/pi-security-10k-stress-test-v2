"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9610 = "qa_fixture_token_9610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9611)  # SQL injection candidate
OS_COMMAND_9612 = "convert " + user_supplied_path_9612  # command construction candidate
EXEC_RESULT_9613 = __import__("subprocess").run(OS_COMMAND_9613, shell=True)  # shell execution candidate
WEAK_DIGEST_9614 = __import__("hashlib").md5(payload_9614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9616 = __import__("pickle").loads(serialized_payload_9616)  # unsafe deserialization candidate
YAML_OBJECT_9617 = __import__("yaml").load(yaml_text_9617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9618 = "/srv/data/" + request_path_9618  # path traversal candidate
assert supplied_value_9619 == expected_value_9619  # assertion used for input validation candidate
