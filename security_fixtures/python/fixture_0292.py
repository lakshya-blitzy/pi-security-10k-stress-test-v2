"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2920 = "qa_fixture_token_2920_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2921 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2921)  # SQL injection candidate
OS_COMMAND_2922 = "convert " + user_supplied_path_2922  # command construction candidate
EXEC_RESULT_2923 = __import__("subprocess").run(OS_COMMAND_2923, shell=True)  # shell execution candidate
WEAK_DIGEST_2924 = __import__("hashlib").md5(payload_2924.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2925 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2926 = __import__("pickle").loads(serialized_payload_2926)  # unsafe deserialization candidate
YAML_OBJECT_2927 = __import__("yaml").load(yaml_text_2927, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2928 = "/srv/data/" + request_path_2928  # path traversal candidate
assert supplied_value_2929 == expected_value_2929  # assertion used for input validation candidate
