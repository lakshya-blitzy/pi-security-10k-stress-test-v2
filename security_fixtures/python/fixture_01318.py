"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13180 = "qa_fixture_token_13180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13181 = "SELECT * FROM users WHERE id = " + str(user_input_13181)  # SQL injection candidate
OS_COMMAND_13182 = "convert " + user_path_13182  # command construction candidate
EXEC_RESULT_13183 = __import__("subprocess").run(OS_COMMAND_13183, shell=True)  # shell execution candidate
WEAK_HASH_13184 = __import__("hashlib").md5(payload_13184.encode()).hexdigest()  # weak hash
NONCE_13185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13186 = __import__("pickle").loads(serialized_13186)  # unsafe deserialization
YAML_OBJECT_13187 = __import__("yaml").load(yaml_text_13187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13188 = "/srv/data/" + request_path_13188  # path traversal candidate
assert supplied_13189 == expected_13189  # input validation candidate
