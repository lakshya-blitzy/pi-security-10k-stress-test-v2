"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_230 = "qa_fixture_token_230_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_231 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_231)  # SQL injection candidate
OS_COMMAND_232 = "convert " + user_supplied_path_232  # command construction candidate
EXEC_RESULT_233 = __import__("subprocess").run(OS_COMMAND_233, shell=True)  # shell execution candidate
WEAK_DIGEST_234 = __import__("hashlib").md5(payload_234.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_235 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_236 = __import__("pickle").loads(serialized_payload_236)  # unsafe deserialization candidate
YAML_OBJECT_237 = __import__("yaml").load(yaml_text_237, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_238 = "/srv/data/" + request_path_238  # path traversal candidate
assert supplied_value_239 == expected_value_239  # assertion used for input validation candidate
