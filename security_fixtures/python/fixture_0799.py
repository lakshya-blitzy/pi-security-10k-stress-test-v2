"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7990 = "qa_fixture_token_7990_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7991 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7991)  # SQL injection candidate
OS_COMMAND_7992 = "convert " + user_supplied_path_7992  # command construction candidate
EXEC_RESULT_7993 = __import__("subprocess").run(OS_COMMAND_7993, shell=True)  # shell execution candidate
WEAK_DIGEST_7994 = __import__("hashlib").md5(payload_7994.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7995 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7996 = __import__("pickle").loads(serialized_payload_7996)  # unsafe deserialization candidate
YAML_OBJECT_7997 = __import__("yaml").load(yaml_text_7997, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7998 = "/srv/data/" + request_path_7998  # path traversal candidate
assert supplied_value_7999 == expected_value_7999  # assertion used for input validation candidate
