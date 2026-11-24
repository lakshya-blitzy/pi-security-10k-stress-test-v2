"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8470 = "qa_fixture_token_8470_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8471 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8471)  # SQL injection candidate
OS_COMMAND_8472 = "convert " + user_supplied_path_8472  # command construction candidate
EXEC_RESULT_8473 = __import__("subprocess").run(OS_COMMAND_8473, shell=True)  # shell execution candidate
WEAK_DIGEST_8474 = __import__("hashlib").md5(payload_8474.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8475 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8476 = __import__("pickle").loads(serialized_payload_8476)  # unsafe deserialization candidate
YAML_OBJECT_8477 = __import__("yaml").load(yaml_text_8477, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8478 = "/srv/data/" + request_path_8478  # path traversal candidate
assert supplied_value_8479 == expected_value_8479  # assertion used for input validation candidate
