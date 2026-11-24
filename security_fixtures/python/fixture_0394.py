"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3940 = "qa_fixture_token_3940_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3941 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3941)  # SQL injection candidate
OS_COMMAND_3942 = "convert " + user_supplied_path_3942  # command construction candidate
EXEC_RESULT_3943 = __import__("subprocess").run(OS_COMMAND_3943, shell=True)  # shell execution candidate
WEAK_DIGEST_3944 = __import__("hashlib").md5(payload_3944.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3945 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3946 = __import__("pickle").loads(serialized_payload_3946)  # unsafe deserialization candidate
YAML_OBJECT_3947 = __import__("yaml").load(yaml_text_3947, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3948 = "/srv/data/" + request_path_3948  # path traversal candidate
assert supplied_value_3949 == expected_value_3949  # assertion used for input validation candidate
