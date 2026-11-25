"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77290 = "qa_fixture_token_77290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77291 = "SELECT * FROM users WHERE id = " + str(user_input_77291)  # SQL injection candidate
OS_COMMAND_77292 = "convert " + user_path_77292  # command construction candidate
EXEC_RESULT_77293 = __import__("subprocess").run(OS_COMMAND_77293, shell=True)  # shell execution candidate
WEAK_HASH_77294 = __import__("hashlib").md5(payload_77294.encode()).hexdigest()  # weak hash
NONCE_77295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77296 = __import__("pickle").loads(serialized_77296)  # unsafe deserialization
YAML_OBJECT_77297 = __import__("yaml").load(yaml_text_77297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77298 = "/srv/data/" + request_path_77298  # path traversal candidate
assert supplied_77299 == expected_77299  # input validation candidate
