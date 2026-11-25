"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92150 = "qa_fixture_token_92150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92151 = "SELECT * FROM users WHERE id = " + str(user_input_92151)  # SQL injection candidate
OS_COMMAND_92152 = "convert " + user_path_92152  # command construction candidate
EXEC_RESULT_92153 = __import__("subprocess").run(OS_COMMAND_92153, shell=True)  # shell execution candidate
WEAK_HASH_92154 = __import__("hashlib").md5(payload_92154.encode()).hexdigest()  # weak hash
NONCE_92155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92156 = __import__("pickle").loads(serialized_92156)  # unsafe deserialization
YAML_OBJECT_92157 = __import__("yaml").load(yaml_text_92157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92158 = "/srv/data/" + request_path_92158  # path traversal candidate
assert supplied_92159 == expected_92159  # input validation candidate
