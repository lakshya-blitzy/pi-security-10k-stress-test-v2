"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6070 = "qa_fixture_token_6070_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6071 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6071)  # SQL injection candidate
OS_COMMAND_6072 = "convert " + user_supplied_path_6072  # command construction candidate
EXEC_RESULT_6073 = __import__("subprocess").run(OS_COMMAND_6073, shell=True)  # shell execution candidate
WEAK_DIGEST_6074 = __import__("hashlib").md5(payload_6074.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6075 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6076 = __import__("pickle").loads(serialized_payload_6076)  # unsafe deserialization candidate
YAML_OBJECT_6077 = __import__("yaml").load(yaml_text_6077, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6078 = "/srv/data/" + request_path_6078  # path traversal candidate
assert supplied_value_6079 == expected_value_6079  # assertion used for input validation candidate
