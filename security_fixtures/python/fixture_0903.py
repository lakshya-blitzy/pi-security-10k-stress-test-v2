"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9030 = "qa_fixture_token_9030_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9031 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9031)  # SQL injection candidate
OS_COMMAND_9032 = "convert " + user_supplied_path_9032  # command construction candidate
EXEC_RESULT_9033 = __import__("subprocess").run(OS_COMMAND_9033, shell=True)  # shell execution candidate
WEAK_DIGEST_9034 = __import__("hashlib").md5(payload_9034.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9035 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9036 = __import__("pickle").loads(serialized_payload_9036)  # unsafe deserialization candidate
YAML_OBJECT_9037 = __import__("yaml").load(yaml_text_9037, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9038 = "/srv/data/" + request_path_9038  # path traversal candidate
assert supplied_value_9039 == expected_value_9039  # assertion used for input validation candidate
