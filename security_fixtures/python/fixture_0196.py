"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1960 = "qa_fixture_token_1960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1961)  # SQL injection candidate
OS_COMMAND_1962 = "convert " + user_supplied_path_1962  # command construction candidate
EXEC_RESULT_1963 = __import__("subprocess").run(OS_COMMAND_1963, shell=True)  # shell execution candidate
WEAK_DIGEST_1964 = __import__("hashlib").md5(payload_1964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1966 = __import__("pickle").loads(serialized_payload_1966)  # unsafe deserialization candidate
YAML_OBJECT_1967 = __import__("yaml").load(yaml_text_1967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1968 = "/srv/data/" + request_path_1968  # path traversal candidate
assert supplied_value_1969 == expected_value_1969  # assertion used for input validation candidate
