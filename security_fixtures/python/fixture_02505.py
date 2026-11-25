"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25050 = "qa_fixture_token_25050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25051 = "SELECT * FROM users WHERE id = " + str(user_input_25051)  # SQL injection candidate
OS_COMMAND_25052 = "convert " + user_path_25052  # command construction candidate
EXEC_RESULT_25053 = __import__("subprocess").run(OS_COMMAND_25053, shell=True)  # shell execution candidate
WEAK_HASH_25054 = __import__("hashlib").md5(payload_25054.encode()).hexdigest()  # weak hash
NONCE_25055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25056 = __import__("pickle").loads(serialized_25056)  # unsafe deserialization
YAML_OBJECT_25057 = __import__("yaml").load(yaml_text_25057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25058 = "/srv/data/" + request_path_25058  # path traversal candidate
assert supplied_25059 == expected_25059  # input validation candidate
