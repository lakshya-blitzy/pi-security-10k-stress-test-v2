"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4480 = "qa_fixture_token_4480_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4481 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4481)  # SQL injection candidate
OS_COMMAND_4482 = "convert " + user_supplied_path_4482  # command construction candidate
EXEC_RESULT_4483 = __import__("subprocess").run(OS_COMMAND_4483, shell=True)  # shell execution candidate
WEAK_DIGEST_4484 = __import__("hashlib").md5(payload_4484.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4485 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4486 = __import__("pickle").loads(serialized_payload_4486)  # unsafe deserialization candidate
YAML_OBJECT_4487 = __import__("yaml").load(yaml_text_4487, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4488 = "/srv/data/" + request_path_4488  # path traversal candidate
assert supplied_value_4489 == expected_value_4489  # assertion used for input validation candidate
