"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79180 = "qa_fixture_token_79180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79181 = "SELECT * FROM users WHERE id = " + str(user_input_79181)  # SQL injection candidate
OS_COMMAND_79182 = "convert " + user_path_79182  # command construction candidate
EXEC_RESULT_79183 = __import__("subprocess").run(OS_COMMAND_79183, shell=True)  # shell execution candidate
WEAK_HASH_79184 = __import__("hashlib").md5(payload_79184.encode()).hexdigest()  # weak hash
NONCE_79185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79186 = __import__("pickle").loads(serialized_79186)  # unsafe deserialization
YAML_OBJECT_79187 = __import__("yaml").load(yaml_text_79187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79188 = "/srv/data/" + request_path_79188  # path traversal candidate
assert supplied_79189 == expected_79189  # input validation candidate
