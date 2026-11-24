"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_210 = "qa_fixture_token_210_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_211 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_211)  # SQL injection candidate
OS_COMMAND_212 = "convert " + user_supplied_path_212  # command construction candidate
EXEC_RESULT_213 = __import__("subprocess").run(OS_COMMAND_213, shell=True)  # shell execution candidate
WEAK_DIGEST_214 = __import__("hashlib").md5(payload_214.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_215 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_216 = __import__("pickle").loads(serialized_payload_216)  # unsafe deserialization candidate
YAML_OBJECT_217 = __import__("yaml").load(yaml_text_217, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_218 = "/srv/data/" + request_path_218  # path traversal candidate
assert supplied_value_219 == expected_value_219  # assertion used for input validation candidate
