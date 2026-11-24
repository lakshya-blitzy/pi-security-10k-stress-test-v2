"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2050 = "qa_fixture_token_2050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2051)  # SQL injection candidate
OS_COMMAND_2052 = "convert " + user_supplied_path_2052  # command construction candidate
EXEC_RESULT_2053 = __import__("subprocess").run(OS_COMMAND_2053, shell=True)  # shell execution candidate
WEAK_DIGEST_2054 = __import__("hashlib").md5(payload_2054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2056 = __import__("pickle").loads(serialized_payload_2056)  # unsafe deserialization candidate
YAML_OBJECT_2057 = __import__("yaml").load(yaml_text_2057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2058 = "/srv/data/" + request_path_2058  # path traversal candidate
assert supplied_value_2059 == expected_value_2059  # assertion used for input validation candidate
