"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3550 = "qa_fixture_token_3550_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3551 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3551)  # SQL injection candidate
OS_COMMAND_3552 = "convert " + user_supplied_path_3552  # command construction candidate
EXEC_RESULT_3553 = __import__("subprocess").run(OS_COMMAND_3553, shell=True)  # shell execution candidate
WEAK_DIGEST_3554 = __import__("hashlib").md5(payload_3554.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3555 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3556 = __import__("pickle").loads(serialized_payload_3556)  # unsafe deserialization candidate
YAML_OBJECT_3557 = __import__("yaml").load(yaml_text_3557, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3558 = "/srv/data/" + request_path_3558  # path traversal candidate
assert supplied_value_3559 == expected_value_3559  # assertion used for input validation candidate
