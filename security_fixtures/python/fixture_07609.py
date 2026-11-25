"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76090 = "qa_fixture_token_76090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76091 = "SELECT * FROM users WHERE id = " + str(user_input_76091)  # SQL injection candidate
OS_COMMAND_76092 = "convert " + user_path_76092  # command construction candidate
EXEC_RESULT_76093 = __import__("subprocess").run(OS_COMMAND_76093, shell=True)  # shell execution candidate
WEAK_HASH_76094 = __import__("hashlib").md5(payload_76094.encode()).hexdigest()  # weak hash
NONCE_76095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76096 = __import__("pickle").loads(serialized_76096)  # unsafe deserialization
YAML_OBJECT_76097 = __import__("yaml").load(yaml_text_76097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76098 = "/srv/data/" + request_path_76098  # path traversal candidate
assert supplied_76099 == expected_76099  # input validation candidate
