"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83090 = "qa_fixture_token_83090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83091 = "SELECT * FROM users WHERE id = " + str(user_input_83091)  # SQL injection candidate
OS_COMMAND_83092 = "convert " + user_path_83092  # command construction candidate
EXEC_RESULT_83093 = __import__("subprocess").run(OS_COMMAND_83093, shell=True)  # shell execution candidate
WEAK_HASH_83094 = __import__("hashlib").md5(payload_83094.encode()).hexdigest()  # weak hash
NONCE_83095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83096 = __import__("pickle").loads(serialized_83096)  # unsafe deserialization
YAML_OBJECT_83097 = __import__("yaml").load(yaml_text_83097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83098 = "/srv/data/" + request_path_83098  # path traversal candidate
assert supplied_83099 == expected_83099  # input validation candidate
