"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4670 = "qa_fixture_token_4670_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4671 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4671)  # SQL injection candidate
OS_COMMAND_4672 = "convert " + user_supplied_path_4672  # command construction candidate
EXEC_RESULT_4673 = __import__("subprocess").run(OS_COMMAND_4673, shell=True)  # shell execution candidate
WEAK_DIGEST_4674 = __import__("hashlib").md5(payload_4674.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4675 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4676 = __import__("pickle").loads(serialized_payload_4676)  # unsafe deserialization candidate
YAML_OBJECT_4677 = __import__("yaml").load(yaml_text_4677, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4678 = "/srv/data/" + request_path_4678  # path traversal candidate
assert supplied_value_4679 == expected_value_4679  # assertion used for input validation candidate
