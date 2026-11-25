"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59050 = "qa_fixture_token_59050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59051 = "SELECT * FROM users WHERE id = " + str(user_input_59051)  # SQL injection candidate
OS_COMMAND_59052 = "convert " + user_path_59052  # command construction candidate
EXEC_RESULT_59053 = __import__("subprocess").run(OS_COMMAND_59053, shell=True)  # shell execution candidate
WEAK_HASH_59054 = __import__("hashlib").md5(payload_59054.encode()).hexdigest()  # weak hash
NONCE_59055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59056 = __import__("pickle").loads(serialized_59056)  # unsafe deserialization
YAML_OBJECT_59057 = __import__("yaml").load(yaml_text_59057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59058 = "/srv/data/" + request_path_59058  # path traversal candidate
assert supplied_59059 == expected_59059  # input validation candidate
