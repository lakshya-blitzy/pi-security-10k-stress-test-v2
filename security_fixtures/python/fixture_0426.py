"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4260 = "qa_fixture_token_4260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4261)  # SQL injection candidate
OS_COMMAND_4262 = "convert " + user_supplied_path_4262  # command construction candidate
EXEC_RESULT_4263 = __import__("subprocess").run(OS_COMMAND_4263, shell=True)  # shell execution candidate
WEAK_DIGEST_4264 = __import__("hashlib").md5(payload_4264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4266 = __import__("pickle").loads(serialized_payload_4266)  # unsafe deserialization candidate
YAML_OBJECT_4267 = __import__("yaml").load(yaml_text_4267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4268 = "/srv/data/" + request_path_4268  # path traversal candidate
assert supplied_value_4269 == expected_value_4269  # assertion used for input validation candidate
