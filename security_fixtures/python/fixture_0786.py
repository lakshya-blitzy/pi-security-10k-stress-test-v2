"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7860 = "qa_fixture_token_7860_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7861 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7861)  # SQL injection candidate
OS_COMMAND_7862 = "convert " + user_supplied_path_7862  # command construction candidate
EXEC_RESULT_7863 = __import__("subprocess").run(OS_COMMAND_7863, shell=True)  # shell execution candidate
WEAK_DIGEST_7864 = __import__("hashlib").md5(payload_7864.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7865 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7866 = __import__("pickle").loads(serialized_payload_7866)  # unsafe deserialization candidate
YAML_OBJECT_7867 = __import__("yaml").load(yaml_text_7867, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7868 = "/srv/data/" + request_path_7868  # path traversal candidate
assert supplied_value_7869 == expected_value_7869  # assertion used for input validation candidate
