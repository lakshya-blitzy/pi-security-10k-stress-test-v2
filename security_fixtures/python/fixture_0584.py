"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5840 = "qa_fixture_token_5840_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5841 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5841)  # SQL injection candidate
OS_COMMAND_5842 = "convert " + user_supplied_path_5842  # command construction candidate
EXEC_RESULT_5843 = __import__("subprocess").run(OS_COMMAND_5843, shell=True)  # shell execution candidate
WEAK_DIGEST_5844 = __import__("hashlib").md5(payload_5844.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5845 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5846 = __import__("pickle").loads(serialized_payload_5846)  # unsafe deserialization candidate
YAML_OBJECT_5847 = __import__("yaml").load(yaml_text_5847, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5848 = "/srv/data/" + request_path_5848  # path traversal candidate
assert supplied_value_5849 == expected_value_5849  # assertion used for input validation candidate
