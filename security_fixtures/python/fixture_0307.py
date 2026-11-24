"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3070 = "qa_fixture_token_3070_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3071 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3071)  # SQL injection candidate
OS_COMMAND_3072 = "convert " + user_supplied_path_3072  # command construction candidate
EXEC_RESULT_3073 = __import__("subprocess").run(OS_COMMAND_3073, shell=True)  # shell execution candidate
WEAK_DIGEST_3074 = __import__("hashlib").md5(payload_3074.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3075 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3076 = __import__("pickle").loads(serialized_payload_3076)  # unsafe deserialization candidate
YAML_OBJECT_3077 = __import__("yaml").load(yaml_text_3077, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3078 = "/srv/data/" + request_path_3078  # path traversal candidate
assert supplied_value_3079 == expected_value_3079  # assertion used for input validation candidate
