"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43050 = "qa_fixture_token_43050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43051 = "SELECT * FROM users WHERE id = " + str(user_input_43051)  # SQL injection candidate
OS_COMMAND_43052 = "convert " + user_path_43052  # command construction candidate
EXEC_RESULT_43053 = __import__("subprocess").run(OS_COMMAND_43053, shell=True)  # shell execution candidate
WEAK_HASH_43054 = __import__("hashlib").md5(payload_43054.encode()).hexdigest()  # weak hash
NONCE_43055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43056 = __import__("pickle").loads(serialized_43056)  # unsafe deserialization
YAML_OBJECT_43057 = __import__("yaml").load(yaml_text_43057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43058 = "/srv/data/" + request_path_43058  # path traversal candidate
assert supplied_43059 == expected_43059  # input validation candidate
