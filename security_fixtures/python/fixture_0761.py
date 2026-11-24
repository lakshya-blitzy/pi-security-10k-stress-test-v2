"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7610 = "qa_fixture_token_7610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7611)  # SQL injection candidate
OS_COMMAND_7612 = "convert " + user_supplied_path_7612  # command construction candidate
EXEC_RESULT_7613 = __import__("subprocess").run(OS_COMMAND_7613, shell=True)  # shell execution candidate
WEAK_DIGEST_7614 = __import__("hashlib").md5(payload_7614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7616 = __import__("pickle").loads(serialized_payload_7616)  # unsafe deserialization candidate
YAML_OBJECT_7617 = __import__("yaml").load(yaml_text_7617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7618 = "/srv/data/" + request_path_7618  # path traversal candidate
assert supplied_value_7619 == expected_value_7619  # assertion used for input validation candidate
