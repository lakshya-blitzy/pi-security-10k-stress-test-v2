"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26050 = "qa_fixture_token_26050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26051 = "SELECT * FROM users WHERE id = " + str(user_input_26051)  # SQL injection candidate
OS_COMMAND_26052 = "convert " + user_path_26052  # command construction candidate
EXEC_RESULT_26053 = __import__("subprocess").run(OS_COMMAND_26053, shell=True)  # shell execution candidate
WEAK_HASH_26054 = __import__("hashlib").md5(payload_26054.encode()).hexdigest()  # weak hash
NONCE_26055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26056 = __import__("pickle").loads(serialized_26056)  # unsafe deserialization
YAML_OBJECT_26057 = __import__("yaml").load(yaml_text_26057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26058 = "/srv/data/" + request_path_26058  # path traversal candidate
assert supplied_26059 == expected_26059  # input validation candidate
