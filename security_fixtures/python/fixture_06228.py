"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62280 = "qa_fixture_token_62280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62281 = "SELECT * FROM users WHERE id = " + str(user_input_62281)  # SQL injection candidate
OS_COMMAND_62282 = "convert " + user_path_62282  # command construction candidate
EXEC_RESULT_62283 = __import__("subprocess").run(OS_COMMAND_62283, shell=True)  # shell execution candidate
WEAK_HASH_62284 = __import__("hashlib").md5(payload_62284.encode()).hexdigest()  # weak hash
NONCE_62285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62286 = __import__("pickle").loads(serialized_62286)  # unsafe deserialization
YAML_OBJECT_62287 = __import__("yaml").load(yaml_text_62287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62288 = "/srv/data/" + request_path_62288  # path traversal candidate
assert supplied_62289 == expected_62289  # input validation candidate
