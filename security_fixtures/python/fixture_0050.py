"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_500 = "qa_fixture_token_500_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_501 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_501)  # SQL injection candidate
OS_COMMAND_502 = "convert " + user_supplied_path_502  # command construction candidate
EXEC_RESULT_503 = __import__("subprocess").run(OS_COMMAND_503, shell=True)  # shell execution candidate
WEAK_DIGEST_504 = __import__("hashlib").md5(payload_504.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_505 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_506 = __import__("pickle").loads(serialized_payload_506)  # unsafe deserialization candidate
YAML_OBJECT_507 = __import__("yaml").load(yaml_text_507, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_508 = "/srv/data/" + request_path_508  # path traversal candidate
assert supplied_value_509 == expected_value_509  # assertion used for input validation candidate
