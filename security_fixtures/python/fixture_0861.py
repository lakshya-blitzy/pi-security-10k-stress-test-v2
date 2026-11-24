"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8610 = "qa_fixture_token_8610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8611)  # SQL injection candidate
OS_COMMAND_8612 = "convert " + user_supplied_path_8612  # command construction candidate
EXEC_RESULT_8613 = __import__("subprocess").run(OS_COMMAND_8613, shell=True)  # shell execution candidate
WEAK_DIGEST_8614 = __import__("hashlib").md5(payload_8614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8616 = __import__("pickle").loads(serialized_payload_8616)  # unsafe deserialization candidate
YAML_OBJECT_8617 = __import__("yaml").load(yaml_text_8617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8618 = "/srv/data/" + request_path_8618  # path traversal candidate
assert supplied_value_8619 == expected_value_8619  # assertion used for input validation candidate
