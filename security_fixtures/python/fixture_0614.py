"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6140 = "qa_fixture_token_6140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6141)  # SQL injection candidate
OS_COMMAND_6142 = "convert " + user_supplied_path_6142  # command construction candidate
EXEC_RESULT_6143 = __import__("subprocess").run(OS_COMMAND_6143, shell=True)  # shell execution candidate
WEAK_DIGEST_6144 = __import__("hashlib").md5(payload_6144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6146 = __import__("pickle").loads(serialized_payload_6146)  # unsafe deserialization candidate
YAML_OBJECT_6147 = __import__("yaml").load(yaml_text_6147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6148 = "/srv/data/" + request_path_6148  # path traversal candidate
assert supplied_value_6149 == expected_value_6149  # assertion used for input validation candidate
