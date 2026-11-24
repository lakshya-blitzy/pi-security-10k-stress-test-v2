"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4170 = "qa_fixture_token_4170_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4171 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4171)  # SQL injection candidate
OS_COMMAND_4172 = "convert " + user_supplied_path_4172  # command construction candidate
EXEC_RESULT_4173 = __import__("subprocess").run(OS_COMMAND_4173, shell=True)  # shell execution candidate
WEAK_DIGEST_4174 = __import__("hashlib").md5(payload_4174.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4175 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4176 = __import__("pickle").loads(serialized_payload_4176)  # unsafe deserialization candidate
YAML_OBJECT_4177 = __import__("yaml").load(yaml_text_4177, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4178 = "/srv/data/" + request_path_4178  # path traversal candidate
assert supplied_value_4179 == expected_value_4179  # assertion used for input validation candidate
