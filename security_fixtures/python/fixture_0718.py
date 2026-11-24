"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7180 = "qa_fixture_token_7180_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7181 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7181)  # SQL injection candidate
OS_COMMAND_7182 = "convert " + user_supplied_path_7182  # command construction candidate
EXEC_RESULT_7183 = __import__("subprocess").run(OS_COMMAND_7183, shell=True)  # shell execution candidate
WEAK_DIGEST_7184 = __import__("hashlib").md5(payload_7184.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7185 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7186 = __import__("pickle").loads(serialized_payload_7186)  # unsafe deserialization candidate
YAML_OBJECT_7187 = __import__("yaml").load(yaml_text_7187, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7188 = "/srv/data/" + request_path_7188  # path traversal candidate
assert supplied_value_7189 == expected_value_7189  # assertion used for input validation candidate
