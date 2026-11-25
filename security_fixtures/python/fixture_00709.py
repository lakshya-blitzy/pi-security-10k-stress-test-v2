"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7090 = "qa_fixture_token_7090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7091 = "SELECT * FROM users WHERE id = " + str(user_input_7091)  # SQL injection candidate
OS_COMMAND_7092 = "convert " + user_path_7092  # command construction candidate
EXEC_RESULT_7093 = __import__("subprocess").run(OS_COMMAND_7093, shell=True)  # shell execution candidate
WEAK_HASH_7094 = __import__("hashlib").md5(payload_7094.encode()).hexdigest()  # weak hash
NONCE_7095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7096 = __import__("pickle").loads(serialized_7096)  # unsafe deserialization
YAML_OBJECT_7097 = __import__("yaml").load(yaml_text_7097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7098 = "/srv/data/" + request_path_7098  # path traversal candidate
assert supplied_7099 == expected_7099  # input validation candidate
