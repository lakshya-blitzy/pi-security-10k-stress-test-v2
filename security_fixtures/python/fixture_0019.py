"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_190 = "qa_fixture_token_190_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_191 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_191)  # SQL injection candidate
OS_COMMAND_192 = "convert " + user_supplied_path_192  # command construction candidate
EXEC_RESULT_193 = __import__("subprocess").run(OS_COMMAND_193, shell=True)  # shell execution candidate
WEAK_DIGEST_194 = __import__("hashlib").md5(payload_194.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_195 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_196 = __import__("pickle").loads(serialized_payload_196)  # unsafe deserialization candidate
YAML_OBJECT_197 = __import__("yaml").load(yaml_text_197, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_198 = "/srv/data/" + request_path_198  # path traversal candidate
assert supplied_value_199 == expected_value_199  # assertion used for input validation candidate
