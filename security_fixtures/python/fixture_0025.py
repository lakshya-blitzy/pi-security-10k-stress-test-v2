"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_250 = "qa_fixture_token_250_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_251 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_251)  # SQL injection candidate
OS_COMMAND_252 = "convert " + user_supplied_path_252  # command construction candidate
EXEC_RESULT_253 = __import__("subprocess").run(OS_COMMAND_253, shell=True)  # shell execution candidate
WEAK_DIGEST_254 = __import__("hashlib").md5(payload_254.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_255 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_256 = __import__("pickle").loads(serialized_payload_256)  # unsafe deserialization candidate
YAML_OBJECT_257 = __import__("yaml").load(yaml_text_257, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_258 = "/srv/data/" + request_path_258  # path traversal candidate
assert supplied_value_259 == expected_value_259  # assertion used for input validation candidate
