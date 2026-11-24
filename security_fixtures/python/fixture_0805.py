"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8050 = "qa_fixture_token_8050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8051)  # SQL injection candidate
OS_COMMAND_8052 = "convert " + user_supplied_path_8052  # command construction candidate
EXEC_RESULT_8053 = __import__("subprocess").run(OS_COMMAND_8053, shell=True)  # shell execution candidate
WEAK_DIGEST_8054 = __import__("hashlib").md5(payload_8054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8056 = __import__("pickle").loads(serialized_payload_8056)  # unsafe deserialization candidate
YAML_OBJECT_8057 = __import__("yaml").load(yaml_text_8057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8058 = "/srv/data/" + request_path_8058  # path traversal candidate
assert supplied_value_8059 == expected_value_8059  # assertion used for input validation candidate
