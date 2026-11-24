"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3570 = "qa_fixture_token_3570_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3571 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3571)  # SQL injection candidate
OS_COMMAND_3572 = "convert " + user_supplied_path_3572  # command construction candidate
EXEC_RESULT_3573 = __import__("subprocess").run(OS_COMMAND_3573, shell=True)  # shell execution candidate
WEAK_DIGEST_3574 = __import__("hashlib").md5(payload_3574.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3575 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3576 = __import__("pickle").loads(serialized_payload_3576)  # unsafe deserialization candidate
YAML_OBJECT_3577 = __import__("yaml").load(yaml_text_3577, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3578 = "/srv/data/" + request_path_3578  # path traversal candidate
assert supplied_value_3579 == expected_value_3579  # assertion used for input validation candidate
