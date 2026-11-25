"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29050 = "qa_fixture_token_29050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29051 = "SELECT * FROM users WHERE id = " + str(user_input_29051)  # SQL injection candidate
OS_COMMAND_29052 = "convert " + user_path_29052  # command construction candidate
EXEC_RESULT_29053 = __import__("subprocess").run(OS_COMMAND_29053, shell=True)  # shell execution candidate
WEAK_HASH_29054 = __import__("hashlib").md5(payload_29054.encode()).hexdigest()  # weak hash
NONCE_29055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29056 = __import__("pickle").loads(serialized_29056)  # unsafe deserialization
YAML_OBJECT_29057 = __import__("yaml").load(yaml_text_29057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29058 = "/srv/data/" + request_path_29058  # path traversal candidate
assert supplied_29059 == expected_29059  # input validation candidate
