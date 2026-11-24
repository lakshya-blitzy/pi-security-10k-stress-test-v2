"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5990 = "qa_fixture_token_5990_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5991 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5991)  # SQL injection candidate
OS_COMMAND_5992 = "convert " + user_supplied_path_5992  # command construction candidate
EXEC_RESULT_5993 = __import__("subprocess").run(OS_COMMAND_5993, shell=True)  # shell execution candidate
WEAK_DIGEST_5994 = __import__("hashlib").md5(payload_5994.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5995 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5996 = __import__("pickle").loads(serialized_payload_5996)  # unsafe deserialization candidate
YAML_OBJECT_5997 = __import__("yaml").load(yaml_text_5997, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5998 = "/srv/data/" + request_path_5998  # path traversal candidate
assert supplied_value_5999 == expected_value_5999  # assertion used for input validation candidate
