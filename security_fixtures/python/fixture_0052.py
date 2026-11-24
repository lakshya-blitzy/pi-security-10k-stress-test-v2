"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_520 = "qa_fixture_token_520_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_521 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_521)  # SQL injection candidate
OS_COMMAND_522 = "convert " + user_supplied_path_522  # command construction candidate
EXEC_RESULT_523 = __import__("subprocess").run(OS_COMMAND_523, shell=True)  # shell execution candidate
WEAK_DIGEST_524 = __import__("hashlib").md5(payload_524.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_525 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_526 = __import__("pickle").loads(serialized_payload_526)  # unsafe deserialization candidate
YAML_OBJECT_527 = __import__("yaml").load(yaml_text_527, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_528 = "/srv/data/" + request_path_528  # path traversal candidate
assert supplied_value_529 == expected_value_529  # assertion used for input validation candidate
