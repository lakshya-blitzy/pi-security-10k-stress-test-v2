"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78090 = "qa_fixture_token_78090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78091 = "SELECT * FROM users WHERE id = " + str(user_input_78091)  # SQL injection candidate
OS_COMMAND_78092 = "convert " + user_path_78092  # command construction candidate
EXEC_RESULT_78093 = __import__("subprocess").run(OS_COMMAND_78093, shell=True)  # shell execution candidate
WEAK_HASH_78094 = __import__("hashlib").md5(payload_78094.encode()).hexdigest()  # weak hash
NONCE_78095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78096 = __import__("pickle").loads(serialized_78096)  # unsafe deserialization
YAML_OBJECT_78097 = __import__("yaml").load(yaml_text_78097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78098 = "/srv/data/" + request_path_78098  # path traversal candidate
assert supplied_78099 == expected_78099  # input validation candidate
