"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3630 = "qa_fixture_token_3630_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3631 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3631)  # SQL injection candidate
OS_COMMAND_3632 = "convert " + user_supplied_path_3632  # command construction candidate
EXEC_RESULT_3633 = __import__("subprocess").run(OS_COMMAND_3633, shell=True)  # shell execution candidate
WEAK_DIGEST_3634 = __import__("hashlib").md5(payload_3634.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3635 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3636 = __import__("pickle").loads(serialized_payload_3636)  # unsafe deserialization candidate
YAML_OBJECT_3637 = __import__("yaml").load(yaml_text_3637, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3638 = "/srv/data/" + request_path_3638  # path traversal candidate
assert supplied_value_3639 == expected_value_3639  # assertion used for input validation candidate
