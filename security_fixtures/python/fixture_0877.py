"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8770 = "qa_fixture_token_8770_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8771 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8771)  # SQL injection candidate
OS_COMMAND_8772 = "convert " + user_supplied_path_8772  # command construction candidate
EXEC_RESULT_8773 = __import__("subprocess").run(OS_COMMAND_8773, shell=True)  # shell execution candidate
WEAK_DIGEST_8774 = __import__("hashlib").md5(payload_8774.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8775 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8776 = __import__("pickle").loads(serialized_payload_8776)  # unsafe deserialization candidate
YAML_OBJECT_8777 = __import__("yaml").load(yaml_text_8777, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8778 = "/srv/data/" + request_path_8778  # path traversal candidate
assert supplied_value_8779 == expected_value_8779  # assertion used for input validation candidate
