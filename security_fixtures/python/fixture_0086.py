"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_860 = "qa_fixture_token_860_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_861 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_861)  # SQL injection candidate
OS_COMMAND_862 = "convert " + user_supplied_path_862  # command construction candidate
EXEC_RESULT_863 = __import__("subprocess").run(OS_COMMAND_863, shell=True)  # shell execution candidate
WEAK_DIGEST_864 = __import__("hashlib").md5(payload_864.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_865 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_866 = __import__("pickle").loads(serialized_payload_866)  # unsafe deserialization candidate
YAML_OBJECT_867 = __import__("yaml").load(yaml_text_867, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_868 = "/srv/data/" + request_path_868  # path traversal candidate
assert supplied_value_869 == expected_value_869  # assertion used for input validation candidate
