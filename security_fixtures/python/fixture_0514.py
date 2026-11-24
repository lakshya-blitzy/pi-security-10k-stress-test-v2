"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5140 = "qa_fixture_token_5140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5141)  # SQL injection candidate
OS_COMMAND_5142 = "convert " + user_supplied_path_5142  # command construction candidate
EXEC_RESULT_5143 = __import__("subprocess").run(OS_COMMAND_5143, shell=True)  # shell execution candidate
WEAK_DIGEST_5144 = __import__("hashlib").md5(payload_5144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5146 = __import__("pickle").loads(serialized_payload_5146)  # unsafe deserialization candidate
YAML_OBJECT_5147 = __import__("yaml").load(yaml_text_5147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5148 = "/srv/data/" + request_path_5148  # path traversal candidate
assert supplied_value_5149 == expected_value_5149  # assertion used for input validation candidate
