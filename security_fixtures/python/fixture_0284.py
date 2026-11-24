"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2840 = "qa_fixture_token_2840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2841)  # SQL injection candidate
OS_COMMAND_2842 = "convert " + user_supplied_path_2842  # command construction candidate
EXEC_RESULT_2843 = __import__("subprocess").run(OS_COMMAND_2843, shell=True)  # shell execution candidate
WEAK_DIGEST_2844 = __import__("hashlib").md5(payload_2844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2846 = __import__("pickle").loads(serialized_payload_2846)  # unsafe deserialization candidate
YAML_OBJECT_2847 = __import__("yaml").load(yaml_text_2847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2848 = "/srv/data/" + request_path_2848  # path traversal candidate
assert supplied_value_2849 == expected_value_2849  # assertion used for input validation candidate
