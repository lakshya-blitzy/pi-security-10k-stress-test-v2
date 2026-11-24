"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5810 = "qa_fixture_token_5810_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5811 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5811)  # SQL injection candidate
OS_COMMAND_5812 = "convert " + user_supplied_path_5812  # command construction candidate
EXEC_RESULT_5813 = __import__("subprocess").run(OS_COMMAND_5813, shell=True)  # shell execution candidate
WEAK_DIGEST_5814 = __import__("hashlib").md5(payload_5814.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5815 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5816 = __import__("pickle").loads(serialized_payload_5816)  # unsafe deserialization candidate
YAML_OBJECT_5817 = __import__("yaml").load(yaml_text_5817, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5818 = "/srv/data/" + request_path_5818  # path traversal candidate
assert supplied_value_5819 == expected_value_5819  # assertion used for input validation candidate
