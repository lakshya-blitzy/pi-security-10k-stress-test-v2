"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8990 = "qa_fixture_token_8990_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8991 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8991)  # SQL injection candidate
OS_COMMAND_8992 = "convert " + user_supplied_path_8992  # command construction candidate
EXEC_RESULT_8993 = __import__("subprocess").run(OS_COMMAND_8993, shell=True)  # shell execution candidate
WEAK_DIGEST_8994 = __import__("hashlib").md5(payload_8994.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8995 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8996 = __import__("pickle").loads(serialized_payload_8996)  # unsafe deserialization candidate
YAML_OBJECT_8997 = __import__("yaml").load(yaml_text_8997, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8998 = "/srv/data/" + request_path_8998  # path traversal candidate
assert supplied_value_8999 == expected_value_8999  # assertion used for input validation candidate
