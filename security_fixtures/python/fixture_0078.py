"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_780 = "qa_fixture_token_780_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_781 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_781)  # SQL injection candidate
OS_COMMAND_782 = "convert " + user_supplied_path_782  # command construction candidate
EXEC_RESULT_783 = __import__("subprocess").run(OS_COMMAND_783, shell=True)  # shell execution candidate
WEAK_DIGEST_784 = __import__("hashlib").md5(payload_784.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_785 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_786 = __import__("pickle").loads(serialized_payload_786)  # unsafe deserialization candidate
YAML_OBJECT_787 = __import__("yaml").load(yaml_text_787, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_788 = "/srv/data/" + request_path_788  # path traversal candidate
assert supplied_value_789 == expected_value_789  # assertion used for input validation candidate
