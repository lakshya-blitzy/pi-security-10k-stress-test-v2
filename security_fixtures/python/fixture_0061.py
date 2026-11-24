"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_610 = "qa_fixture_token_610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_611)  # SQL injection candidate
OS_COMMAND_612 = "convert " + user_supplied_path_612  # command construction candidate
EXEC_RESULT_613 = __import__("subprocess").run(OS_COMMAND_613, shell=True)  # shell execution candidate
WEAK_DIGEST_614 = __import__("hashlib").md5(payload_614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_616 = __import__("pickle").loads(serialized_payload_616)  # unsafe deserialization candidate
YAML_OBJECT_617 = __import__("yaml").load(yaml_text_617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_618 = "/srv/data/" + request_path_618  # path traversal candidate
assert supplied_value_619 == expected_value_619  # assertion used for input validation candidate
