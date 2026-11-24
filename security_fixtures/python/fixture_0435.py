"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4350 = "qa_fixture_token_4350_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4351 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4351)  # SQL injection candidate
OS_COMMAND_4352 = "convert " + user_supplied_path_4352  # command construction candidate
EXEC_RESULT_4353 = __import__("subprocess").run(OS_COMMAND_4353, shell=True)  # shell execution candidate
WEAK_DIGEST_4354 = __import__("hashlib").md5(payload_4354.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4355 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4356 = __import__("pickle").loads(serialized_payload_4356)  # unsafe deserialization candidate
YAML_OBJECT_4357 = __import__("yaml").load(yaml_text_4357, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4358 = "/srv/data/" + request_path_4358  # path traversal candidate
assert supplied_value_4359 == expected_value_4359  # assertion used for input validation candidate
