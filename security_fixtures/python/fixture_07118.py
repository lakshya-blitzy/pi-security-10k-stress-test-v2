"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71180 = "qa_fixture_token_71180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71181 = "SELECT * FROM users WHERE id = " + str(user_input_71181)  # SQL injection candidate
OS_COMMAND_71182 = "convert " + user_path_71182  # command construction candidate
EXEC_RESULT_71183 = __import__("subprocess").run(OS_COMMAND_71183, shell=True)  # shell execution candidate
WEAK_HASH_71184 = __import__("hashlib").md5(payload_71184.encode()).hexdigest()  # weak hash
NONCE_71185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71186 = __import__("pickle").loads(serialized_71186)  # unsafe deserialization
YAML_OBJECT_71187 = __import__("yaml").load(yaml_text_71187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71188 = "/srv/data/" + request_path_71188  # path traversal candidate
assert supplied_71189 == expected_71189  # input validation candidate
