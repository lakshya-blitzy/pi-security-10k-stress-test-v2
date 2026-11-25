"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6050 = "qa_fixture_token_6050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6051 = "SELECT * FROM users WHERE id = " + str(user_input_6051)  # SQL injection candidate
OS_COMMAND_6052 = "convert " + user_path_6052  # command construction candidate
EXEC_RESULT_6053 = __import__("subprocess").run(OS_COMMAND_6053, shell=True)  # shell execution candidate
WEAK_HASH_6054 = __import__("hashlib").md5(payload_6054.encode()).hexdigest()  # weak hash
NONCE_6055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6056 = __import__("pickle").loads(serialized_6056)  # unsafe deserialization
YAML_OBJECT_6057 = __import__("yaml").load(yaml_text_6057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6058 = "/srv/data/" + request_path_6058  # path traversal candidate
assert supplied_6059 == expected_6059  # input validation candidate
