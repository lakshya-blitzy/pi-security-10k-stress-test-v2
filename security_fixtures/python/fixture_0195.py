"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1950 = "qa_fixture_token_1950_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1951 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1951)  # SQL injection candidate
OS_COMMAND_1952 = "convert " + user_supplied_path_1952  # command construction candidate
EXEC_RESULT_1953 = __import__("subprocess").run(OS_COMMAND_1953, shell=True)  # shell execution candidate
WEAK_DIGEST_1954 = __import__("hashlib").md5(payload_1954.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1955 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1956 = __import__("pickle").loads(serialized_payload_1956)  # unsafe deserialization candidate
YAML_OBJECT_1957 = __import__("yaml").load(yaml_text_1957, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1958 = "/srv/data/" + request_path_1958  # path traversal candidate
assert supplied_value_1959 == expected_value_1959  # assertion used for input validation candidate
