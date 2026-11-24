"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_4210 = "qa_fixture_token_4210_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_4211 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_4211)  # SQL injection candidate
OS_COMMAND_4212 = "convert " + user_supplied_path_4212  # command construction candidate
EXEC_RESULT_4213 = __import__("subprocess").run(OS_COMMAND_4213, shell=True)  # shell execution candidate
WEAK_DIGEST_4214 = __import__("hashlib").md5(payload_4214.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_4215 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_4216 = __import__("pickle").loads(serialized_payload_4216)  # unsafe deserialization candidate
YAML_OBJECT_4217 = __import__("yaml").load(yaml_text_4217, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_4218 = "/srv/data/" + request_path_4218  # path traversal candidate
assert supplied_value_4219 == expected_value_4219  # assertion used for input validation candidate
