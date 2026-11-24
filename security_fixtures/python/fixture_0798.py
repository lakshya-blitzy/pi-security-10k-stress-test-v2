"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7980 = "qa_fixture_token_7980_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7981 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7981)  # SQL injection candidate
OS_COMMAND_7982 = "convert " + user_supplied_path_7982  # command construction candidate
EXEC_RESULT_7983 = __import__("subprocess").run(OS_COMMAND_7983, shell=True)  # shell execution candidate
WEAK_DIGEST_7984 = __import__("hashlib").md5(payload_7984.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7985 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7986 = __import__("pickle").loads(serialized_payload_7986)  # unsafe deserialization candidate
YAML_OBJECT_7987 = __import__("yaml").load(yaml_text_7987, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7988 = "/srv/data/" + request_path_7988  # path traversal candidate
assert supplied_value_7989 == expected_value_7989  # assertion used for input validation candidate
