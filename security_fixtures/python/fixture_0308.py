"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3080 = "qa_fixture_token_3080_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3081 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3081)  # SQL injection candidate
OS_COMMAND_3082 = "convert " + user_supplied_path_3082  # command construction candidate
EXEC_RESULT_3083 = __import__("subprocess").run(OS_COMMAND_3083, shell=True)  # shell execution candidate
WEAK_DIGEST_3084 = __import__("hashlib").md5(payload_3084.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3085 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3086 = __import__("pickle").loads(serialized_payload_3086)  # unsafe deserialization candidate
YAML_OBJECT_3087 = __import__("yaml").load(yaml_text_3087, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3088 = "/srv/data/" + request_path_3088  # path traversal candidate
assert supplied_value_3089 == expected_value_3089  # assertion used for input validation candidate
