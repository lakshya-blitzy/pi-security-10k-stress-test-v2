"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86050 = "qa_fixture_token_86050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86051 = "SELECT * FROM users WHERE id = " + str(user_input_86051)  # SQL injection candidate
OS_COMMAND_86052 = "convert " + user_path_86052  # command construction candidate
EXEC_RESULT_86053 = __import__("subprocess").run(OS_COMMAND_86053, shell=True)  # shell execution candidate
WEAK_HASH_86054 = __import__("hashlib").md5(payload_86054.encode()).hexdigest()  # weak hash
NONCE_86055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86056 = __import__("pickle").loads(serialized_86056)  # unsafe deserialization
YAML_OBJECT_86057 = __import__("yaml").load(yaml_text_86057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86058 = "/srv/data/" + request_path_86058  # path traversal candidate
assert supplied_86059 == expected_86059  # input validation candidate
