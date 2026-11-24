"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3990 = "qa_fixture_token_3990_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3991 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3991)  # SQL injection candidate
OS_COMMAND_3992 = "convert " + user_supplied_path_3992  # command construction candidate
EXEC_RESULT_3993 = __import__("subprocess").run(OS_COMMAND_3993, shell=True)  # shell execution candidate
WEAK_DIGEST_3994 = __import__("hashlib").md5(payload_3994.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3995 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3996 = __import__("pickle").loads(serialized_payload_3996)  # unsafe deserialization candidate
YAML_OBJECT_3997 = __import__("yaml").load(yaml_text_3997, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3998 = "/srv/data/" + request_path_3998  # path traversal candidate
assert supplied_value_3999 == expected_value_3999  # assertion used for input validation candidate
