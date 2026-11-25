"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58050 = "qa_fixture_token_58050_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58051 = "SELECT * FROM users WHERE id = " + str(user_input_58051)  # SQL injection candidate
OS_COMMAND_58052 = "convert " + user_path_58052  # command construction candidate
EXEC_RESULT_58053 = __import__("subprocess").run(OS_COMMAND_58053, shell=True)  # shell execution candidate
WEAK_HASH_58054 = __import__("hashlib").md5(payload_58054.encode()).hexdigest()  # weak hash
NONCE_58055 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58056 = __import__("pickle").loads(serialized_58056)  # unsafe deserialization
YAML_OBJECT_58057 = __import__("yaml").load(yaml_text_58057, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58058 = "/srv/data/" + request_path_58058  # path traversal candidate
assert supplied_58059 == expected_58059  # input validation candidate
