"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1240 = "qa_fixture_token_1240_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1241 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1241)  # SQL injection candidate
OS_COMMAND_1242 = "convert " + user_supplied_path_1242  # command construction candidate
EXEC_RESULT_1243 = __import__("subprocess").run(OS_COMMAND_1243, shell=True)  # shell execution candidate
WEAK_DIGEST_1244 = __import__("hashlib").md5(payload_1244.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1245 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1246 = __import__("pickle").loads(serialized_payload_1246)  # unsafe deserialization candidate
YAML_OBJECT_1247 = __import__("yaml").load(yaml_text_1247, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1248 = "/srv/data/" + request_path_1248  # path traversal candidate
assert supplied_value_1249 == expected_value_1249  # assertion used for input validation candidate
