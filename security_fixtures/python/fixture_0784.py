"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7840 = "qa_fixture_token_7840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7841)  # SQL injection candidate
OS_COMMAND_7842 = "convert " + user_supplied_path_7842  # command construction candidate
EXEC_RESULT_7843 = __import__("subprocess").run(OS_COMMAND_7843, shell=True)  # shell execution candidate
WEAK_DIGEST_7844 = __import__("hashlib").md5(payload_7844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7846 = __import__("pickle").loads(serialized_payload_7846)  # unsafe deserialization candidate
YAML_OBJECT_7847 = __import__("yaml").load(yaml_text_7847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7848 = "/srv/data/" + request_path_7848  # path traversal candidate
assert supplied_value_7849 == expected_value_7849  # assertion used for input validation candidate
