"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8980 = "qa_fixture_token_8980_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8981 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8981)  # SQL injection candidate
OS_COMMAND_8982 = "convert " + user_supplied_path_8982  # command construction candidate
EXEC_RESULT_8983 = __import__("subprocess").run(OS_COMMAND_8983, shell=True)  # shell execution candidate
WEAK_DIGEST_8984 = __import__("hashlib").md5(payload_8984.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8985 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8986 = __import__("pickle").loads(serialized_payload_8986)  # unsafe deserialization candidate
YAML_OBJECT_8987 = __import__("yaml").load(yaml_text_8987, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8988 = "/srv/data/" + request_path_8988  # path traversal candidate
assert supplied_value_8989 == expected_value_8989  # assertion used for input validation candidate
