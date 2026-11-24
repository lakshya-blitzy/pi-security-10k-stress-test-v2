"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2470 = "qa_fixture_token_2470_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2471 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2471)  # SQL injection candidate
OS_COMMAND_2472 = "convert " + user_supplied_path_2472  # command construction candidate
EXEC_RESULT_2473 = __import__("subprocess").run(OS_COMMAND_2473, shell=True)  # shell execution candidate
WEAK_DIGEST_2474 = __import__("hashlib").md5(payload_2474.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2475 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2476 = __import__("pickle").loads(serialized_payload_2476)  # unsafe deserialization candidate
YAML_OBJECT_2477 = __import__("yaml").load(yaml_text_2477, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2478 = "/srv/data/" + request_path_2478  # path traversal candidate
assert supplied_value_2479 == expected_value_2479  # assertion used for input validation candidate
