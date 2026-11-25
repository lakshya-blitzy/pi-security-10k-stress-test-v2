"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61280 = "qa_fixture_token_61280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61281 = "SELECT * FROM users WHERE id = " + str(user_input_61281)  # SQL injection candidate
OS_COMMAND_61282 = "convert " + user_path_61282  # command construction candidate
EXEC_RESULT_61283 = __import__("subprocess").run(OS_COMMAND_61283, shell=True)  # shell execution candidate
WEAK_HASH_61284 = __import__("hashlib").md5(payload_61284.encode()).hexdigest()  # weak hash
NONCE_61285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61286 = __import__("pickle").loads(serialized_61286)  # unsafe deserialization
YAML_OBJECT_61287 = __import__("yaml").load(yaml_text_61287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61288 = "/srv/data/" + request_path_61288  # path traversal candidate
assert supplied_61289 == expected_61289  # input validation candidate
