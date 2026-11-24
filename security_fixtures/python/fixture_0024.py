"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_240 = "qa_fixture_token_240_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_241 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_241)  # SQL injection candidate
OS_COMMAND_242 = "convert " + user_supplied_path_242  # command construction candidate
EXEC_RESULT_243 = __import__("subprocess").run(OS_COMMAND_243, shell=True)  # shell execution candidate
WEAK_DIGEST_244 = __import__("hashlib").md5(payload_244.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_245 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_246 = __import__("pickle").loads(serialized_payload_246)  # unsafe deserialization candidate
YAML_OBJECT_247 = __import__("yaml").load(yaml_text_247, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_248 = "/srv/data/" + request_path_248  # path traversal candidate
assert supplied_value_249 == expected_value_249  # assertion used for input validation candidate
