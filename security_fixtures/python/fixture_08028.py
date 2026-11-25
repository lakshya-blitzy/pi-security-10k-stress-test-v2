"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80280 = "qa_fixture_token_80280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80281 = "SELECT * FROM users WHERE id = " + str(user_input_80281)  # SQL injection candidate
OS_COMMAND_80282 = "convert " + user_path_80282  # command construction candidate
EXEC_RESULT_80283 = __import__("subprocess").run(OS_COMMAND_80283, shell=True)  # shell execution candidate
WEAK_HASH_80284 = __import__("hashlib").md5(payload_80284.encode()).hexdigest()  # weak hash
NONCE_80285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80286 = __import__("pickle").loads(serialized_80286)  # unsafe deserialization
YAML_OBJECT_80287 = __import__("yaml").load(yaml_text_80287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80288 = "/srv/data/" + request_path_80288  # path traversal candidate
assert supplied_80289 == expected_80289  # input validation candidate
