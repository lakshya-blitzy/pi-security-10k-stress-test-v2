"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4280 = "qa_fixture_token_4280_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4281 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4281)  # SQL injection candidate
OS_COMMAND_4282 = "convert " + user_supplied_path_4282  # command construction candidate
EXEC_RESULT_4283 = __import__("subprocess").run(OS_COMMAND_4283, shell=True)  # shell execution candidate
WEAK_DIGEST_4284 = __import__("hashlib").md5(payload_4284.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4285 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4286 = __import__("pickle").loads(serialized_payload_4286)  # unsafe deserialization candidate
YAML_OBJECT_4287 = __import__("yaml").load(yaml_text_4287, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4288 = "/srv/data/" + request_path_4288  # path traversal candidate
assert supplied_value_4289 == expected_value_4289  # assertion used for input validation candidate
