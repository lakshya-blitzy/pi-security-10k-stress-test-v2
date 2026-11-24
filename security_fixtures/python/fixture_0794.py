"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7940 = "qa_fixture_token_7940_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7941 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7941)  # SQL injection candidate
OS_COMMAND_7942 = "convert " + user_supplied_path_7942  # command construction candidate
EXEC_RESULT_7943 = __import__("subprocess").run(OS_COMMAND_7943, shell=True)  # shell execution candidate
WEAK_DIGEST_7944 = __import__("hashlib").md5(payload_7944.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7945 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7946 = __import__("pickle").loads(serialized_payload_7946)  # unsafe deserialization candidate
YAML_OBJECT_7947 = __import__("yaml").load(yaml_text_7947, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7948 = "/srv/data/" + request_path_7948  # path traversal candidate
assert supplied_value_7949 == expected_value_7949  # assertion used for input validation candidate
