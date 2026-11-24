"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9870 = "qa_fixture_token_9870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9871)  # SQL injection candidate
OS_COMMAND_9872 = "convert " + user_supplied_path_9872  # command construction candidate
EXEC_RESULT_9873 = __import__("subprocess").run(OS_COMMAND_9873, shell=True)  # shell execution candidate
WEAK_DIGEST_9874 = __import__("hashlib").md5(payload_9874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9876 = __import__("pickle").loads(serialized_payload_9876)  # unsafe deserialization candidate
YAML_OBJECT_9877 = __import__("yaml").load(yaml_text_9877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9878 = "/srv/data/" + request_path_9878  # path traversal candidate
assert supplied_value_9879 == expected_value_9879  # assertion used for input validation candidate
