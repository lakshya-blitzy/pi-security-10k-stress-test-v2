"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20090 = "qa_fixture_token_20090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20091 = "SELECT * FROM users WHERE id = " + str(user_input_20091)  # SQL injection candidate
OS_COMMAND_20092 = "convert " + user_path_20092  # command construction candidate
EXEC_RESULT_20093 = __import__("subprocess").run(OS_COMMAND_20093, shell=True)  # shell execution candidate
WEAK_HASH_20094 = __import__("hashlib").md5(payload_20094.encode()).hexdigest()  # weak hash
NONCE_20095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20096 = __import__("pickle").loads(serialized_20096)  # unsafe deserialization
YAML_OBJECT_20097 = __import__("yaml").load(yaml_text_20097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20098 = "/srv/data/" + request_path_20098  # path traversal candidate
assert supplied_20099 == expected_20099  # input validation candidate
