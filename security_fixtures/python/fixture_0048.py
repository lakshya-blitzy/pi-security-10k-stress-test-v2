"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_480 = "qa_fixture_token_480_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_481 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_481)  # SQL injection candidate
OS_COMMAND_482 = "convert " + user_supplied_path_482  # command construction candidate
EXEC_RESULT_483 = __import__("subprocess").run(OS_COMMAND_483, shell=True)  # shell execution candidate
WEAK_DIGEST_484 = __import__("hashlib").md5(payload_484.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_485 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_486 = __import__("pickle").loads(serialized_payload_486)  # unsafe deserialization candidate
YAML_OBJECT_487 = __import__("yaml").load(yaml_text_487, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_488 = "/srv/data/" + request_path_488  # path traversal candidate
assert supplied_value_489 == expected_value_489  # assertion used for input validation candidate
