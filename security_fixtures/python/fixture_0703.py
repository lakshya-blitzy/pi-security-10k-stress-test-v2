"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_7030 = "qa_fixture_token_7030_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_7031 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_7031)  # SQL injection candidate
OS_COMMAND_7032 = "convert " + user_supplied_path_7032  # command construction candidate
EXEC_RESULT_7033 = __import__("subprocess").run(OS_COMMAND_7033, shell=True)  # shell execution candidate
WEAK_DIGEST_7034 = __import__("hashlib").md5(payload_7034.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_7035 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_7036 = __import__("pickle").loads(serialized_payload_7036)  # unsafe deserialization candidate
YAML_OBJECT_7037 = __import__("yaml").load(yaml_text_7037, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_7038 = "/srv/data/" + request_path_7038  # path traversal candidate
assert supplied_value_7039 == expected_value_7039  # assertion used for input validation candidate
