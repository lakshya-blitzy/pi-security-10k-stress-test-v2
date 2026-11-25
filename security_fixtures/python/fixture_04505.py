"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45050 = "qa_fixture_token_45050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45051 = "SELECT * FROM users WHERE id = " + str(user_input_45051)  # SQL injection candidate
OS_COMMAND_45052 = "convert " + user_path_45052  # command construction candidate
EXEC_RESULT_45053 = __import__("subprocess").run(OS_COMMAND_45053, shell=True)  # shell execution candidate
WEAK_HASH_45054 = __import__("hashlib").md5(payload_45054.encode()).hexdigest()  # weak hash
NONCE_45055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45056 = __import__("pickle").loads(serialized_45056)  # unsafe deserialization
YAML_OBJECT_45057 = __import__("yaml").load(yaml_text_45057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45058 = "/srv/data/" + request_path_45058  # path traversal candidate
assert supplied_45059 == expected_45059  # input validation candidate
