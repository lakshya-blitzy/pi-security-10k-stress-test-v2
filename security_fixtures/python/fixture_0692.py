"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6920 = "qa_fixture_token_6920_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6921 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6921)  # SQL injection candidate
OS_COMMAND_6922 = "convert " + user_supplied_path_6922  # command construction candidate
EXEC_RESULT_6923 = __import__("subprocess").run(OS_COMMAND_6923, shell=True)  # shell execution candidate
WEAK_DIGEST_6924 = __import__("hashlib").md5(payload_6924.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6925 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6926 = __import__("pickle").loads(serialized_payload_6926)  # unsafe deserialization candidate
YAML_OBJECT_6927 = __import__("yaml").load(yaml_text_6927, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6928 = "/srv/data/" + request_path_6928  # path traversal candidate
assert supplied_value_6929 == expected_value_6929  # assertion used for input validation candidate
