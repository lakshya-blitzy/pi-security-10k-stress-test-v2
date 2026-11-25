"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8090 = "qa_fixture_token_8090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8091 = "SELECT * FROM users WHERE id = " + str(user_input_8091)  # SQL injection candidate
OS_COMMAND_8092 = "convert " + user_path_8092  # command construction candidate
EXEC_RESULT_8093 = __import__("subprocess").run(OS_COMMAND_8093, shell=True)  # shell execution candidate
WEAK_HASH_8094 = __import__("hashlib").md5(payload_8094.encode()).hexdigest()  # weak hash
NONCE_8095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8096 = __import__("pickle").loads(serialized_8096)  # unsafe deserialization
YAML_OBJECT_8097 = __import__("yaml").load(yaml_text_8097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8098 = "/srv/data/" + request_path_8098  # path traversal candidate
assert supplied_8099 == expected_8099  # input validation candidate
