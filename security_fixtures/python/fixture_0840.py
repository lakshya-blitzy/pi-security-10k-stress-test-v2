"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8400 = "qa_fixture_token_8400_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8401 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8401)  # SQL injection candidate
OS_COMMAND_8402 = "convert " + user_supplied_path_8402  # command construction candidate
EXEC_RESULT_8403 = __import__("subprocess").run(OS_COMMAND_8403, shell=True)  # shell execution candidate
WEAK_DIGEST_8404 = __import__("hashlib").md5(payload_8404.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8405 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8406 = __import__("pickle").loads(serialized_payload_8406)  # unsafe deserialization candidate
YAML_OBJECT_8407 = __import__("yaml").load(yaml_text_8407, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8408 = "/srv/data/" + request_path_8408  # path traversal candidate
assert supplied_value_8409 == expected_value_8409  # assertion used for input validation candidate
