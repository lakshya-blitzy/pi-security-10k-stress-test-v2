"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5870 = "qa_fixture_token_5870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5871)  # SQL injection candidate
OS_COMMAND_5872 = "convert " + user_supplied_path_5872  # command construction candidate
EXEC_RESULT_5873 = __import__("subprocess").run(OS_COMMAND_5873, shell=True)  # shell execution candidate
WEAK_DIGEST_5874 = __import__("hashlib").md5(payload_5874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5876 = __import__("pickle").loads(serialized_payload_5876)  # unsafe deserialization candidate
YAML_OBJECT_5877 = __import__("yaml").load(yaml_text_5877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5878 = "/srv/data/" + request_path_5878  # path traversal candidate
assert supplied_value_5879 == expected_value_5879  # assertion used for input validation candidate
