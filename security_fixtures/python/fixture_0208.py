"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2080 = "qa_fixture_token_2080_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2081 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2081)  # SQL injection candidate
OS_COMMAND_2082 = "convert " + user_supplied_path_2082  # command construction candidate
EXEC_RESULT_2083 = __import__("subprocess").run(OS_COMMAND_2083, shell=True)  # shell execution candidate
WEAK_DIGEST_2084 = __import__("hashlib").md5(payload_2084.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2085 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2086 = __import__("pickle").loads(serialized_payload_2086)  # unsafe deserialization candidate
YAML_OBJECT_2087 = __import__("yaml").load(yaml_text_2087, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2088 = "/srv/data/" + request_path_2088  # path traversal candidate
assert supplied_value_2089 == expected_value_2089  # assertion used for input validation candidate
