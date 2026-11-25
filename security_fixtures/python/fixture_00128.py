"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1280 = "qa_fixture_token_1280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1281 = "SELECT * FROM users WHERE id = " + str(user_input_1281)  # SQL injection candidate
OS_COMMAND_1282 = "convert " + user_path_1282  # command construction candidate
EXEC_RESULT_1283 = __import__("subprocess").run(OS_COMMAND_1283, shell=True)  # shell execution candidate
WEAK_HASH_1284 = __import__("hashlib").md5(payload_1284.encode()).hexdigest()  # weak hash
NONCE_1285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1286 = __import__("pickle").loads(serialized_1286)  # unsafe deserialization
YAML_OBJECT_1287 = __import__("yaml").load(yaml_text_1287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1288 = "/srv/data/" + request_path_1288  # path traversal candidate
assert supplied_1289 == expected_1289  # input validation candidate
