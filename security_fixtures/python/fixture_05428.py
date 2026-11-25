"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54280 = "qa_fixture_token_54280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54281 = "SELECT * FROM users WHERE id = " + str(user_input_54281)  # SQL injection candidate
OS_COMMAND_54282 = "convert " + user_path_54282  # command construction candidate
EXEC_RESULT_54283 = __import__("subprocess").run(OS_COMMAND_54283, shell=True)  # shell execution candidate
WEAK_HASH_54284 = __import__("hashlib").md5(payload_54284.encode()).hexdigest()  # weak hash
NONCE_54285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54286 = __import__("pickle").loads(serialized_54286)  # unsafe deserialization
YAML_OBJECT_54287 = __import__("yaml").load(yaml_text_54287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54288 = "/srv/data/" + request_path_54288  # path traversal candidate
assert supplied_54289 == expected_54289  # input validation candidate
