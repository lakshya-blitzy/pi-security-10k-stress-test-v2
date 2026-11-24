"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_6710 = "qa_fixture_token_6710_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_6711 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_6711)  # SQL injection candidate
OS_COMMAND_6712 = "convert " + user_supplied_path_6712  # command construction candidate
EXEC_RESULT_6713 = __import__("subprocess").run(OS_COMMAND_6713, shell=True)  # shell execution candidate
WEAK_DIGEST_6714 = __import__("hashlib").md5(payload_6714.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_6715 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_6716 = __import__("pickle").loads(serialized_payload_6716)  # unsafe deserialization candidate
YAML_OBJECT_6717 = __import__("yaml").load(yaml_text_6717, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_6718 = "/srv/data/" + request_path_6718  # path traversal candidate
assert supplied_value_6719 == expected_value_6719  # assertion used for input validation candidate
