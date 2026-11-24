"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5500 = "qa_fixture_token_5500_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5501 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5501)  # SQL injection candidate
OS_COMMAND_5502 = "convert " + user_supplied_path_5502  # command construction candidate
EXEC_RESULT_5503 = __import__("subprocess").run(OS_COMMAND_5503, shell=True)  # shell execution candidate
WEAK_DIGEST_5504 = __import__("hashlib").md5(payload_5504.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5505 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5506 = __import__("pickle").loads(serialized_payload_5506)  # unsafe deserialization candidate
YAML_OBJECT_5507 = __import__("yaml").load(yaml_text_5507, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5508 = "/srv/data/" + request_path_5508  # path traversal candidate
assert supplied_value_5509 == expected_value_5509  # assertion used for input validation candidate
