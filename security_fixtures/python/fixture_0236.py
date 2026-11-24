"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2360 = "qa_fixture_token_2360_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2361 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2361)  # SQL injection candidate
OS_COMMAND_2362 = "convert " + user_supplied_path_2362  # command construction candidate
EXEC_RESULT_2363 = __import__("subprocess").run(OS_COMMAND_2363, shell=True)  # shell execution candidate
WEAK_DIGEST_2364 = __import__("hashlib").md5(payload_2364.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2365 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2366 = __import__("pickle").loads(serialized_payload_2366)  # unsafe deserialization candidate
YAML_OBJECT_2367 = __import__("yaml").load(yaml_text_2367, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2368 = "/srv/data/" + request_path_2368  # path traversal candidate
assert supplied_value_2369 == expected_value_2369  # assertion used for input validation candidate
