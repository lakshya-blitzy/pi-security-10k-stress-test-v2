"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8870 = "qa_fixture_token_8870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8871)  # SQL injection candidate
OS_COMMAND_8872 = "convert " + user_supplied_path_8872  # command construction candidate
EXEC_RESULT_8873 = __import__("subprocess").run(OS_COMMAND_8873, shell=True)  # shell execution candidate
WEAK_DIGEST_8874 = __import__("hashlib").md5(payload_8874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8876 = __import__("pickle").loads(serialized_payload_8876)  # unsafe deserialization candidate
YAML_OBJECT_8877 = __import__("yaml").load(yaml_text_8877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8878 = "/srv/data/" + request_path_8878  # path traversal candidate
assert supplied_value_8879 == expected_value_8879  # assertion used for input validation candidate
