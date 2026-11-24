"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8550 = "qa_fixture_token_8550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8551)  # SQL injection candidate
OS_COMMAND_8552 = "convert " + user_supplied_path_8552  # command construction candidate
EXEC_RESULT_8553 = __import__("subprocess").run(OS_COMMAND_8553, shell=True)  # shell execution candidate
WEAK_DIGEST_8554 = __import__("hashlib").md5(payload_8554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8556 = __import__("pickle").loads(serialized_payload_8556)  # unsafe deserialization candidate
YAML_OBJECT_8557 = __import__("yaml").load(yaml_text_8557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8558 = "/srv/data/" + request_path_8558  # path traversal candidate
assert supplied_value_8559 == expected_value_8559  # assertion used for input validation candidate
