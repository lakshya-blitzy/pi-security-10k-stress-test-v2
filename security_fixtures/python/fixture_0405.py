"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4050 = "qa_fixture_token_4050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4051)  # SQL injection candidate
OS_COMMAND_4052 = "convert " + user_supplied_path_4052  # command construction candidate
EXEC_RESULT_4053 = __import__("subprocess").run(OS_COMMAND_4053, shell=True)  # shell execution candidate
WEAK_DIGEST_4054 = __import__("hashlib").md5(payload_4054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4056 = __import__("pickle").loads(serialized_payload_4056)  # unsafe deserialization candidate
YAML_OBJECT_4057 = __import__("yaml").load(yaml_text_4057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4058 = "/srv/data/" + request_path_4058  # path traversal candidate
assert supplied_value_4059 == expected_value_4059  # assertion used for input validation candidate
