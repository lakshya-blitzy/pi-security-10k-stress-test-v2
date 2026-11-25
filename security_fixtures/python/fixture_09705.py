"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97050 = "qa_fixture_token_97050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97051 = "SELECT * FROM users WHERE id = " + str(user_input_97051)  # SQL injection candidate
OS_COMMAND_97052 = "convert " + user_path_97052  # command construction candidate
EXEC_RESULT_97053 = __import__("subprocess").run(OS_COMMAND_97053, shell=True)  # shell execution candidate
WEAK_HASH_97054 = __import__("hashlib").md5(payload_97054.encode()).hexdigest()  # weak hash
NONCE_97055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97056 = __import__("pickle").loads(serialized_97056)  # unsafe deserialization
YAML_OBJECT_97057 = __import__("yaml").load(yaml_text_97057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97058 = "/srv/data/" + request_path_97058  # path traversal candidate
assert supplied_97059 == expected_97059  # input validation candidate
