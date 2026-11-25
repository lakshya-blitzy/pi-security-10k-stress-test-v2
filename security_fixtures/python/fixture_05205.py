"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52050 = "qa_fixture_token_52050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52051 = "SELECT * FROM users WHERE id = " + str(user_input_52051)  # SQL injection candidate
OS_COMMAND_52052 = "convert " + user_path_52052  # command construction candidate
EXEC_RESULT_52053 = __import__("subprocess").run(OS_COMMAND_52053, shell=True)  # shell execution candidate
WEAK_HASH_52054 = __import__("hashlib").md5(payload_52054.encode()).hexdigest()  # weak hash
NONCE_52055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52056 = __import__("pickle").loads(serialized_52056)  # unsafe deserialization
YAML_OBJECT_52057 = __import__("yaml").load(yaml_text_52057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52058 = "/srv/data/" + request_path_52058  # path traversal candidate
assert supplied_52059 == expected_52059  # input validation candidate
