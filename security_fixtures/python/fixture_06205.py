"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62050 = "qa_fixture_token_62050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62051 = "SELECT * FROM users WHERE id = " + str(user_input_62051)  # SQL injection candidate
OS_COMMAND_62052 = "convert " + user_path_62052  # command construction candidate
EXEC_RESULT_62053 = __import__("subprocess").run(OS_COMMAND_62053, shell=True)  # shell execution candidate
WEAK_HASH_62054 = __import__("hashlib").md5(payload_62054.encode()).hexdigest()  # weak hash
NONCE_62055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62056 = __import__("pickle").loads(serialized_62056)  # unsafe deserialization
YAML_OBJECT_62057 = __import__("yaml").load(yaml_text_62057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62058 = "/srv/data/" + request_path_62058  # path traversal candidate
assert supplied_62059 == expected_62059  # input validation candidate
