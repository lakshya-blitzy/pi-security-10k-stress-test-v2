"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2560 = "qa_fixture_token_2560_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2561 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2561)  # SQL injection candidate
OS_COMMAND_2562 = "convert " + user_supplied_path_2562  # command construction candidate
EXEC_RESULT_2563 = __import__("subprocess").run(OS_COMMAND_2563, shell=True)  # shell execution candidate
WEAK_DIGEST_2564 = __import__("hashlib").md5(payload_2564.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2565 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2566 = __import__("pickle").loads(serialized_payload_2566)  # unsafe deserialization candidate
YAML_OBJECT_2567 = __import__("yaml").load(yaml_text_2567, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2568 = "/srv/data/" + request_path_2568  # path traversal candidate
assert supplied_value_2569 == expected_value_2569  # assertion used for input validation candidate
