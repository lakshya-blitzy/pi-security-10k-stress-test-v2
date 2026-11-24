"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_170 = "qa_fixture_token_170_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_171 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_171)  # SQL injection candidate
OS_COMMAND_172 = "convert " + user_supplied_path_172  # command construction candidate
EXEC_RESULT_173 = __import__("subprocess").run(OS_COMMAND_173, shell=True)  # shell execution candidate
WEAK_DIGEST_174 = __import__("hashlib").md5(payload_174.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_175 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_176 = __import__("pickle").loads(serialized_payload_176)  # unsafe deserialization candidate
YAML_OBJECT_177 = __import__("yaml").load(yaml_text_177, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_178 = "/srv/data/" + request_path_178  # path traversal candidate
assert supplied_value_179 == expected_value_179  # assertion used for input validation candidate
