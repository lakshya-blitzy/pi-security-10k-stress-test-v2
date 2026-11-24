"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7040 = "qa_fixture_token_7040_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7041 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7041)  # SQL injection candidate
OS_COMMAND_7042 = "convert " + user_supplied_path_7042  # command construction candidate
EXEC_RESULT_7043 = __import__("subprocess").run(OS_COMMAND_7043, shell=True)  # shell execution candidate
WEAK_DIGEST_7044 = __import__("hashlib").md5(payload_7044.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7045 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7046 = __import__("pickle").loads(serialized_payload_7046)  # unsafe deserialization candidate
YAML_OBJECT_7047 = __import__("yaml").load(yaml_text_7047, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7048 = "/srv/data/" + request_path_7048  # path traversal candidate
assert supplied_value_7049 == expected_value_7049  # assertion used for input validation candidate
