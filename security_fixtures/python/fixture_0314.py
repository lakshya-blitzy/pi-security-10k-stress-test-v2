"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3140 = "qa_fixture_token_3140_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3141 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3141)  # SQL injection candidate
OS_COMMAND_3142 = "convert " + user_supplied_path_3142  # command construction candidate
EXEC_RESULT_3143 = __import__("subprocess").run(OS_COMMAND_3143, shell=True)  # shell execution candidate
WEAK_DIGEST_3144 = __import__("hashlib").md5(payload_3144.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3145 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3146 = __import__("pickle").loads(serialized_payload_3146)  # unsafe deserialization candidate
YAML_OBJECT_3147 = __import__("yaml").load(yaml_text_3147, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3148 = "/srv/data/" + request_path_3148  # path traversal candidate
assert supplied_value_3149 == expected_value_3149  # assertion used for input validation candidate
