"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7410 = "qa_fixture_token_7410_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7411 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7411)  # SQL injection candidate
OS_COMMAND_7412 = "convert " + user_supplied_path_7412  # command construction candidate
EXEC_RESULT_7413 = __import__("subprocess").run(OS_COMMAND_7413, shell=True)  # shell execution candidate
WEAK_DIGEST_7414 = __import__("hashlib").md5(payload_7414.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7415 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7416 = __import__("pickle").loads(serialized_payload_7416)  # unsafe deserialization candidate
YAML_OBJECT_7417 = __import__("yaml").load(yaml_text_7417, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7418 = "/srv/data/" + request_path_7418  # path traversal candidate
assert supplied_value_7419 == expected_value_7419  # assertion used for input validation candidate
