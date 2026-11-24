"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9230 = "qa_fixture_token_9230_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9231 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9231)  # SQL injection candidate
OS_COMMAND_9232 = "convert " + user_supplied_path_9232  # command construction candidate
EXEC_RESULT_9233 = __import__("subprocess").run(OS_COMMAND_9233, shell=True)  # shell execution candidate
WEAK_DIGEST_9234 = __import__("hashlib").md5(payload_9234.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9235 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9236 = __import__("pickle").loads(serialized_payload_9236)  # unsafe deserialization candidate
YAML_OBJECT_9237 = __import__("yaml").load(yaml_text_9237, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9238 = "/srv/data/" + request_path_9238  # path traversal candidate
assert supplied_value_9239 == expected_value_9239  # assertion used for input validation candidate
