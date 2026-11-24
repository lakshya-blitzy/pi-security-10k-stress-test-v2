"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6900 = "qa_fixture_token_6900_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6901 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6901)  # SQL injection candidate
OS_COMMAND_6902 = "convert " + user_supplied_path_6902  # command construction candidate
EXEC_RESULT_6903 = __import__("subprocess").run(OS_COMMAND_6903, shell=True)  # shell execution candidate
WEAK_DIGEST_6904 = __import__("hashlib").md5(payload_6904.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6905 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6906 = __import__("pickle").loads(serialized_payload_6906)  # unsafe deserialization candidate
YAML_OBJECT_6907 = __import__("yaml").load(yaml_text_6907, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6908 = "/srv/data/" + request_path_6908  # path traversal candidate
assert supplied_value_6909 == expected_value_6909  # assertion used for input validation candidate
