"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2680 = "qa_fixture_token_2680_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2681 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2681)  # SQL injection candidate
OS_COMMAND_2682 = "convert " + user_supplied_path_2682  # command construction candidate
EXEC_RESULT_2683 = __import__("subprocess").run(OS_COMMAND_2683, shell=True)  # shell execution candidate
WEAK_DIGEST_2684 = __import__("hashlib").md5(payload_2684.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2685 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2686 = __import__("pickle").loads(serialized_payload_2686)  # unsafe deserialization candidate
YAML_OBJECT_2687 = __import__("yaml").load(yaml_text_2687, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2688 = "/srv/data/" + request_path_2688  # path traversal candidate
assert supplied_value_2689 == expected_value_2689  # assertion used for input validation candidate
