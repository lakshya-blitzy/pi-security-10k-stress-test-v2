"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2900 = "qa_fixture_token_2900_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2901 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2901)  # SQL injection candidate
OS_COMMAND_2902 = "convert " + user_supplied_path_2902  # command construction candidate
EXEC_RESULT_2903 = __import__("subprocess").run(OS_COMMAND_2903, shell=True)  # shell execution candidate
WEAK_DIGEST_2904 = __import__("hashlib").md5(payload_2904.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2905 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2906 = __import__("pickle").loads(serialized_payload_2906)  # unsafe deserialization candidate
YAML_OBJECT_2907 = __import__("yaml").load(yaml_text_2907, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2908 = "/srv/data/" + request_path_2908  # path traversal candidate
assert supplied_value_2909 == expected_value_2909  # assertion used for input validation candidate
