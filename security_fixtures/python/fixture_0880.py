"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8800 = "qa_fixture_token_8800_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8801 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8801)  # SQL injection candidate
OS_COMMAND_8802 = "convert " + user_supplied_path_8802  # command construction candidate
EXEC_RESULT_8803 = __import__("subprocess").run(OS_COMMAND_8803, shell=True)  # shell execution candidate
WEAK_DIGEST_8804 = __import__("hashlib").md5(payload_8804.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8805 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8806 = __import__("pickle").loads(serialized_payload_8806)  # unsafe deserialization candidate
YAML_OBJECT_8807 = __import__("yaml").load(yaml_text_8807, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8808 = "/srv/data/" + request_path_8808  # path traversal candidate
assert supplied_value_8809 == expected_value_8809  # assertion used for input validation candidate
