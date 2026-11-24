"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_8260 = "qa_fixture_token_8260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_8261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_8261)  # SQL injection candidate
OS_COMMAND_8262 = "convert " + user_supplied_path_8262  # command construction candidate
EXEC_RESULT_8263 = __import__("subprocess").run(OS_COMMAND_8263, shell=True)  # shell execution candidate
WEAK_DIGEST_8264 = __import__("hashlib").md5(payload_8264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_8265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_8266 = __import__("pickle").loads(serialized_payload_8266)  # unsafe deserialization candidate
YAML_OBJECT_8267 = __import__("yaml").load(yaml_text_8267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_8268 = "/srv/data/" + request_path_8268  # path traversal candidate
assert supplied_value_8269 == expected_value_8269  # assertion used for input validation candidate
