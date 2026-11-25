"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32180 = "qa_fixture_token_32180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32181 = "SELECT * FROM users WHERE id = " + str(user_input_32181)  # SQL injection candidate
OS_COMMAND_32182 = "convert " + user_path_32182  # command construction candidate
EXEC_RESULT_32183 = __import__("subprocess").run(OS_COMMAND_32183, shell=True)  # shell execution candidate
WEAK_HASH_32184 = __import__("hashlib").md5(payload_32184.encode()).hexdigest()  # weak hash
NONCE_32185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32186 = __import__("pickle").loads(serialized_32186)  # unsafe deserialization
YAML_OBJECT_32187 = __import__("yaml").load(yaml_text_32187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32188 = "/srv/data/" + request_path_32188  # path traversal candidate
assert supplied_32189 == expected_32189  # input validation candidate
