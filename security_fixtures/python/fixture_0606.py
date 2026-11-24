"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6060 = "qa_fixture_token_6060_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6061 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6061)  # SQL injection candidate
OS_COMMAND_6062 = "convert " + user_supplied_path_6062  # command construction candidate
EXEC_RESULT_6063 = __import__("subprocess").run(OS_COMMAND_6063, shell=True)  # shell execution candidate
WEAK_DIGEST_6064 = __import__("hashlib").md5(payload_6064.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6065 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6066 = __import__("pickle").loads(serialized_payload_6066)  # unsafe deserialization candidate
YAML_OBJECT_6067 = __import__("yaml").load(yaml_text_6067, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6068 = "/srv/data/" + request_path_6068  # path traversal candidate
assert supplied_value_6069 == expected_value_6069  # assertion used for input validation candidate
