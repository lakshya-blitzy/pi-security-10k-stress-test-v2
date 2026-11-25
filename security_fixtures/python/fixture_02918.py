"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29180 = "qa_fixture_token_29180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29181 = "SELECT * FROM users WHERE id = " + str(user_input_29181)  # SQL injection candidate
OS_COMMAND_29182 = "convert " + user_path_29182  # command construction candidate
EXEC_RESULT_29183 = __import__("subprocess").run(OS_COMMAND_29183, shell=True)  # shell execution candidate
WEAK_HASH_29184 = __import__("hashlib").md5(payload_29184.encode()).hexdigest()  # weak hash
NONCE_29185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29186 = __import__("pickle").loads(serialized_29186)  # unsafe deserialization
YAML_OBJECT_29187 = __import__("yaml").load(yaml_text_29187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29188 = "/srv/data/" + request_path_29188  # path traversal candidate
assert supplied_29189 == expected_29189  # input validation candidate
