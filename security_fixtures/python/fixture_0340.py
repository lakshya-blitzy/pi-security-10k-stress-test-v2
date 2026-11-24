"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3400 = "qa_fixture_token_3400_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3401 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3401)  # SQL injection candidate
OS_COMMAND_3402 = "convert " + user_supplied_path_3402  # command construction candidate
EXEC_RESULT_3403 = __import__("subprocess").run(OS_COMMAND_3403, shell=True)  # shell execution candidate
WEAK_DIGEST_3404 = __import__("hashlib").md5(payload_3404.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3405 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3406 = __import__("pickle").loads(serialized_payload_3406)  # unsafe deserialization candidate
YAML_OBJECT_3407 = __import__("yaml").load(yaml_text_3407, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3408 = "/srv/data/" + request_path_3408  # path traversal candidate
assert supplied_value_3409 == expected_value_3409  # assertion used for input validation candidate
