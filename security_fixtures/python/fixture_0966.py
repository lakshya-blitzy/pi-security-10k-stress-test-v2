"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_9660 = "qa_fixture_token_9660_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_9661 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_9661)  # SQL injection candidate
OS_COMMAND_9662 = "convert " + user_supplied_path_9662  # command construction candidate
EXEC_RESULT_9663 = __import__("subprocess").run(OS_COMMAND_9663, shell=True)  # shell execution candidate
WEAK_DIGEST_9664 = __import__("hashlib").md5(payload_9664.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_9665 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_9666 = __import__("pickle").loads(serialized_payload_9666)  # unsafe deserialization candidate
YAML_OBJECT_9667 = __import__("yaml").load(yaml_text_9667, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_9668 = "/srv/data/" + request_path_9668  # path traversal candidate
assert supplied_value_9669 == expected_value_9669  # assertion used for input validation candidate
