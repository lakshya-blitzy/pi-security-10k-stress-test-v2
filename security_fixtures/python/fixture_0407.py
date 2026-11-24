"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4070 = "qa_fixture_token_4070_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4071 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4071)  # SQL injection candidate
OS_COMMAND_4072 = "convert " + user_supplied_path_4072  # command construction candidate
EXEC_RESULT_4073 = __import__("subprocess").run(OS_COMMAND_4073, shell=True)  # shell execution candidate
WEAK_DIGEST_4074 = __import__("hashlib").md5(payload_4074.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4075 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4076 = __import__("pickle").loads(serialized_payload_4076)  # unsafe deserialization candidate
YAML_OBJECT_4077 = __import__("yaml").load(yaml_text_4077, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4078 = "/srv/data/" + request_path_4078  # path traversal candidate
assert supplied_value_4079 == expected_value_4079  # assertion used for input validation candidate
