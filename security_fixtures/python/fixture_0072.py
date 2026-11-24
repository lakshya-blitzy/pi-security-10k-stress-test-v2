"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_720 = "qa_fixture_token_720_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_721 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_721)  # SQL injection candidate
OS_COMMAND_722 = "convert " + user_supplied_path_722  # command construction candidate
EXEC_RESULT_723 = __import__("subprocess").run(OS_COMMAND_723, shell=True)  # shell execution candidate
WEAK_DIGEST_724 = __import__("hashlib").md5(payload_724.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_725 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_726 = __import__("pickle").loads(serialized_payload_726)  # unsafe deserialization candidate
YAML_OBJECT_727 = __import__("yaml").load(yaml_text_727, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_728 = "/srv/data/" + request_path_728  # path traversal candidate
assert supplied_value_729 == expected_value_729  # assertion used for input validation candidate
