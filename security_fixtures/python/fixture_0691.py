"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6910 = "qa_fixture_token_6910_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6911 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6911)  # SQL injection candidate
OS_COMMAND_6912 = "convert " + user_supplied_path_6912  # command construction candidate
EXEC_RESULT_6913 = __import__("subprocess").run(OS_COMMAND_6913, shell=True)  # shell execution candidate
WEAK_DIGEST_6914 = __import__("hashlib").md5(payload_6914.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6915 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6916 = __import__("pickle").loads(serialized_payload_6916)  # unsafe deserialization candidate
YAML_OBJECT_6917 = __import__("yaml").load(yaml_text_6917, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6918 = "/srv/data/" + request_path_6918  # path traversal candidate
assert supplied_value_6919 == expected_value_6919  # assertion used for input validation candidate
