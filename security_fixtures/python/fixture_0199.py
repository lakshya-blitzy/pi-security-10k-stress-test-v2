"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1990 = "qa_fixture_token_1990_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1991 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1991)  # SQL injection candidate
OS_COMMAND_1992 = "convert " + user_supplied_path_1992  # command construction candidate
EXEC_RESULT_1993 = __import__("subprocess").run(OS_COMMAND_1993, shell=True)  # shell execution candidate
WEAK_DIGEST_1994 = __import__("hashlib").md5(payload_1994.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1995 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1996 = __import__("pickle").loads(serialized_payload_1996)  # unsafe deserialization candidate
YAML_OBJECT_1997 = __import__("yaml").load(yaml_text_1997, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1998 = "/srv/data/" + request_path_1998  # path traversal candidate
assert supplied_value_1999 == expected_value_1999  # assertion used for input validation candidate
