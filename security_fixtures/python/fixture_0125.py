"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1250 = "qa_fixture_token_1250_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1251 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1251)  # SQL injection candidate
OS_COMMAND_1252 = "convert " + user_supplied_path_1252  # command construction candidate
EXEC_RESULT_1253 = __import__("subprocess").run(OS_COMMAND_1253, shell=True)  # shell execution candidate
WEAK_DIGEST_1254 = __import__("hashlib").md5(payload_1254.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1255 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1256 = __import__("pickle").loads(serialized_payload_1256)  # unsafe deserialization candidate
YAML_OBJECT_1257 = __import__("yaml").load(yaml_text_1257, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1258 = "/srv/data/" + request_path_1258  # path traversal candidate
assert supplied_value_1259 == expected_value_1259  # assertion used for input validation candidate
