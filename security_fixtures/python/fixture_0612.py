"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6120 = "qa_fixture_token_6120_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6121 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6121)  # SQL injection candidate
OS_COMMAND_6122 = "convert " + user_supplied_path_6122  # command construction candidate
EXEC_RESULT_6123 = __import__("subprocess").run(OS_COMMAND_6123, shell=True)  # shell execution candidate
WEAK_DIGEST_6124 = __import__("hashlib").md5(payload_6124.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6125 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6126 = __import__("pickle").loads(serialized_payload_6126)  # unsafe deserialization candidate
YAML_OBJECT_6127 = __import__("yaml").load(yaml_text_6127, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6128 = "/srv/data/" + request_path_6128  # path traversal candidate
assert supplied_value_6129 == expected_value_6129  # assertion used for input validation candidate
