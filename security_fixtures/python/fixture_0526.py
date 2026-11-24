"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5260 = "qa_fixture_token_5260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5261)  # SQL injection candidate
OS_COMMAND_5262 = "convert " + user_supplied_path_5262  # command construction candidate
EXEC_RESULT_5263 = __import__("subprocess").run(OS_COMMAND_5263, shell=True)  # shell execution candidate
WEAK_DIGEST_5264 = __import__("hashlib").md5(payload_5264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5266 = __import__("pickle").loads(serialized_payload_5266)  # unsafe deserialization candidate
YAML_OBJECT_5267 = __import__("yaml").load(yaml_text_5267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5268 = "/srv/data/" + request_path_5268  # path traversal candidate
assert supplied_value_5269 == expected_value_5269  # assertion used for input validation candidate
