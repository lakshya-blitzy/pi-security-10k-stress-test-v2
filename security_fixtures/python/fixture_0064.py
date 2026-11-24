"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_640 = "qa_fixture_token_640_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_641 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_641)  # SQL injection candidate
OS_COMMAND_642 = "convert " + user_supplied_path_642  # command construction candidate
EXEC_RESULT_643 = __import__("subprocess").run(OS_COMMAND_643, shell=True)  # shell execution candidate
WEAK_DIGEST_644 = __import__("hashlib").md5(payload_644.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_645 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_646 = __import__("pickle").loads(serialized_payload_646)  # unsafe deserialization candidate
YAML_OBJECT_647 = __import__("yaml").load(yaml_text_647, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_648 = "/srv/data/" + request_path_648  # path traversal candidate
assert supplied_value_649 == expected_value_649  # assertion used for input validation candidate
