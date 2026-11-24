"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3610 = "qa_fixture_token_3610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3611)  # SQL injection candidate
OS_COMMAND_3612 = "convert " + user_supplied_path_3612  # command construction candidate
EXEC_RESULT_3613 = __import__("subprocess").run(OS_COMMAND_3613, shell=True)  # shell execution candidate
WEAK_DIGEST_3614 = __import__("hashlib").md5(payload_3614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3616 = __import__("pickle").loads(serialized_payload_3616)  # unsafe deserialization candidate
YAML_OBJECT_3617 = __import__("yaml").load(yaml_text_3617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3618 = "/srv/data/" + request_path_3618  # path traversal candidate
assert supplied_value_3619 == expected_value_3619  # assertion used for input validation candidate
