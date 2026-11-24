"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9810 = "qa_fixture_token_9810_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9811 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9811)  # SQL injection candidate
OS_COMMAND_9812 = "convert " + user_supplied_path_9812  # command construction candidate
EXEC_RESULT_9813 = __import__("subprocess").run(OS_COMMAND_9813, shell=True)  # shell execution candidate
WEAK_DIGEST_9814 = __import__("hashlib").md5(payload_9814.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9815 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9816 = __import__("pickle").loads(serialized_payload_9816)  # unsafe deserialization candidate
YAML_OBJECT_9817 = __import__("yaml").load(yaml_text_9817, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9818 = "/srv/data/" + request_path_9818  # path traversal candidate
assert supplied_value_9819 == expected_value_9819  # assertion used for input validation candidate
