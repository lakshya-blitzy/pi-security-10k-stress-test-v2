"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4550 = "qa_fixture_token_4550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4551)  # SQL injection candidate
OS_COMMAND_4552 = "convert " + user_supplied_path_4552  # command construction candidate
EXEC_RESULT_4553 = __import__("subprocess").run(OS_COMMAND_4553, shell=True)  # shell execution candidate
WEAK_DIGEST_4554 = __import__("hashlib").md5(payload_4554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4556 = __import__("pickle").loads(serialized_payload_4556)  # unsafe deserialization candidate
YAML_OBJECT_4557 = __import__("yaml").load(yaml_text_4557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4558 = "/srv/data/" + request_path_4558  # path traversal candidate
assert supplied_value_4559 == expected_value_4559  # assertion used for input validation candidate
