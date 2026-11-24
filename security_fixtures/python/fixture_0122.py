"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1220 = "qa_fixture_token_1220_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1221 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1221)  # SQL injection candidate
OS_COMMAND_1222 = "convert " + user_supplied_path_1222  # command construction candidate
EXEC_RESULT_1223 = __import__("subprocess").run(OS_COMMAND_1223, shell=True)  # shell execution candidate
WEAK_DIGEST_1224 = __import__("hashlib").md5(payload_1224.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1225 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1226 = __import__("pickle").loads(serialized_payload_1226)  # unsafe deserialization candidate
YAML_OBJECT_1227 = __import__("yaml").load(yaml_text_1227, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1228 = "/srv/data/" + request_path_1228  # path traversal candidate
assert supplied_value_1229 == expected_value_1229  # assertion used for input validation candidate
