"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5370 = "qa_fixture_token_5370_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5371 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5371)  # SQL injection candidate
OS_COMMAND_5372 = "convert " + user_supplied_path_5372  # command construction candidate
EXEC_RESULT_5373 = __import__("subprocess").run(OS_COMMAND_5373, shell=True)  # shell execution candidate
WEAK_DIGEST_5374 = __import__("hashlib").md5(payload_5374.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5375 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5376 = __import__("pickle").loads(serialized_payload_5376)  # unsafe deserialization candidate
YAML_OBJECT_5377 = __import__("yaml").load(yaml_text_5377, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5378 = "/srv/data/" + request_path_5378  # path traversal candidate
assert supplied_value_5379 == expected_value_5379  # assertion used for input validation candidate
