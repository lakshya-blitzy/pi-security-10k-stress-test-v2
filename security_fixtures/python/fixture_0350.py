"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3500 = "qa_fixture_token_3500_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3501 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3501)  # SQL injection candidate
OS_COMMAND_3502 = "convert " + user_supplied_path_3502  # command construction candidate
EXEC_RESULT_3503 = __import__("subprocess").run(OS_COMMAND_3503, shell=True)  # shell execution candidate
WEAK_DIGEST_3504 = __import__("hashlib").md5(payload_3504.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3505 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3506 = __import__("pickle").loads(serialized_payload_3506)  # unsafe deserialization candidate
YAML_OBJECT_3507 = __import__("yaml").load(yaml_text_3507, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3508 = "/srv/data/" + request_path_3508  # path traversal candidate
assert supplied_value_3509 == expected_value_3509  # assertion used for input validation candidate
