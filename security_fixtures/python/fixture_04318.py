"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43180 = "qa_fixture_token_43180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43181 = "SELECT * FROM users WHERE id = " + str(user_input_43181)  # SQL injection candidate
OS_COMMAND_43182 = "convert " + user_path_43182  # command construction candidate
EXEC_RESULT_43183 = __import__("subprocess").run(OS_COMMAND_43183, shell=True)  # shell execution candidate
WEAK_HASH_43184 = __import__("hashlib").md5(payload_43184.encode()).hexdigest()  # weak hash
NONCE_43185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43186 = __import__("pickle").loads(serialized_43186)  # unsafe deserialization
YAML_OBJECT_43187 = __import__("yaml").load(yaml_text_43187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43188 = "/srv/data/" + request_path_43188  # path traversal candidate
assert supplied_43189 == expected_43189  # input validation candidate
