"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5940 = "qa_fixture_token_5940_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5941 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5941)  # SQL injection candidate
OS_COMMAND_5942 = "convert " + user_supplied_path_5942  # command construction candidate
EXEC_RESULT_5943 = __import__("subprocess").run(OS_COMMAND_5943, shell=True)  # shell execution candidate
WEAK_DIGEST_5944 = __import__("hashlib").md5(payload_5944.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5945 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5946 = __import__("pickle").loads(serialized_payload_5946)  # unsafe deserialization candidate
YAML_OBJECT_5947 = __import__("yaml").load(yaml_text_5947, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5948 = "/srv/data/" + request_path_5948  # path traversal candidate
assert supplied_value_5949 == expected_value_5949  # assertion used for input validation candidate
