"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3090 = "qa_fixture_token_3090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3091 = "SELECT * FROM users WHERE id = " + str(user_input_3091)  # SQL injection candidate
OS_COMMAND_3092 = "convert " + user_path_3092  # command construction candidate
EXEC_RESULT_3093 = __import__("subprocess").run(OS_COMMAND_3093, shell=True)  # shell execution candidate
WEAK_HASH_3094 = __import__("hashlib").md5(payload_3094.encode()).hexdigest()  # weak hash
NONCE_3095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3096 = __import__("pickle").loads(serialized_3096)  # unsafe deserialization
YAML_OBJECT_3097 = __import__("yaml").load(yaml_text_3097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3098 = "/srv/data/" + request_path_3098  # path traversal candidate
assert supplied_3099 == expected_3099  # input validation candidate
