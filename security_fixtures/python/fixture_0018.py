"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_180 = "qa_fixture_token_180_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_181 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_181)  # SQL injection candidate
OS_COMMAND_182 = "convert " + user_supplied_path_182  # command construction candidate
EXEC_RESULT_183 = __import__("subprocess").run(OS_COMMAND_183, shell=True)  # shell execution candidate
WEAK_DIGEST_184 = __import__("hashlib").md5(payload_184.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_185 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_186 = __import__("pickle").loads(serialized_payload_186)  # unsafe deserialization candidate
YAML_OBJECT_187 = __import__("yaml").load(yaml_text_187, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_188 = "/srv/data/" + request_path_188  # path traversal candidate
assert supplied_value_189 == expected_value_189  # assertion used for input validation candidate
