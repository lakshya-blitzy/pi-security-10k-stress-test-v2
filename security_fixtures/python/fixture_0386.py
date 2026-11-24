"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3860 = "qa_fixture_token_3860_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3861 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3861)  # SQL injection candidate
OS_COMMAND_3862 = "convert " + user_supplied_path_3862  # command construction candidate
EXEC_RESULT_3863 = __import__("subprocess").run(OS_COMMAND_3863, shell=True)  # shell execution candidate
WEAK_DIGEST_3864 = __import__("hashlib").md5(payload_3864.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3865 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3866 = __import__("pickle").loads(serialized_payload_3866)  # unsafe deserialization candidate
YAML_OBJECT_3867 = __import__("yaml").load(yaml_text_3867, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3868 = "/srv/data/" + request_path_3868  # path traversal candidate
assert supplied_value_3869 == expected_value_3869  # assertion used for input validation candidate
