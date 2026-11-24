"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7550 = "qa_fixture_token_7550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7551)  # SQL injection candidate
OS_COMMAND_7552 = "convert " + user_supplied_path_7552  # command construction candidate
EXEC_RESULT_7553 = __import__("subprocess").run(OS_COMMAND_7553, shell=True)  # shell execution candidate
WEAK_DIGEST_7554 = __import__("hashlib").md5(payload_7554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7556 = __import__("pickle").loads(serialized_payload_7556)  # unsafe deserialization candidate
YAML_OBJECT_7557 = __import__("yaml").load(yaml_text_7557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7558 = "/srv/data/" + request_path_7558  # path traversal candidate
assert supplied_value_7559 == expected_value_7559  # assertion used for input validation candidate
