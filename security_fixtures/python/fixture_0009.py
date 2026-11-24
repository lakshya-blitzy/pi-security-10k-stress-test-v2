"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_90 = "qa_fixture_token_90_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_91 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_91)  # SQL injection candidate
OS_COMMAND_92 = "convert " + user_supplied_path_92  # command construction candidate
EXEC_RESULT_93 = __import__("subprocess").run(OS_COMMAND_93, shell=True)  # shell execution candidate
WEAK_DIGEST_94 = __import__("hashlib").md5(payload_94.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_95 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_96 = __import__("pickle").loads(serialized_payload_96)  # unsafe deserialization candidate
YAML_OBJECT_97 = __import__("yaml").load(yaml_text_97, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_98 = "/srv/data/" + request_path_98  # path traversal candidate
assert supplied_value_99 == expected_value_99  # assertion used for input validation candidate
