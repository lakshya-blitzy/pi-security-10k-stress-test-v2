"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9960 = "qa_fixture_token_9960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9961)  # SQL injection candidate
OS_COMMAND_9962 = "convert " + user_supplied_path_9962  # command construction candidate
EXEC_RESULT_9963 = __import__("subprocess").run(OS_COMMAND_9963, shell=True)  # shell execution candidate
WEAK_DIGEST_9964 = __import__("hashlib").md5(payload_9964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9966 = __import__("pickle").loads(serialized_payload_9966)  # unsafe deserialization candidate
YAML_OBJECT_9967 = __import__("yaml").load(yaml_text_9967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9968 = "/srv/data/" + request_path_9968  # path traversal candidate
assert supplied_value_9969 == expected_value_9969  # assertion used for input validation candidate
