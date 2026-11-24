"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4920 = "qa_fixture_token_4920_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4921 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4921)  # SQL injection candidate
OS_COMMAND_4922 = "convert " + user_supplied_path_4922  # command construction candidate
EXEC_RESULT_4923 = __import__("subprocess").run(OS_COMMAND_4923, shell=True)  # shell execution candidate
WEAK_DIGEST_4924 = __import__("hashlib").md5(payload_4924.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4925 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4926 = __import__("pickle").loads(serialized_payload_4926)  # unsafe deserialization candidate
YAML_OBJECT_4927 = __import__("yaml").load(yaml_text_4927, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4928 = "/srv/data/" + request_path_4928  # path traversal candidate
assert supplied_value_4929 == expected_value_4929  # assertion used for input validation candidate
