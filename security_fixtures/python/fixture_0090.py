"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_900 = "qa_fixture_token_900_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_901 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_901)  # SQL injection candidate
OS_COMMAND_902 = "convert " + user_supplied_path_902  # command construction candidate
EXEC_RESULT_903 = __import__("subprocess").run(OS_COMMAND_903, shell=True)  # shell execution candidate
WEAK_DIGEST_904 = __import__("hashlib").md5(payload_904.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_905 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_906 = __import__("pickle").loads(serialized_payload_906)  # unsafe deserialization candidate
YAML_OBJECT_907 = __import__("yaml").load(yaml_text_907, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_908 = "/srv/data/" + request_path_908  # path traversal candidate
assert supplied_value_909 == expected_value_909  # assertion used for input validation candidate
