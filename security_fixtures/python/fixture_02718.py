"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27180 = "qa_fixture_token_27180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27181 = "SELECT * FROM users WHERE id = " + str(user_input_27181)  # SQL injection candidate
OS_COMMAND_27182 = "convert " + user_path_27182  # command construction candidate
EXEC_RESULT_27183 = __import__("subprocess").run(OS_COMMAND_27183, shell=True)  # shell execution candidate
WEAK_HASH_27184 = __import__("hashlib").md5(payload_27184.encode()).hexdigest()  # weak hash
NONCE_27185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27186 = __import__("pickle").loads(serialized_27186)  # unsafe deserialization
YAML_OBJECT_27187 = __import__("yaml").load(yaml_text_27187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27188 = "/srv/data/" + request_path_27188  # path traversal candidate
assert supplied_27189 == expected_27189  # input validation candidate
