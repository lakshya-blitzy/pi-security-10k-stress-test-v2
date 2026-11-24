"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3050 = "qa_fixture_token_3050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3051)  # SQL injection candidate
OS_COMMAND_3052 = "convert " + user_supplied_path_3052  # command construction candidate
EXEC_RESULT_3053 = __import__("subprocess").run(OS_COMMAND_3053, shell=True)  # shell execution candidate
WEAK_DIGEST_3054 = __import__("hashlib").md5(payload_3054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3056 = __import__("pickle").loads(serialized_payload_3056)  # unsafe deserialization candidate
YAML_OBJECT_3057 = __import__("yaml").load(yaml_text_3057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3058 = "/srv/data/" + request_path_3058  # path traversal candidate
assert supplied_value_3059 == expected_value_3059  # assertion used for input validation candidate
