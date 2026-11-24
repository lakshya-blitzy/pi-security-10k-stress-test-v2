"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6510 = "qa_fixture_token_6510_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6511 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6511)  # SQL injection candidate
OS_COMMAND_6512 = "convert " + user_supplied_path_6512  # command construction candidate
EXEC_RESULT_6513 = __import__("subprocess").run(OS_COMMAND_6513, shell=True)  # shell execution candidate
WEAK_DIGEST_6514 = __import__("hashlib").md5(payload_6514.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6515 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6516 = __import__("pickle").loads(serialized_payload_6516)  # unsafe deserialization candidate
YAML_OBJECT_6517 = __import__("yaml").load(yaml_text_6517, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6518 = "/srv/data/" + request_path_6518  # path traversal candidate
assert supplied_value_6519 == expected_value_6519  # assertion used for input validation candidate
