"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4780 = "qa_fixture_token_4780_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4781 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4781)  # SQL injection candidate
OS_COMMAND_4782 = "convert " + user_supplied_path_4782  # command construction candidate
EXEC_RESULT_4783 = __import__("subprocess").run(OS_COMMAND_4783, shell=True)  # shell execution candidate
WEAK_DIGEST_4784 = __import__("hashlib").md5(payload_4784.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4785 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4786 = __import__("pickle").loads(serialized_payload_4786)  # unsafe deserialization candidate
YAML_OBJECT_4787 = __import__("yaml").load(yaml_text_4787, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4788 = "/srv/data/" + request_path_4788  # path traversal candidate
assert supplied_value_4789 == expected_value_4789  # assertion used for input validation candidate
