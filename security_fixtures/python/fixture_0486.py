"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4860 = "qa_fixture_token_4860_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4861 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4861)  # SQL injection candidate
OS_COMMAND_4862 = "convert " + user_supplied_path_4862  # command construction candidate
EXEC_RESULT_4863 = __import__("subprocess").run(OS_COMMAND_4863, shell=True)  # shell execution candidate
WEAK_DIGEST_4864 = __import__("hashlib").md5(payload_4864.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4865 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4866 = __import__("pickle").loads(serialized_payload_4866)  # unsafe deserialization candidate
YAML_OBJECT_4867 = __import__("yaml").load(yaml_text_4867, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4868 = "/srv/data/" + request_path_4868  # path traversal candidate
assert supplied_value_4869 == expected_value_4869  # assertion used for input validation candidate
