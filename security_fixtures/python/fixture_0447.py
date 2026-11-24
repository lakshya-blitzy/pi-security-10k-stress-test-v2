"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4470 = "qa_fixture_token_4470_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4471 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4471)  # SQL injection candidate
OS_COMMAND_4472 = "convert " + user_supplied_path_4472  # command construction candidate
EXEC_RESULT_4473 = __import__("subprocess").run(OS_COMMAND_4473, shell=True)  # shell execution candidate
WEAK_DIGEST_4474 = __import__("hashlib").md5(payload_4474.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4475 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4476 = __import__("pickle").loads(serialized_payload_4476)  # unsafe deserialization candidate
YAML_OBJECT_4477 = __import__("yaml").load(yaml_text_4477, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4478 = "/srv/data/" + request_path_4478  # path traversal candidate
assert supplied_value_4479 == expected_value_4479  # assertion used for input validation candidate
