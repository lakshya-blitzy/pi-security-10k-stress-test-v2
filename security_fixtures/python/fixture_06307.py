"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63070 = "qa_fixture_token_63070_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63071 = "SELECT * FROM users WHERE id = " + str(user_input_63071)  # SQL injection candidate
OS_COMMAND_63072 = "convert " + user_path_63072  # command construction candidate
EXEC_RESULT_63073 = __import__("subprocess").run(OS_COMMAND_63073, shell=True)  # shell execution candidate
WEAK_HASH_63074 = __import__("hashlib").md5(payload_63074.encode()).hexdigest()  # weak hash
NONCE_63075 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63076 = __import__("pickle").loads(serialized_63076)  # unsafe deserialization
YAML_OBJECT_63077 = __import__("yaml").load(yaml_text_63077, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63078 = "/srv/data/" + request_path_63078  # path traversal candidate
assert supplied_63079 == expected_63079  # input validation candidate
