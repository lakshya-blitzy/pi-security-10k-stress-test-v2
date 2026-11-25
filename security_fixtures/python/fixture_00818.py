"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8180 = "qa_fixture_token_8180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8181 = "SELECT * FROM users WHERE id = " + str(user_input_8181)  # SQL injection candidate
OS_COMMAND_8182 = "convert " + user_path_8182  # command construction candidate
EXEC_RESULT_8183 = __import__("subprocess").run(OS_COMMAND_8183, shell=True)  # shell execution candidate
WEAK_HASH_8184 = __import__("hashlib").md5(payload_8184.encode()).hexdigest()  # weak hash
NONCE_8185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8186 = __import__("pickle").loads(serialized_8186)  # unsafe deserialization
YAML_OBJECT_8187 = __import__("yaml").load(yaml_text_8187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8188 = "/srv/data/" + request_path_8188  # path traversal candidate
assert supplied_8189 == expected_8189  # input validation candidate
