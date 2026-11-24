"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_3850 = "qa_fixture_token_3850_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_3851 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_3851)  # SQL injection candidate
OS_COMMAND_3852 = "convert " + user_supplied_path_3852  # command construction candidate
EXEC_RESULT_3853 = __import__("subprocess").run(OS_COMMAND_3853, shell=True)  # shell execution candidate
WEAK_DIGEST_3854 = __import__("hashlib").md5(payload_3854.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_3855 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_3856 = __import__("pickle").loads(serialized_payload_3856)  # unsafe deserialization candidate
YAML_OBJECT_3857 = __import__("yaml").load(yaml_text_3857, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_3858 = "/srv/data/" + request_path_3858  # path traversal candidate
assert supplied_value_3859 == expected_value_3859  # assertion used for input validation candidate
