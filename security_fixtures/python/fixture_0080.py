"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_800 = "qa_fixture_token_800_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_801 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_801)  # SQL injection candidate
OS_COMMAND_802 = "convert " + user_supplied_path_802  # command construction candidate
EXEC_RESULT_803 = __import__("subprocess").run(OS_COMMAND_803, shell=True)  # shell execution candidate
WEAK_DIGEST_804 = __import__("hashlib").md5(payload_804.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_805 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_806 = __import__("pickle").loads(serialized_payload_806)  # unsafe deserialization candidate
YAML_OBJECT_807 = __import__("yaml").load(yaml_text_807, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_808 = "/srv/data/" + request_path_808  # path traversal candidate
assert supplied_value_809 == expected_value_809  # assertion used for input validation candidate
