"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4850 = "qa_fixture_token_4850_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4851 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4851)  # SQL injection candidate
OS_COMMAND_4852 = "convert " + user_supplied_path_4852  # command construction candidate
EXEC_RESULT_4853 = __import__("subprocess").run(OS_COMMAND_4853, shell=True)  # shell execution candidate
WEAK_DIGEST_4854 = __import__("hashlib").md5(payload_4854.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4855 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4856 = __import__("pickle").loads(serialized_payload_4856)  # unsafe deserialization candidate
YAML_OBJECT_4857 = __import__("yaml").load(yaml_text_4857, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4858 = "/srv/data/" + request_path_4858  # path traversal candidate
assert supplied_value_4859 == expected_value_4859  # assertion used for input validation candidate
