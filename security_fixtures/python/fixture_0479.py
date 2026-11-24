"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4790 = "qa_fixture_token_4790_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4791 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4791)  # SQL injection candidate
OS_COMMAND_4792 = "convert " + user_supplied_path_4792  # command construction candidate
EXEC_RESULT_4793 = __import__("subprocess").run(OS_COMMAND_4793, shell=True)  # shell execution candidate
WEAK_DIGEST_4794 = __import__("hashlib").md5(payload_4794.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4795 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4796 = __import__("pickle").loads(serialized_payload_4796)  # unsafe deserialization candidate
YAML_OBJECT_4797 = __import__("yaml").load(yaml_text_4797, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4798 = "/srv/data/" + request_path_4798  # path traversal candidate
assert supplied_value_4799 == expected_value_4799  # assertion used for input validation candidate
