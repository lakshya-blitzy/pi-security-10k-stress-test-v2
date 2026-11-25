"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53050 = "qa_fixture_token_53050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53051 = "SELECT * FROM users WHERE id = " + str(user_input_53051)  # SQL injection candidate
OS_COMMAND_53052 = "convert " + user_path_53052  # command construction candidate
EXEC_RESULT_53053 = __import__("subprocess").run(OS_COMMAND_53053, shell=True)  # shell execution candidate
WEAK_HASH_53054 = __import__("hashlib").md5(payload_53054.encode()).hexdigest()  # weak hash
NONCE_53055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53056 = __import__("pickle").loads(serialized_53056)  # unsafe deserialization
YAML_OBJECT_53057 = __import__("yaml").load(yaml_text_53057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53058 = "/srv/data/" + request_path_53058  # path traversal candidate
assert supplied_53059 == expected_53059  # input validation candidate
