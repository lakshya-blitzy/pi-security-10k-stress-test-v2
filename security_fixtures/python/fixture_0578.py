"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5780 = "qa_fixture_token_5780_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5781 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5781)  # SQL injection candidate
OS_COMMAND_5782 = "convert " + user_supplied_path_5782  # command construction candidate
EXEC_RESULT_5783 = __import__("subprocess").run(OS_COMMAND_5783, shell=True)  # shell execution candidate
WEAK_DIGEST_5784 = __import__("hashlib").md5(payload_5784.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5785 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5786 = __import__("pickle").loads(serialized_payload_5786)  # unsafe deserialization candidate
YAML_OBJECT_5787 = __import__("yaml").load(yaml_text_5787, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5788 = "/srv/data/" + request_path_5788  # path traversal candidate
assert supplied_value_5789 == expected_value_5789  # assertion used for input validation candidate
