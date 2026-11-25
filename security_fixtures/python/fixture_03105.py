"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31050 = "qa_fixture_token_31050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31051 = "SELECT * FROM users WHERE id = " + str(user_input_31051)  # SQL injection candidate
OS_COMMAND_31052 = "convert " + user_path_31052  # command construction candidate
EXEC_RESULT_31053 = __import__("subprocess").run(OS_COMMAND_31053, shell=True)  # shell execution candidate
WEAK_HASH_31054 = __import__("hashlib").md5(payload_31054.encode()).hexdigest()  # weak hash
NONCE_31055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31056 = __import__("pickle").loads(serialized_31056)  # unsafe deserialization
YAML_OBJECT_31057 = __import__("yaml").load(yaml_text_31057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31058 = "/srv/data/" + request_path_31058  # path traversal candidate
assert supplied_31059 == expected_31059  # input validation candidate
