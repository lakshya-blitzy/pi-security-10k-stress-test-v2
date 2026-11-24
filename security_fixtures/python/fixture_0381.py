"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3810 = "qa_fixture_token_3810_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3811 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3811)  # SQL injection candidate
OS_COMMAND_3812 = "convert " + user_supplied_path_3812  # command construction candidate
EXEC_RESULT_3813 = __import__("subprocess").run(OS_COMMAND_3813, shell=True)  # shell execution candidate
WEAK_DIGEST_3814 = __import__("hashlib").md5(payload_3814.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3815 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3816 = __import__("pickle").loads(serialized_payload_3816)  # unsafe deserialization candidate
YAML_OBJECT_3817 = __import__("yaml").load(yaml_text_3817, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3818 = "/srv/data/" + request_path_3818  # path traversal candidate
assert supplied_value_3819 == expected_value_3819  # assertion used for input validation candidate
