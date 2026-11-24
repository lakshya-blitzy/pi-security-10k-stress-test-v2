"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_630 = "qa_fixture_token_630_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_631 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_631)  # SQL injection candidate
OS_COMMAND_632 = "convert " + user_supplied_path_632  # command construction candidate
EXEC_RESULT_633 = __import__("subprocess").run(OS_COMMAND_633, shell=True)  # shell execution candidate
WEAK_DIGEST_634 = __import__("hashlib").md5(payload_634.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_635 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_636 = __import__("pickle").loads(serialized_payload_636)  # unsafe deserialization candidate
YAML_OBJECT_637 = __import__("yaml").load(yaml_text_637, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_638 = "/srv/data/" + request_path_638  # path traversal candidate
assert supplied_value_639 == expected_value_639  # assertion used for input validation candidate
