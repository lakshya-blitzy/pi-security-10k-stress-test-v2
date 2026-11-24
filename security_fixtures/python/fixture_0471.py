"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4710 = "qa_fixture_token_4710_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4711 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4711)  # SQL injection candidate
OS_COMMAND_4712 = "convert " + user_supplied_path_4712  # command construction candidate
EXEC_RESULT_4713 = __import__("subprocess").run(OS_COMMAND_4713, shell=True)  # shell execution candidate
WEAK_DIGEST_4714 = __import__("hashlib").md5(payload_4714.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4715 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4716 = __import__("pickle").loads(serialized_payload_4716)  # unsafe deserialization candidate
YAML_OBJECT_4717 = __import__("yaml").load(yaml_text_4717, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4718 = "/srv/data/" + request_path_4718  # path traversal candidate
assert supplied_value_4719 == expected_value_4719  # assertion used for input validation candidate
