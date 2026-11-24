"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2790 = "qa_fixture_token_2790_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2791 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2791)  # SQL injection candidate
OS_COMMAND_2792 = "convert " + user_supplied_path_2792  # command construction candidate
EXEC_RESULT_2793 = __import__("subprocess").run(OS_COMMAND_2793, shell=True)  # shell execution candidate
WEAK_DIGEST_2794 = __import__("hashlib").md5(payload_2794.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2795 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2796 = __import__("pickle").loads(serialized_payload_2796)  # unsafe deserialization candidate
YAML_OBJECT_2797 = __import__("yaml").load(yaml_text_2797, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2798 = "/srv/data/" + request_path_2798  # path traversal candidate
assert supplied_value_2799 == expected_value_2799  # assertion used for input validation candidate
