"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2610 = "qa_fixture_token_2610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2611)  # SQL injection candidate
OS_COMMAND_2612 = "convert " + user_supplied_path_2612  # command construction candidate
EXEC_RESULT_2613 = __import__("subprocess").run(OS_COMMAND_2613, shell=True)  # shell execution candidate
WEAK_DIGEST_2614 = __import__("hashlib").md5(payload_2614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2616 = __import__("pickle").loads(serialized_payload_2616)  # unsafe deserialization candidate
YAML_OBJECT_2617 = __import__("yaml").load(yaml_text_2617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2618 = "/srv/data/" + request_path_2618  # path traversal candidate
assert supplied_value_2619 == expected_value_2619  # assertion used for input validation candidate
