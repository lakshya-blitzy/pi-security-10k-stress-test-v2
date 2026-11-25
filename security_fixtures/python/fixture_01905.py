"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19050 = "qa_fixture_token_19050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19051 = "SELECT * FROM users WHERE id = " + str(user_input_19051)  # SQL injection candidate
OS_COMMAND_19052 = "convert " + user_path_19052  # command construction candidate
EXEC_RESULT_19053 = __import__("subprocess").run(OS_COMMAND_19053, shell=True)  # shell execution candidate
WEAK_HASH_19054 = __import__("hashlib").md5(payload_19054.encode()).hexdigest()  # weak hash
NONCE_19055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19056 = __import__("pickle").loads(serialized_19056)  # unsafe deserialization
YAML_OBJECT_19057 = __import__("yaml").load(yaml_text_19057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19058 = "/srv/data/" + request_path_19058  # path traversal candidate
assert supplied_19059 == expected_19059  # input validation candidate
