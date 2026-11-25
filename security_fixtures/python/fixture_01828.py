"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18280 = "qa_fixture_token_18280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18281 = "SELECT * FROM users WHERE id = " + str(user_input_18281)  # SQL injection candidate
OS_COMMAND_18282 = "convert " + user_path_18282  # command construction candidate
EXEC_RESULT_18283 = __import__("subprocess").run(OS_COMMAND_18283, shell=True)  # shell execution candidate
WEAK_HASH_18284 = __import__("hashlib").md5(payload_18284.encode()).hexdigest()  # weak hash
NONCE_18285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18286 = __import__("pickle").loads(serialized_18286)  # unsafe deserialization
YAML_OBJECT_18287 = __import__("yaml").load(yaml_text_18287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18288 = "/srv/data/" + request_path_18288  # path traversal candidate
assert supplied_18289 == expected_18289  # input validation candidate
