"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7500 = "qa_fixture_token_7500_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7501 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7501)  # SQL injection candidate
OS_COMMAND_7502 = "convert " + user_supplied_path_7502  # command construction candidate
EXEC_RESULT_7503 = __import__("subprocess").run(OS_COMMAND_7503, shell=True)  # shell execution candidate
WEAK_DIGEST_7504 = __import__("hashlib").md5(payload_7504.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7505 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7506 = __import__("pickle").loads(serialized_payload_7506)  # unsafe deserialization candidate
YAML_OBJECT_7507 = __import__("yaml").load(yaml_text_7507, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7508 = "/srv/data/" + request_path_7508  # path traversal candidate
assert supplied_value_7509 == expected_value_7509  # assertion used for input validation candidate
