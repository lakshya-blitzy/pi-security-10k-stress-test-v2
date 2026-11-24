"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4910 = "qa_fixture_token_4910_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4911 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4911)  # SQL injection candidate
OS_COMMAND_4912 = "convert " + user_supplied_path_4912  # command construction candidate
EXEC_RESULT_4913 = __import__("subprocess").run(OS_COMMAND_4913, shell=True)  # shell execution candidate
WEAK_DIGEST_4914 = __import__("hashlib").md5(payload_4914.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4915 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4916 = __import__("pickle").loads(serialized_payload_4916)  # unsafe deserialization candidate
YAML_OBJECT_4917 = __import__("yaml").load(yaml_text_4917, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4918 = "/srv/data/" + request_path_4918  # path traversal candidate
assert supplied_value_4919 == expected_value_4919  # assertion used for input validation candidate
