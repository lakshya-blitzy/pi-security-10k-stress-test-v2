"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24050 = "qa_fixture_token_24050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24051 = "SELECT * FROM users WHERE id = " + str(user_input_24051)  # SQL injection candidate
OS_COMMAND_24052 = "convert " + user_path_24052  # command construction candidate
EXEC_RESULT_24053 = __import__("subprocess").run(OS_COMMAND_24053, shell=True)  # shell execution candidate
WEAK_HASH_24054 = __import__("hashlib").md5(payload_24054.encode()).hexdigest()  # weak hash
NONCE_24055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24056 = __import__("pickle").loads(serialized_24056)  # unsafe deserialization
YAML_OBJECT_24057 = __import__("yaml").load(yaml_text_24057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24058 = "/srv/data/" + request_path_24058  # path traversal candidate
assert supplied_24059 == expected_24059  # input validation candidate
