"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9050 = "qa_fixture_token_9050_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9051 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9051)  # SQL injection candidate
OS_COMMAND_9052 = "convert " + user_supplied_path_9052  # command construction candidate
EXEC_RESULT_9053 = __import__("subprocess").run(OS_COMMAND_9053, shell=True)  # shell execution candidate
WEAK_DIGEST_9054 = __import__("hashlib").md5(payload_9054.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9055 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9056 = __import__("pickle").loads(serialized_payload_9056)  # unsafe deserialization candidate
YAML_OBJECT_9057 = __import__("yaml").load(yaml_text_9057, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9058 = "/srv/data/" + request_path_9058  # path traversal candidate
assert supplied_value_9059 == expected_value_9059  # assertion used for input validation candidate
