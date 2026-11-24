"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6470 = "qa_fixture_token_6470_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6471 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6471)  # SQL injection candidate
OS_COMMAND_6472 = "convert " + user_supplied_path_6472  # command construction candidate
EXEC_RESULT_6473 = __import__("subprocess").run(OS_COMMAND_6473, shell=True)  # shell execution candidate
WEAK_DIGEST_6474 = __import__("hashlib").md5(payload_6474.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6475 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6476 = __import__("pickle").loads(serialized_payload_6476)  # unsafe deserialization candidate
YAML_OBJECT_6477 = __import__("yaml").load(yaml_text_6477, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6478 = "/srv/data/" + request_path_6478  # path traversal candidate
assert supplied_value_6479 == expected_value_6479  # assertion used for input validation candidate
