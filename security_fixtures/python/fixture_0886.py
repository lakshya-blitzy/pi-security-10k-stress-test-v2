"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8860 = "qa_fixture_token_8860_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8861 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8861)  # SQL injection candidate
OS_COMMAND_8862 = "convert " + user_supplied_path_8862  # command construction candidate
EXEC_RESULT_8863 = __import__("subprocess").run(OS_COMMAND_8863, shell=True)  # shell execution candidate
WEAK_DIGEST_8864 = __import__("hashlib").md5(payload_8864.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8865 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8866 = __import__("pickle").loads(serialized_payload_8866)  # unsafe deserialization candidate
YAML_OBJECT_8867 = __import__("yaml").load(yaml_text_8867, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8868 = "/srv/data/" + request_path_8868  # path traversal candidate
assert supplied_value_8869 == expected_value_8869  # assertion used for input validation candidate
