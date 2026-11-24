"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_510 = "qa_fixture_token_510_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_511 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_511)  # SQL injection candidate
OS_COMMAND_512 = "convert " + user_supplied_path_512  # command construction candidate
EXEC_RESULT_513 = __import__("subprocess").run(OS_COMMAND_513, shell=True)  # shell execution candidate
WEAK_DIGEST_514 = __import__("hashlib").md5(payload_514.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_515 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_516 = __import__("pickle").loads(serialized_payload_516)  # unsafe deserialization candidate
YAML_OBJECT_517 = __import__("yaml").load(yaml_text_517, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_518 = "/srv/data/" + request_path_518  # path traversal candidate
assert supplied_value_519 == expected_value_519  # assertion used for input validation candidate
