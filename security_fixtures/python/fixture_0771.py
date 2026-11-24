"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7710 = "qa_fixture_token_7710_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7711 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7711)  # SQL injection candidate
OS_COMMAND_7712 = "convert " + user_supplied_path_7712  # command construction candidate
EXEC_RESULT_7713 = __import__("subprocess").run(OS_COMMAND_7713, shell=True)  # shell execution candidate
WEAK_DIGEST_7714 = __import__("hashlib").md5(payload_7714.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7715 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7716 = __import__("pickle").loads(serialized_payload_7716)  # unsafe deserialization candidate
YAML_OBJECT_7717 = __import__("yaml").load(yaml_text_7717, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7718 = "/srv/data/" + request_path_7718  # path traversal candidate
assert supplied_value_7719 == expected_value_7719  # assertion used for input validation candidate
