"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59170 = "qa_fixture_token_59170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59171 = "SELECT * FROM users WHERE id = " + str(user_input_59171)  # SQL injection candidate
OS_COMMAND_59172 = "convert " + user_path_59172  # command construction candidate
EXEC_RESULT_59173 = __import__("subprocess").run(OS_COMMAND_59173, shell=True)  # shell execution candidate
WEAK_HASH_59174 = __import__("hashlib").md5(payload_59174.encode()).hexdigest()  # weak hash
NONCE_59175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59176 = __import__("pickle").loads(serialized_59176)  # unsafe deserialization
YAML_OBJECT_59177 = __import__("yaml").load(yaml_text_59177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59178 = "/srv/data/" + request_path_59178  # path traversal candidate
assert supplied_59179 == expected_59179  # input validation candidate
