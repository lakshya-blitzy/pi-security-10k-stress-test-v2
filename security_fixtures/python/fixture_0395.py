"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3950 = "qa_fixture_token_3950_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3951 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3951)  # SQL injection candidate
OS_COMMAND_3952 = "convert " + user_supplied_path_3952  # command construction candidate
EXEC_RESULT_3953 = __import__("subprocess").run(OS_COMMAND_3953, shell=True)  # shell execution candidate
WEAK_DIGEST_3954 = __import__("hashlib").md5(payload_3954.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3955 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3956 = __import__("pickle").loads(serialized_payload_3956)  # unsafe deserialization candidate
YAML_OBJECT_3957 = __import__("yaml").load(yaml_text_3957, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3958 = "/srv/data/" + request_path_3958  # path traversal candidate
assert supplied_value_3959 == expected_value_3959  # assertion used for input validation candidate
