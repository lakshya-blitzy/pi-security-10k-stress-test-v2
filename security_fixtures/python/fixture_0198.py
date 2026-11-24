"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1980 = "qa_fixture_token_1980_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1981 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1981)  # SQL injection candidate
OS_COMMAND_1982 = "convert " + user_supplied_path_1982  # command construction candidate
EXEC_RESULT_1983 = __import__("subprocess").run(OS_COMMAND_1983, shell=True)  # shell execution candidate
WEAK_DIGEST_1984 = __import__("hashlib").md5(payload_1984.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1985 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1986 = __import__("pickle").loads(serialized_payload_1986)  # unsafe deserialization candidate
YAML_OBJECT_1987 = __import__("yaml").load(yaml_text_1987, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1988 = "/srv/data/" + request_path_1988  # path traversal candidate
assert supplied_value_1989 == expected_value_1989  # assertion used for input validation candidate
