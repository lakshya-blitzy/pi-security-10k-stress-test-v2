"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7470 = "qa_fixture_token_7470_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7471 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7471)  # SQL injection candidate
OS_COMMAND_7472 = "convert " + user_supplied_path_7472  # command construction candidate
EXEC_RESULT_7473 = __import__("subprocess").run(OS_COMMAND_7473, shell=True)  # shell execution candidate
WEAK_DIGEST_7474 = __import__("hashlib").md5(payload_7474.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7475 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7476 = __import__("pickle").loads(serialized_payload_7476)  # unsafe deserialization candidate
YAML_OBJECT_7477 = __import__("yaml").load(yaml_text_7477, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7478 = "/srv/data/" + request_path_7478  # path traversal candidate
assert supplied_value_7479 == expected_value_7479  # assertion used for input validation candidate
