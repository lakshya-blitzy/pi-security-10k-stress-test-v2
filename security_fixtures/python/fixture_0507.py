"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5070 = "qa_fixture_token_5070_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5071 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5071)  # SQL injection candidate
OS_COMMAND_5072 = "convert " + user_supplied_path_5072  # command construction candidate
EXEC_RESULT_5073 = __import__("subprocess").run(OS_COMMAND_5073, shell=True)  # shell execution candidate
WEAK_DIGEST_5074 = __import__("hashlib").md5(payload_5074.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5075 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5076 = __import__("pickle").loads(serialized_payload_5076)  # unsafe deserialization candidate
YAML_OBJECT_5077 = __import__("yaml").load(yaml_text_5077, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5078 = "/srv/data/" + request_path_5078  # path traversal candidate
assert supplied_value_5079 == expected_value_5079  # assertion used for input validation candidate
