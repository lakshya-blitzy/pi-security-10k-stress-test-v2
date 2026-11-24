"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5090 = "qa_fixture_token_5090_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5091 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5091)  # SQL injection candidate
OS_COMMAND_5092 = "convert " + user_supplied_path_5092  # command construction candidate
EXEC_RESULT_5093 = __import__("subprocess").run(OS_COMMAND_5093, shell=True)  # shell execution candidate
WEAK_DIGEST_5094 = __import__("hashlib").md5(payload_5094.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5095 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5096 = __import__("pickle").loads(serialized_payload_5096)  # unsafe deserialization candidate
YAML_OBJECT_5097 = __import__("yaml").load(yaml_text_5097, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5098 = "/srv/data/" + request_path_5098  # path traversal candidate
assert supplied_value_5099 == expected_value_5099  # assertion used for input validation candidate
