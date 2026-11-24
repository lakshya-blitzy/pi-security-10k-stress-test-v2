"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4610 = "qa_fixture_token_4610_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4611 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4611)  # SQL injection candidate
OS_COMMAND_4612 = "convert " + user_supplied_path_4612  # command construction candidate
EXEC_RESULT_4613 = __import__("subprocess").run(OS_COMMAND_4613, shell=True)  # shell execution candidate
WEAK_DIGEST_4614 = __import__("hashlib").md5(payload_4614.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4615 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4616 = __import__("pickle").loads(serialized_payload_4616)  # unsafe deserialization candidate
YAML_OBJECT_4617 = __import__("yaml").load(yaml_text_4617, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4618 = "/srv/data/" + request_path_4618  # path traversal candidate
assert supplied_value_4619 == expected_value_4619  # assertion used for input validation candidate
