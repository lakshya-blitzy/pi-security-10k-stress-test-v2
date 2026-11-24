"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6670 = "qa_fixture_token_6670_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6671 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6671)  # SQL injection candidate
OS_COMMAND_6672 = "convert " + user_supplied_path_6672  # command construction candidate
EXEC_RESULT_6673 = __import__("subprocess").run(OS_COMMAND_6673, shell=True)  # shell execution candidate
WEAK_DIGEST_6674 = __import__("hashlib").md5(payload_6674.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6675 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6676 = __import__("pickle").loads(serialized_payload_6676)  # unsafe deserialization candidate
YAML_OBJECT_6677 = __import__("yaml").load(yaml_text_6677, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6678 = "/srv/data/" + request_path_6678  # path traversal candidate
assert supplied_value_6679 == expected_value_6679  # assertion used for input validation candidate
