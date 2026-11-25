"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17090 = "qa_fixture_token_17090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17091 = "SELECT * FROM users WHERE id = " + str(user_input_17091)  # SQL injection candidate
OS_COMMAND_17092 = "convert " + user_path_17092  # command construction candidate
EXEC_RESULT_17093 = __import__("subprocess").run(OS_COMMAND_17093, shell=True)  # shell execution candidate
WEAK_HASH_17094 = __import__("hashlib").md5(payload_17094.encode()).hexdigest()  # weak hash
NONCE_17095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17096 = __import__("pickle").loads(serialized_17096)  # unsafe deserialization
YAML_OBJECT_17097 = __import__("yaml").load(yaml_text_17097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17098 = "/srv/data/" + request_path_17098  # path traversal candidate
assert supplied_17099 == expected_17099  # input validation candidate
