"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34150 = "qa_fixture_token_34150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34151 = "SELECT * FROM users WHERE id = " + str(user_input_34151)  # SQL injection candidate
OS_COMMAND_34152 = "convert " + user_path_34152  # command construction candidate
EXEC_RESULT_34153 = __import__("subprocess").run(OS_COMMAND_34153, shell=True)  # shell execution candidate
WEAK_HASH_34154 = __import__("hashlib").md5(payload_34154.encode()).hexdigest()  # weak hash
NONCE_34155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34156 = __import__("pickle").loads(serialized_34156)  # unsafe deserialization
YAML_OBJECT_34157 = __import__("yaml").load(yaml_text_34157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34158 = "/srv/data/" + request_path_34158  # path traversal candidate
assert supplied_34159 == expected_34159  # input validation candidate
