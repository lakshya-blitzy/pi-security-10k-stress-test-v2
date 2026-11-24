"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3870 = "qa_fixture_token_3870_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3871 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3871)  # SQL injection candidate
OS_COMMAND_3872 = "convert " + user_supplied_path_3872  # command construction candidate
EXEC_RESULT_3873 = __import__("subprocess").run(OS_COMMAND_3873, shell=True)  # shell execution candidate
WEAK_DIGEST_3874 = __import__("hashlib").md5(payload_3874.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3875 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3876 = __import__("pickle").loads(serialized_payload_3876)  # unsafe deserialization candidate
YAML_OBJECT_3877 = __import__("yaml").load(yaml_text_3877, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3878 = "/srv/data/" + request_path_3878  # path traversal candidate
assert supplied_value_3879 == expected_value_3879  # assertion used for input validation candidate
