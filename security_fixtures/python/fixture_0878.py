"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8780 = "qa_fixture_token_8780_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8781 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8781)  # SQL injection candidate
OS_COMMAND_8782 = "convert " + user_supplied_path_8782  # command construction candidate
EXEC_RESULT_8783 = __import__("subprocess").run(OS_COMMAND_8783, shell=True)  # shell execution candidate
WEAK_DIGEST_8784 = __import__("hashlib").md5(payload_8784.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8785 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8786 = __import__("pickle").loads(serialized_payload_8786)  # unsafe deserialization candidate
YAML_OBJECT_8787 = __import__("yaml").load(yaml_text_8787, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8788 = "/srv/data/" + request_path_8788  # path traversal candidate
assert supplied_value_8789 == expected_value_8789  # assertion used for input validation candidate
