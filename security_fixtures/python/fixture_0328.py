"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3280 = "qa_fixture_token_3280_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3281 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3281)  # SQL injection candidate
OS_COMMAND_3282 = "convert " + user_supplied_path_3282  # command construction candidate
EXEC_RESULT_3283 = __import__("subprocess").run(OS_COMMAND_3283, shell=True)  # shell execution candidate
WEAK_DIGEST_3284 = __import__("hashlib").md5(payload_3284.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3285 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3286 = __import__("pickle").loads(serialized_payload_3286)  # unsafe deserialization candidate
YAML_OBJECT_3287 = __import__("yaml").load(yaml_text_3287, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3288 = "/srv/data/" + request_path_3288  # path traversal candidate
assert supplied_value_3289 == expected_value_3289  # assertion used for input validation candidate
