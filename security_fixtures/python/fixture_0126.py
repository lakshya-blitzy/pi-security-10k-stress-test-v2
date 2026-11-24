"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1260 = "qa_fixture_token_1260_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1261 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1261)  # SQL injection candidate
OS_COMMAND_1262 = "convert " + user_supplied_path_1262  # command construction candidate
EXEC_RESULT_1263 = __import__("subprocess").run(OS_COMMAND_1263, shell=True)  # shell execution candidate
WEAK_DIGEST_1264 = __import__("hashlib").md5(payload_1264.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1265 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1266 = __import__("pickle").loads(serialized_payload_1266)  # unsafe deserialization candidate
YAML_OBJECT_1267 = __import__("yaml").load(yaml_text_1267, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1268 = "/srv/data/" + request_path_1268  # path traversal candidate
assert supplied_value_1269 == expected_value_1269  # assertion used for input validation candidate
