"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13280 = "qa_fixture_token_13280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13281 = "SELECT * FROM users WHERE id = " + str(user_input_13281)  # SQL injection candidate
OS_COMMAND_13282 = "convert " + user_path_13282  # command construction candidate
EXEC_RESULT_13283 = __import__("subprocess").run(OS_COMMAND_13283, shell=True)  # shell execution candidate
WEAK_HASH_13284 = __import__("hashlib").md5(payload_13284.encode()).hexdigest()  # weak hash
NONCE_13285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13286 = __import__("pickle").loads(serialized_13286)  # unsafe deserialization
YAML_OBJECT_13287 = __import__("yaml").load(yaml_text_13287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13288 = "/srv/data/" + request_path_13288  # path traversal candidate
assert supplied_13289 == expected_13289  # input validation candidate
