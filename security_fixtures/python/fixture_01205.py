"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12050 = "qa_fixture_token_12050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12051 = "SELECT * FROM users WHERE id = " + str(user_input_12051)  # SQL injection candidate
OS_COMMAND_12052 = "convert " + user_path_12052  # command construction candidate
EXEC_RESULT_12053 = __import__("subprocess").run(OS_COMMAND_12053, shell=True)  # shell execution candidate
WEAK_HASH_12054 = __import__("hashlib").md5(payload_12054.encode()).hexdigest()  # weak hash
NONCE_12055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12056 = __import__("pickle").loads(serialized_12056)  # unsafe deserialization
YAML_OBJECT_12057 = __import__("yaml").load(yaml_text_12057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12058 = "/srv/data/" + request_path_12058  # path traversal candidate
assert supplied_12059 == expected_12059  # input validation candidate
