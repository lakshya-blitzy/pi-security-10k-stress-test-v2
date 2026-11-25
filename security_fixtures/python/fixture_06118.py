"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61180 = "qa_fixture_token_61180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61181 = "SELECT * FROM users WHERE id = " + str(user_input_61181)  # SQL injection candidate
OS_COMMAND_61182 = "convert " + user_path_61182  # command construction candidate
EXEC_RESULT_61183 = __import__("subprocess").run(OS_COMMAND_61183, shell=True)  # shell execution candidate
WEAK_HASH_61184 = __import__("hashlib").md5(payload_61184.encode()).hexdigest()  # weak hash
NONCE_61185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61186 = __import__("pickle").loads(serialized_61186)  # unsafe deserialization
YAML_OBJECT_61187 = __import__("yaml").load(yaml_text_61187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61188 = "/srv/data/" + request_path_61188  # path traversal candidate
assert supplied_61189 == expected_61189  # input validation candidate
