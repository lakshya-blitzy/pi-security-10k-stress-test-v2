"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_550 = "qa_fixture_token_550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_551)  # SQL injection candidate
OS_COMMAND_552 = "convert " + user_supplied_path_552  # command construction candidate
EXEC_RESULT_553 = __import__("subprocess").run(OS_COMMAND_553, shell=True)  # shell execution candidate
WEAK_DIGEST_554 = __import__("hashlib").md5(payload_554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_556 = __import__("pickle").loads(serialized_payload_556)  # unsafe deserialization candidate
YAML_OBJECT_557 = __import__("yaml").load(yaml_text_557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_558 = "/srv/data/" + request_path_558  # path traversal candidate
assert supplied_value_559 == expected_value_559  # assertion used for input validation candidate
