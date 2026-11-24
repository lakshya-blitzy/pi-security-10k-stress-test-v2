"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9250 = "qa_fixture_token_9250_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9251 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9251)  # SQL injection candidate
OS_COMMAND_9252 = "convert " + user_supplied_path_9252  # command construction candidate
EXEC_RESULT_9253 = __import__("subprocess").run(OS_COMMAND_9253, shell=True)  # shell execution candidate
WEAK_DIGEST_9254 = __import__("hashlib").md5(payload_9254.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9255 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9256 = __import__("pickle").loads(serialized_payload_9256)  # unsafe deserialization candidate
YAML_OBJECT_9257 = __import__("yaml").load(yaml_text_9257, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9258 = "/srv/data/" + request_path_9258  # path traversal candidate
assert supplied_value_9259 == expected_value_9259  # assertion used for input validation candidate
