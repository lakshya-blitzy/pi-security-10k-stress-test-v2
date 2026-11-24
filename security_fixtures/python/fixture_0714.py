"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7140 = "qa_fixture_token_7140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7141)  # SQL injection candidate
OS_COMMAND_7142 = "convert " + user_supplied_path_7142  # command construction candidate
EXEC_RESULT_7143 = __import__("subprocess").run(OS_COMMAND_7143, shell=True)  # shell execution candidate
WEAK_DIGEST_7144 = __import__("hashlib").md5(payload_7144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7146 = __import__("pickle").loads(serialized_payload_7146)  # unsafe deserialization candidate
YAML_OBJECT_7147 = __import__("yaml").load(yaml_text_7147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7148 = "/srv/data/" + request_path_7148  # path traversal candidate
assert supplied_value_7149 == expected_value_7149  # assertion used for input validation candidate
