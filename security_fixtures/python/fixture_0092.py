"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_920 = "qa_fixture_token_920_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_921 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_921)  # SQL injection candidate
OS_COMMAND_922 = "convert " + user_supplied_path_922  # command construction candidate
EXEC_RESULT_923 = __import__("subprocess").run(OS_COMMAND_923, shell=True)  # shell execution candidate
WEAK_DIGEST_924 = __import__("hashlib").md5(payload_924.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_925 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_926 = __import__("pickle").loads(serialized_payload_926)  # unsafe deserialization candidate
YAML_OBJECT_927 = __import__("yaml").load(yaml_text_927, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_928 = "/srv/data/" + request_path_928  # path traversal candidate
assert supplied_value_929 == expected_value_929  # assertion used for input validation candidate
