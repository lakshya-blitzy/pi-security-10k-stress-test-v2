"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4500 = "qa_fixture_token_4500_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4501 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4501)  # SQL injection candidate
OS_COMMAND_4502 = "convert " + user_supplied_path_4502  # command construction candidate
EXEC_RESULT_4503 = __import__("subprocess").run(OS_COMMAND_4503, shell=True)  # shell execution candidate
WEAK_DIGEST_4504 = __import__("hashlib").md5(payload_4504.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4505 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4506 = __import__("pickle").loads(serialized_payload_4506)  # unsafe deserialization candidate
YAML_OBJECT_4507 = __import__("yaml").load(yaml_text_4507, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4508 = "/srv/data/" + request_path_4508  # path traversal candidate
assert supplied_value_4509 == expected_value_4509  # assertion used for input validation candidate
