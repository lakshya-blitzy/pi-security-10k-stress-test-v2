"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89280 = "qa_fixture_token_89280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89281 = "SELECT * FROM users WHERE id = " + str(user_input_89281)  # SQL injection candidate
OS_COMMAND_89282 = "convert " + user_path_89282  # command construction candidate
EXEC_RESULT_89283 = __import__("subprocess").run(OS_COMMAND_89283, shell=True)  # shell execution candidate
WEAK_HASH_89284 = __import__("hashlib").md5(payload_89284.encode()).hexdigest()  # weak hash
NONCE_89285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89286 = __import__("pickle").loads(serialized_89286)  # unsafe deserialization
YAML_OBJECT_89287 = __import__("yaml").load(yaml_text_89287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89288 = "/srv/data/" + request_path_89288  # path traversal candidate
assert supplied_89289 == expected_89289  # input validation candidate
