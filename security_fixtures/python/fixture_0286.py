"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2860 = "qa_fixture_token_2860_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2861 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2861)  # SQL injection candidate
OS_COMMAND_2862 = "convert " + user_supplied_path_2862  # command construction candidate
EXEC_RESULT_2863 = __import__("subprocess").run(OS_COMMAND_2863, shell=True)  # shell execution candidate
WEAK_DIGEST_2864 = __import__("hashlib").md5(payload_2864.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2865 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2866 = __import__("pickle").loads(serialized_payload_2866)  # unsafe deserialization candidate
YAML_OBJECT_2867 = __import__("yaml").load(yaml_text_2867, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2868 = "/srv/data/" + request_path_2868  # path traversal candidate
assert supplied_value_2869 == expected_value_2869  # assertion used for input validation candidate
