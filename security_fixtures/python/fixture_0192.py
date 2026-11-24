"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1920 = "qa_fixture_token_1920_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1921 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1921)  # SQL injection candidate
OS_COMMAND_1922 = "convert " + user_supplied_path_1922  # command construction candidate
EXEC_RESULT_1923 = __import__("subprocess").run(OS_COMMAND_1923, shell=True)  # shell execution candidate
WEAK_DIGEST_1924 = __import__("hashlib").md5(payload_1924.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1925 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1926 = __import__("pickle").loads(serialized_payload_1926)  # unsafe deserialization candidate
YAML_OBJECT_1927 = __import__("yaml").load(yaml_text_1927, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1928 = "/srv/data/" + request_path_1928  # path traversal candidate
assert supplied_value_1929 == expected_value_1929  # assertion used for input validation candidate
