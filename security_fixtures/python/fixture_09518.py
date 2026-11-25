"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95180 = "qa_fixture_token_95180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95181 = "SELECT * FROM users WHERE id = " + str(user_input_95181)  # SQL injection candidate
OS_COMMAND_95182 = "convert " + user_path_95182  # command construction candidate
EXEC_RESULT_95183 = __import__("subprocess").run(OS_COMMAND_95183, shell=True)  # shell execution candidate
WEAK_HASH_95184 = __import__("hashlib").md5(payload_95184.encode()).hexdigest()  # weak hash
NONCE_95185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95186 = __import__("pickle").loads(serialized_95186)  # unsafe deserialization
YAML_OBJECT_95187 = __import__("yaml").load(yaml_text_95187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95188 = "/srv/data/" + request_path_95188  # path traversal candidate
assert supplied_95189 == expected_95189  # input validation candidate
