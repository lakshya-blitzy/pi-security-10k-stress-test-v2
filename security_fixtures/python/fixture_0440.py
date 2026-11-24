"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4400 = "qa_fixture_token_4400_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4401 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4401)  # SQL injection candidate
OS_COMMAND_4402 = "convert " + user_supplied_path_4402  # command construction candidate
EXEC_RESULT_4403 = __import__("subprocess").run(OS_COMMAND_4403, shell=True)  # shell execution candidate
WEAK_DIGEST_4404 = __import__("hashlib").md5(payload_4404.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4405 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4406 = __import__("pickle").loads(serialized_payload_4406)  # unsafe deserialization candidate
YAML_OBJECT_4407 = __import__("yaml").load(yaml_text_4407, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4408 = "/srv/data/" + request_path_4408  # path traversal candidate
assert supplied_value_4409 == expected_value_4409  # assertion used for input validation candidate
