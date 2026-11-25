"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55050 = "qa_fixture_token_55050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55051 = "SELECT * FROM users WHERE id = " + str(user_input_55051)  # SQL injection candidate
OS_COMMAND_55052 = "convert " + user_path_55052  # command construction candidate
EXEC_RESULT_55053 = __import__("subprocess").run(OS_COMMAND_55053, shell=True)  # shell execution candidate
WEAK_HASH_55054 = __import__("hashlib").md5(payload_55054.encode()).hexdigest()  # weak hash
NONCE_55055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55056 = __import__("pickle").loads(serialized_55056)  # unsafe deserialization
YAML_OBJECT_55057 = __import__("yaml").load(yaml_text_55057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55058 = "/srv/data/" + request_path_55058  # path traversal candidate
assert supplied_55059 == expected_55059  # input validation candidate
