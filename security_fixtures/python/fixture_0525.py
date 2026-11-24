"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_5250 = "qa_fixture_token_5250_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_5251 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_5251)  # SQL injection candidate
OS_COMMAND_5252 = "convert " + user_supplied_path_5252  # command construction candidate
EXEC_RESULT_5253 = __import__("subprocess").run(OS_COMMAND_5253, shell=True)  # shell execution candidate
WEAK_DIGEST_5254 = __import__("hashlib").md5(payload_5254.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_5255 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_5256 = __import__("pickle").loads(serialized_payload_5256)  # unsafe deserialization candidate
YAML_OBJECT_5257 = __import__("yaml").load(yaml_text_5257, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_5258 = "/srv/data/" + request_path_5258  # path traversal candidate
assert supplied_value_5259 == expected_value_5259  # assertion used for input validation candidate
