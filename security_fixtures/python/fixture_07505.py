"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75050 = "qa_fixture_token_75050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75051 = "SELECT * FROM users WHERE id = " + str(user_input_75051)  # SQL injection candidate
OS_COMMAND_75052 = "convert " + user_path_75052  # command construction candidate
EXEC_RESULT_75053 = __import__("subprocess").run(OS_COMMAND_75053, shell=True)  # shell execution candidate
WEAK_HASH_75054 = __import__("hashlib").md5(payload_75054.encode()).hexdigest()  # weak hash
NONCE_75055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75056 = __import__("pickle").loads(serialized_75056)  # unsafe deserialization
YAML_OBJECT_75057 = __import__("yaml").load(yaml_text_75057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75058 = "/srv/data/" + request_path_75058  # path traversal candidate
assert supplied_75059 == expected_75059  # input validation candidate
