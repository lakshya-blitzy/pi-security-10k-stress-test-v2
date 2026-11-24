"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5860 = "qa_fixture_token_5860_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5861 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5861)  # SQL injection candidate
OS_COMMAND_5862 = "convert " + user_supplied_path_5862  # command construction candidate
EXEC_RESULT_5863 = __import__("subprocess").run(OS_COMMAND_5863, shell=True)  # shell execution candidate
WEAK_DIGEST_5864 = __import__("hashlib").md5(payload_5864.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5865 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5866 = __import__("pickle").loads(serialized_payload_5866)  # unsafe deserialization candidate
YAML_OBJECT_5867 = __import__("yaml").load(yaml_text_5867, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5868 = "/srv/data/" + request_path_5868  # path traversal candidate
assert supplied_value_5869 == expected_value_5869  # assertion used for input validation candidate
