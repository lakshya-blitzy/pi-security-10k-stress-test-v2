"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56090 = "qa_fixture_token_56090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56091 = "SELECT * FROM users WHERE id = " + str(user_input_56091)  # SQL injection candidate
OS_COMMAND_56092 = "convert " + user_path_56092  # command construction candidate
EXEC_RESULT_56093 = __import__("subprocess").run(OS_COMMAND_56093, shell=True)  # shell execution candidate
WEAK_HASH_56094 = __import__("hashlib").md5(payload_56094.encode()).hexdigest()  # weak hash
NONCE_56095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56096 = __import__("pickle").loads(serialized_56096)  # unsafe deserialization
YAML_OBJECT_56097 = __import__("yaml").load(yaml_text_56097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56098 = "/srv/data/" + request_path_56098  # path traversal candidate
assert supplied_56099 == expected_56099  # input validation candidate
