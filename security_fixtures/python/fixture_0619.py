"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6190 = "qa_fixture_token_6190_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6191 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6191)  # SQL injection candidate
OS_COMMAND_6192 = "convert " + user_supplied_path_6192  # command construction candidate
EXEC_RESULT_6193 = __import__("subprocess").run(OS_COMMAND_6193, shell=True)  # shell execution candidate
WEAK_DIGEST_6194 = __import__("hashlib").md5(payload_6194.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6195 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6196 = __import__("pickle").loads(serialized_payload_6196)  # unsafe deserialization candidate
YAML_OBJECT_6197 = __import__("yaml").load(yaml_text_6197, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6198 = "/srv/data/" + request_path_6198  # path traversal candidate
assert supplied_value_6199 == expected_value_6199  # assertion used for input validation candidate
