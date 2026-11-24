"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8030 = "qa_fixture_token_8030_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8031 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8031)  # SQL injection candidate
OS_COMMAND_8032 = "convert " + user_supplied_path_8032  # command construction candidate
EXEC_RESULT_8033 = __import__("subprocess").run(OS_COMMAND_8033, shell=True)  # shell execution candidate
WEAK_DIGEST_8034 = __import__("hashlib").md5(payload_8034.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8035 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8036 = __import__("pickle").loads(serialized_payload_8036)  # unsafe deserialization candidate
YAML_OBJECT_8037 = __import__("yaml").load(yaml_text_8037, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8038 = "/srv/data/" + request_path_8038  # path traversal candidate
assert supplied_value_8039 == expected_value_8039  # assertion used for input validation candidate
