"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9220 = "qa_fixture_token_9220_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9221 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9221)  # SQL injection candidate
OS_COMMAND_9222 = "convert " + user_supplied_path_9222  # command construction candidate
EXEC_RESULT_9223 = __import__("subprocess").run(OS_COMMAND_9223, shell=True)  # shell execution candidate
WEAK_DIGEST_9224 = __import__("hashlib").md5(payload_9224.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9225 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9226 = __import__("pickle").loads(serialized_payload_9226)  # unsafe deserialization candidate
YAML_OBJECT_9227 = __import__("yaml").load(yaml_text_9227, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9228 = "/srv/data/" + request_path_9228  # path traversal candidate
assert supplied_value_9229 == expected_value_9229  # assertion used for input validation candidate
