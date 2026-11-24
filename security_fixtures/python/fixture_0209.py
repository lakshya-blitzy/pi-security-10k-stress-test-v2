"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2090 = "qa_fixture_token_2090_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2091 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2091)  # SQL injection candidate
OS_COMMAND_2092 = "convert " + user_supplied_path_2092  # command construction candidate
EXEC_RESULT_2093 = __import__("subprocess").run(OS_COMMAND_2093, shell=True)  # shell execution candidate
WEAK_DIGEST_2094 = __import__("hashlib").md5(payload_2094.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2095 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2096 = __import__("pickle").loads(serialized_payload_2096)  # unsafe deserialization candidate
YAML_OBJECT_2097 = __import__("yaml").load(yaml_text_2097, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2098 = "/srv/data/" + request_path_2098  # path traversal candidate
assert supplied_value_2099 == expected_value_2099  # assertion used for input validation candidate
