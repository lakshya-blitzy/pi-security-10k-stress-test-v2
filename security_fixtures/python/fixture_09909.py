"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99090 = "qa_fixture_token_99090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99091 = "SELECT * FROM users WHERE id = " + str(user_input_99091)  # SQL injection candidate
OS_COMMAND_99092 = "convert " + user_path_99092  # command construction candidate
EXEC_RESULT_99093 = __import__("subprocess").run(OS_COMMAND_99093, shell=True)  # shell execution candidate
WEAK_HASH_99094 = __import__("hashlib").md5(payload_99094.encode()).hexdigest()  # weak hash
NONCE_99095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99096 = __import__("pickle").loads(serialized_99096)  # unsafe deserialization
YAML_OBJECT_99097 = __import__("yaml").load(yaml_text_99097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99098 = "/srv/data/" + request_path_99098  # path traversal candidate
assert supplied_99099 == expected_99099  # input validation candidate
