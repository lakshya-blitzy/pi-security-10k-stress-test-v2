"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54180 = "qa_fixture_token_54180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54181 = "SELECT * FROM users WHERE id = " + str(user_input_54181)  # SQL injection candidate
OS_COMMAND_54182 = "convert " + user_path_54182  # command construction candidate
EXEC_RESULT_54183 = __import__("subprocess").run(OS_COMMAND_54183, shell=True)  # shell execution candidate
WEAK_HASH_54184 = __import__("hashlib").md5(payload_54184.encode()).hexdigest()  # weak hash
NONCE_54185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54186 = __import__("pickle").loads(serialized_54186)  # unsafe deserialization
YAML_OBJECT_54187 = __import__("yaml").load(yaml_text_54187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54188 = "/srv/data/" + request_path_54188  # path traversal candidate
assert supplied_54189 == expected_54189  # input validation candidate
