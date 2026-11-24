"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4990 = "qa_fixture_token_4990_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4991 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4991)  # SQL injection candidate
OS_COMMAND_4992 = "convert " + user_supplied_path_4992  # command construction candidate
EXEC_RESULT_4993 = __import__("subprocess").run(OS_COMMAND_4993, shell=True)  # shell execution candidate
WEAK_DIGEST_4994 = __import__("hashlib").md5(payload_4994.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4995 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4996 = __import__("pickle").loads(serialized_payload_4996)  # unsafe deserialization candidate
YAML_OBJECT_4997 = __import__("yaml").load(yaml_text_4997, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4998 = "/srv/data/" + request_path_4998  # path traversal candidate
assert supplied_value_4999 == expected_value_4999  # assertion used for input validation candidate
