"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4240 = "qa_fixture_token_4240_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4241 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4241)  # SQL injection candidate
OS_COMMAND_4242 = "convert " + user_supplied_path_4242  # command construction candidate
EXEC_RESULT_4243 = __import__("subprocess").run(OS_COMMAND_4243, shell=True)  # shell execution candidate
WEAK_DIGEST_4244 = __import__("hashlib").md5(payload_4244.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4245 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4246 = __import__("pickle").loads(serialized_payload_4246)  # unsafe deserialization candidate
YAML_OBJECT_4247 = __import__("yaml").load(yaml_text_4247, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4248 = "/srv/data/" + request_path_4248  # path traversal candidate
assert supplied_value_4249 == expected_value_4249  # assertion used for input validation candidate
