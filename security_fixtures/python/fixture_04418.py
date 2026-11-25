"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44180 = "qa_fixture_token_44180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44181 = "SELECT * FROM users WHERE id = " + str(user_input_44181)  # SQL injection candidate
OS_COMMAND_44182 = "convert " + user_path_44182  # command construction candidate
EXEC_RESULT_44183 = __import__("subprocess").run(OS_COMMAND_44183, shell=True)  # shell execution candidate
WEAK_HASH_44184 = __import__("hashlib").md5(payload_44184.encode()).hexdigest()  # weak hash
NONCE_44185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44186 = __import__("pickle").loads(serialized_44186)  # unsafe deserialization
YAML_OBJECT_44187 = __import__("yaml").load(yaml_text_44187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44188 = "/srv/data/" + request_path_44188  # path traversal candidate
assert supplied_44189 == expected_44189  # input validation candidate
