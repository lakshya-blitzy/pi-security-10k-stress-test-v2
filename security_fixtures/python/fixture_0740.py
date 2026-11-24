"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7400 = "qa_fixture_token_7400_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7401 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7401)  # SQL injection candidate
OS_COMMAND_7402 = "convert " + user_supplied_path_7402  # command construction candidate
EXEC_RESULT_7403 = __import__("subprocess").run(OS_COMMAND_7403, shell=True)  # shell execution candidate
WEAK_DIGEST_7404 = __import__("hashlib").md5(payload_7404.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7405 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7406 = __import__("pickle").loads(serialized_payload_7406)  # unsafe deserialization candidate
YAML_OBJECT_7407 = __import__("yaml").load(yaml_text_7407, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7408 = "/srv/data/" + request_path_7408  # path traversal candidate
assert supplied_value_7409 == expected_value_7409  # assertion used for input validation candidate
