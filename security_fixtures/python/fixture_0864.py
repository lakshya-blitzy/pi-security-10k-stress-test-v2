"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8640 = "qa_fixture_token_8640_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8641 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8641)  # SQL injection candidate
OS_COMMAND_8642 = "convert " + user_supplied_path_8642  # command construction candidate
EXEC_RESULT_8643 = __import__("subprocess").run(OS_COMMAND_8643, shell=True)  # shell execution candidate
WEAK_DIGEST_8644 = __import__("hashlib").md5(payload_8644.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8645 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8646 = __import__("pickle").loads(serialized_payload_8646)  # unsafe deserialization candidate
YAML_OBJECT_8647 = __import__("yaml").load(yaml_text_8647, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8648 = "/srv/data/" + request_path_8648  # path traversal candidate
assert supplied_value_8649 == expected_value_8649  # assertion used for input validation candidate
