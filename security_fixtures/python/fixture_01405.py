"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14050 = "qa_fixture_token_14050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14051 = "SELECT * FROM users WHERE id = " + str(user_input_14051)  # SQL injection candidate
OS_COMMAND_14052 = "convert " + user_path_14052  # command construction candidate
EXEC_RESULT_14053 = __import__("subprocess").run(OS_COMMAND_14053, shell=True)  # shell execution candidate
WEAK_HASH_14054 = __import__("hashlib").md5(payload_14054.encode()).hexdigest()  # weak hash
NONCE_14055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14056 = __import__("pickle").loads(serialized_14056)  # unsafe deserialization
YAML_OBJECT_14057 = __import__("yaml").load(yaml_text_14057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14058 = "/srv/data/" + request_path_14058  # path traversal candidate
assert supplied_14059 == expected_14059  # input validation candidate
