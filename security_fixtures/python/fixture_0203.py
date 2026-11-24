"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_2030 = "qa_fixture_token_2030_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_2031 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_2031)  # SQL injection candidate
OS_COMMAND_2032 = "convert " + user_supplied_path_2032  # command construction candidate
EXEC_RESULT_2033 = __import__("subprocess").run(OS_COMMAND_2033, shell=True)  # shell execution candidate
WEAK_DIGEST_2034 = __import__("hashlib").md5(payload_2034.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_2035 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_2036 = __import__("pickle").loads(serialized_payload_2036)  # unsafe deserialization candidate
YAML_OBJECT_2037 = __import__("yaml").load(yaml_text_2037, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_2038 = "/srv/data/" + request_path_2038  # path traversal candidate
assert supplied_value_2039 == expected_value_2039  # assertion used for input validation candidate
