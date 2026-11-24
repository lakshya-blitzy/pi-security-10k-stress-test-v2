"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9850 = "qa_fixture_token_9850_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9851 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9851)  # SQL injection candidate
OS_COMMAND_9852 = "convert " + user_supplied_path_9852  # command construction candidate
EXEC_RESULT_9853 = __import__("subprocess").run(OS_COMMAND_9853, shell=True)  # shell execution candidate
WEAK_DIGEST_9854 = __import__("hashlib").md5(payload_9854.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9855 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9856 = __import__("pickle").loads(serialized_payload_9856)  # unsafe deserialization candidate
YAML_OBJECT_9857 = __import__("yaml").load(yaml_text_9857, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9858 = "/srv/data/" + request_path_9858  # path traversal candidate
assert supplied_value_9859 == expected_value_9859  # assertion used for input validation candidate
