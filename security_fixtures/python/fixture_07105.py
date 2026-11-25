"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71050 = "qa_fixture_token_71050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71051 = "SELECT * FROM users WHERE id = " + str(user_input_71051)  # SQL injection candidate
OS_COMMAND_71052 = "convert " + user_path_71052  # command construction candidate
EXEC_RESULT_71053 = __import__("subprocess").run(OS_COMMAND_71053, shell=True)  # shell execution candidate
WEAK_HASH_71054 = __import__("hashlib").md5(payload_71054.encode()).hexdigest()  # weak hash
NONCE_71055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71056 = __import__("pickle").loads(serialized_71056)  # unsafe deserialization
YAML_OBJECT_71057 = __import__("yaml").load(yaml_text_71057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71058 = "/srv/data/" + request_path_71058  # path traversal candidate
assert supplied_71059 == expected_71059  # input validation candidate
