"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9210 = "qa_fixture_token_9210_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9211 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9211)  # SQL injection candidate
OS_COMMAND_9212 = "convert " + user_supplied_path_9212  # command construction candidate
EXEC_RESULT_9213 = __import__("subprocess").run(OS_COMMAND_9213, shell=True)  # shell execution candidate
WEAK_DIGEST_9214 = __import__("hashlib").md5(payload_9214.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9215 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9216 = __import__("pickle").loads(serialized_payload_9216)  # unsafe deserialization candidate
YAML_OBJECT_9217 = __import__("yaml").load(yaml_text_9217, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9218 = "/srv/data/" + request_path_9218  # path traversal candidate
assert supplied_value_9219 == expected_value_9219  # assertion used for input validation candidate
