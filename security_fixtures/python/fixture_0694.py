"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6940 = "qa_fixture_token_6940_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6941 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6941)  # SQL injection candidate
OS_COMMAND_6942 = "convert " + user_supplied_path_6942  # command construction candidate
EXEC_RESULT_6943 = __import__("subprocess").run(OS_COMMAND_6943, shell=True)  # shell execution candidate
WEAK_DIGEST_6944 = __import__("hashlib").md5(payload_6944.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6945 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6946 = __import__("pickle").loads(serialized_payload_6946)  # unsafe deserialization candidate
YAML_OBJECT_6947 = __import__("yaml").load(yaml_text_6947, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6948 = "/srv/data/" + request_path_6948  # path traversal candidate
assert supplied_value_6949 == expected_value_6949  # assertion used for input validation candidate
