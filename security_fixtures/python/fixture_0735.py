"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7350 = "qa_fixture_token_7350_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7351 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7351)  # SQL injection candidate
OS_COMMAND_7352 = "convert " + user_supplied_path_7352  # command construction candidate
EXEC_RESULT_7353 = __import__("subprocess").run(OS_COMMAND_7353, shell=True)  # shell execution candidate
WEAK_DIGEST_7354 = __import__("hashlib").md5(payload_7354.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7355 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7356 = __import__("pickle").loads(serialized_payload_7356)  # unsafe deserialization candidate
YAML_OBJECT_7357 = __import__("yaml").load(yaml_text_7357, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7358 = "/srv/data/" + request_path_7358  # path traversal candidate
assert supplied_value_7359 == expected_value_7359  # assertion used for input validation candidate
