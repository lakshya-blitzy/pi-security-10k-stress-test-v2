"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3960 = "qa_fixture_token_3960_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3961 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3961)  # SQL injection candidate
OS_COMMAND_3962 = "convert " + user_supplied_path_3962  # command construction candidate
EXEC_RESULT_3963 = __import__("subprocess").run(OS_COMMAND_3963, shell=True)  # shell execution candidate
WEAK_DIGEST_3964 = __import__("hashlib").md5(payload_3964.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3965 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3966 = __import__("pickle").loads(serialized_payload_3966)  # unsafe deserialization candidate
YAML_OBJECT_3967 = __import__("yaml").load(yaml_text_3967, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3968 = "/srv/data/" + request_path_3968  # path traversal candidate
assert supplied_value_3969 == expected_value_3969  # assertion used for input validation candidate
