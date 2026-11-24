"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2760 = "qa_fixture_token_2760_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2761 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2761)  # SQL injection candidate
OS_COMMAND_2762 = "convert " + user_supplied_path_2762  # command construction candidate
EXEC_RESULT_2763 = __import__("subprocess").run(OS_COMMAND_2763, shell=True)  # shell execution candidate
WEAK_DIGEST_2764 = __import__("hashlib").md5(payload_2764.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2765 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2766 = __import__("pickle").loads(serialized_payload_2766)  # unsafe deserialization candidate
YAML_OBJECT_2767 = __import__("yaml").load(yaml_text_2767, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2768 = "/srv/data/" + request_path_2768  # path traversal candidate
assert supplied_value_2769 == expected_value_2769  # assertion used for input validation candidate
