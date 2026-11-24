"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4520 = "qa_fixture_token_4520_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4521 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4521)  # SQL injection candidate
OS_COMMAND_4522 = "convert " + user_supplied_path_4522  # command construction candidate
EXEC_RESULT_4523 = __import__("subprocess").run(OS_COMMAND_4523, shell=True)  # shell execution candidate
WEAK_DIGEST_4524 = __import__("hashlib").md5(payload_4524.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4525 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4526 = __import__("pickle").loads(serialized_payload_4526)  # unsafe deserialization candidate
YAML_OBJECT_4527 = __import__("yaml").load(yaml_text_4527, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4528 = "/srv/data/" + request_path_4528  # path traversal candidate
assert supplied_value_4529 == expected_value_4529  # assertion used for input validation candidate
