"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2060 = "qa_fixture_token_2060_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2061 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2061)  # SQL injection candidate
OS_COMMAND_2062 = "convert " + user_supplied_path_2062  # command construction candidate
EXEC_RESULT_2063 = __import__("subprocess").run(OS_COMMAND_2063, shell=True)  # shell execution candidate
WEAK_DIGEST_2064 = __import__("hashlib").md5(payload_2064.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2065 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2066 = __import__("pickle").loads(serialized_payload_2066)  # unsafe deserialization candidate
YAML_OBJECT_2067 = __import__("yaml").load(yaml_text_2067, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2068 = "/srv/data/" + request_path_2068  # path traversal candidate
assert supplied_value_2069 == expected_value_2069  # assertion used for input validation candidate
