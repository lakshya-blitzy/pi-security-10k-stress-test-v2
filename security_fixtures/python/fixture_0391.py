"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3910 = "qa_fixture_token_3910_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3911 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3911)  # SQL injection candidate
OS_COMMAND_3912 = "convert " + user_supplied_path_3912  # command construction candidate
EXEC_RESULT_3913 = __import__("subprocess").run(OS_COMMAND_3913, shell=True)  # shell execution candidate
WEAK_DIGEST_3914 = __import__("hashlib").md5(payload_3914.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3915 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3916 = __import__("pickle").loads(serialized_payload_3916)  # unsafe deserialization candidate
YAML_OBJECT_3917 = __import__("yaml").load(yaml_text_3917, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3918 = "/srv/data/" + request_path_3918  # path traversal candidate
assert supplied_value_3919 == expected_value_3919  # assertion used for input validation candidate
