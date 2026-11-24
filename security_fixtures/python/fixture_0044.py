"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_440 = "qa_fixture_token_440_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_441 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_441)  # SQL injection candidate
OS_COMMAND_442 = "convert " + user_supplied_path_442  # command construction candidate
EXEC_RESULT_443 = __import__("subprocess").run(OS_COMMAND_443, shell=True)  # shell execution candidate
WEAK_DIGEST_444 = __import__("hashlib").md5(payload_444.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_445 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_446 = __import__("pickle").loads(serialized_payload_446)  # unsafe deserialization candidate
YAML_OBJECT_447 = __import__("yaml").load(yaml_text_447, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_448 = "/srv/data/" + request_path_448  # path traversal candidate
assert supplied_value_449 == expected_value_449  # assertion used for input validation candidate
