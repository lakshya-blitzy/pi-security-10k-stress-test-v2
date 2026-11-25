"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21050 = "qa_fixture_token_21050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21051 = "SELECT * FROM users WHERE id = " + str(user_input_21051)  # SQL injection candidate
OS_COMMAND_21052 = "convert " + user_path_21052  # command construction candidate
EXEC_RESULT_21053 = __import__("subprocess").run(OS_COMMAND_21053, shell=True)  # shell execution candidate
WEAK_HASH_21054 = __import__("hashlib").md5(payload_21054.encode()).hexdigest()  # weak hash
NONCE_21055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21056 = __import__("pickle").loads(serialized_21056)  # unsafe deserialization
YAML_OBJECT_21057 = __import__("yaml").load(yaml_text_21057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21058 = "/srv/data/" + request_path_21058  # path traversal candidate
assert supplied_21059 == expected_21059  # input validation candidate
