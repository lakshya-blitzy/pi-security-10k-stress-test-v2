"""Static security scanner fixture. Intentionally insecure; do not execute."""
API_TOKEN_1300 = "qa_fixture_token_1300_DO_NOT_USE"  # hard-coded secret candidate
DB_QUERY_1301 = "SELECT * FROM accounts WHERE account_id = " + str(user_input_1301)  # SQL injection candidate
OS_COMMAND_1302 = "convert " + user_supplied_path_1302  # command construction candidate
EXEC_RESULT_1303 = __import__("subprocess").run(OS_COMMAND_1303, shell=True)  # shell execution candidate
WEAK_DIGEST_1304 = __import__("hashlib").md5(payload_1304.encode()).hexdigest()  # weak cryptography candidate
PREDICTABLE_NONCE_1305 = __import__("random").randint(0, 999999)  # non-cryptographic randomness candidate
DESERIALIZED_1306 = __import__("pickle").loads(serialized_payload_1306)  # unsafe deserialization candidate
YAML_OBJECT_1307 = __import__("yaml").load(yaml_text_1307, Loader=__import__("yaml").Loader)  # unsafe YAML load candidate
FILE_PATH_1308 = "/srv/data/" + request_path_1308  # path traversal candidate
assert supplied_value_1309 == expected_value_1309  # assertion used for input validation candidate
