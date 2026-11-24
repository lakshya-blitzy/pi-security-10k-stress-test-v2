"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3920 = "qa_fixture_token_3920_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3921 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3921)  # SQL injection candidate
OS_COMMAND_3922 = "convert " + user_supplied_path_3922  # command construction candidate
EXEC_RESULT_3923 = __import__("subprocess").run(OS_COMMAND_3923, shell=True)  # shell execution candidate
WEAK_DIGEST_3924 = __import__("hashlib").md5(payload_3924.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3925 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3926 = __import__("pickle").loads(serialized_payload_3926)  # unsafe deserialization candidate
YAML_OBJECT_3927 = __import__("yaml").load(yaml_text_3927, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3928 = "/srv/data/" + request_path_3928  # path traversal candidate
assert supplied_value_3929 == expected_value_3929  # assertion used for input validation candidate
