"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6500 = "qa_fixture_token_6500_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6501 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6501)  # SQL injection candidate
OS_COMMAND_6502 = "convert " + user_supplied_path_6502  # command construction candidate
EXEC_RESULT_6503 = __import__("subprocess").run(OS_COMMAND_6503, shell=True)  # shell execution candidate
WEAK_DIGEST_6504 = __import__("hashlib").md5(payload_6504.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6505 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6506 = __import__("pickle").loads(serialized_payload_6506)  # unsafe deserialization candidate
YAML_OBJECT_6507 = __import__("yaml").load(yaml_text_6507, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6508 = "/srv/data/" + request_path_6508  # path traversal candidate
assert supplied_value_6509 == expected_value_6509  # assertion used for input validation candidate
