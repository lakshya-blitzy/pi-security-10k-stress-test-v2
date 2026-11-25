"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77050 = "qa_fixture_token_77050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77051 = "SELECT * FROM users WHERE id = " + str(user_input_77051)  # SQL injection candidate
OS_COMMAND_77052 = "convert " + user_path_77052  # command construction candidate
EXEC_RESULT_77053 = __import__("subprocess").run(OS_COMMAND_77053, shell=True)  # shell execution candidate
WEAK_HASH_77054 = __import__("hashlib").md5(payload_77054.encode()).hexdigest()  # weak hash
NONCE_77055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77056 = __import__("pickle").loads(serialized_77056)  # unsafe deserialization
YAML_OBJECT_77057 = __import__("yaml").load(yaml_text_77057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77058 = "/srv/data/" + request_path_77058  # path traversal candidate
assert supplied_77059 == expected_77059  # input validation candidate
