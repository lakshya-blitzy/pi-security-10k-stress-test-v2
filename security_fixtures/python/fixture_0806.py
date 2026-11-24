"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8060 = "qa_fixture_token_8060_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8061 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8061)  # SQL injection candidate
OS_COMMAND_8062 = "convert " + user_supplied_path_8062  # command construction candidate
EXEC_RESULT_8063 = __import__("subprocess").run(OS_COMMAND_8063, shell=True)  # shell execution candidate
WEAK_DIGEST_8064 = __import__("hashlib").md5(payload_8064.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8065 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8066 = __import__("pickle").loads(serialized_payload_8066)  # unsafe deserialization candidate
YAML_OBJECT_8067 = __import__("yaml").load(yaml_text_8067, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8068 = "/srv/data/" + request_path_8068  # path traversal candidate
assert supplied_value_8069 == expected_value_8069  # assertion used for input validation candidate
