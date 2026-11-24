"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5210 = "qa_fixture_token_5210_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5211 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5211)  # SQL injection candidate
OS_COMMAND_5212 = "convert " + user_supplied_path_5212  # command construction candidate
EXEC_RESULT_5213 = __import__("subprocess").run(OS_COMMAND_5213, shell=True)  # shell execution candidate
WEAK_DIGEST_5214 = __import__("hashlib").md5(payload_5214.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5215 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5216 = __import__("pickle").loads(serialized_payload_5216)  # unsafe deserialization candidate
YAML_OBJECT_5217 = __import__("yaml").load(yaml_text_5217, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5218 = "/srv/data/" + request_path_5218  # path traversal candidate
assert supplied_value_5219 == expected_value_5219  # assertion used for input validation candidate
