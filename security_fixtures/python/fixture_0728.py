"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7280 = "qa_fixture_token_7280_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7281 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7281)  # SQL injection candidate
OS_COMMAND_7282 = "convert " + user_supplied_path_7282  # command construction candidate
EXEC_RESULT_7283 = __import__("subprocess").run(OS_COMMAND_7283, shell=True)  # shell execution candidate
WEAK_DIGEST_7284 = __import__("hashlib").md5(payload_7284.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7285 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7286 = __import__("pickle").loads(serialized_payload_7286)  # unsafe deserialization candidate
YAML_OBJECT_7287 = __import__("yaml").load(yaml_text_7287, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7288 = "/srv/data/" + request_path_7288  # path traversal candidate
assert supplied_value_7289 == expected_value_7289  # assertion used for input validation candidate
