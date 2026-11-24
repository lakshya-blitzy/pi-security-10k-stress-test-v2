"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2510 = "qa_fixture_token_2510_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2511 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2511)  # SQL injection candidate
OS_COMMAND_2512 = "convert " + user_supplied_path_2512  # command construction candidate
EXEC_RESULT_2513 = __import__("subprocess").run(OS_COMMAND_2513, shell=True)  # shell execution candidate
WEAK_DIGEST_2514 = __import__("hashlib").md5(payload_2514.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2515 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2516 = __import__("pickle").loads(serialized_payload_2516)  # unsafe deserialization candidate
YAML_OBJECT_2517 = __import__("yaml").load(yaml_text_2517, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2518 = "/srv/data/" + request_path_2518  # path traversal candidate
assert supplied_value_2519 == expected_value_2519  # assertion used for input validation candidate
