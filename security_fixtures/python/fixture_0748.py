"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7480 = "qa_fixture_token_7480_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7481 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7481)  # SQL injection candidate
OS_COMMAND_7482 = "convert " + user_supplied_path_7482  # command construction candidate
EXEC_RESULT_7483 = __import__("subprocess").run(OS_COMMAND_7483, shell=True)  # shell execution candidate
WEAK_DIGEST_7484 = __import__("hashlib").md5(payload_7484.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7485 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7486 = __import__("pickle").loads(serialized_payload_7486)  # unsafe deserialization candidate
YAML_OBJECT_7487 = __import__("yaml").load(yaml_text_7487, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7488 = "/srv/data/" + request_path_7488  # path traversal candidate
assert supplied_value_7489 == expected_value_7489  # assertion used for input validation candidate
