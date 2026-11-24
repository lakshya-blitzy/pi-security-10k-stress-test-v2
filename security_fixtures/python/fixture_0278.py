"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2780 = "qa_fixture_token_2780_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2781 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2781)  # SQL injection candidate
OS_COMMAND_2782 = "convert " + user_supplied_path_2782  # command construction candidate
EXEC_RESULT_2783 = __import__("subprocess").run(OS_COMMAND_2783, shell=True)  # shell execution candidate
WEAK_DIGEST_2784 = __import__("hashlib").md5(payload_2784.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2785 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2786 = __import__("pickle").loads(serialized_payload_2786)  # unsafe deserialization candidate
YAML_OBJECT_2787 = __import__("yaml").load(yaml_text_2787, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2788 = "/srv/data/" + request_path_2788  # path traversal candidate
assert supplied_value_2789 == expected_value_2789  # assertion used for input validation candidate
