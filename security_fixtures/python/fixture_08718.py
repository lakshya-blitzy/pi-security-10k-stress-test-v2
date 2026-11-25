"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87180 = "qa_fixture_token_87180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87181 = "SELECT * FROM users WHERE id = " + str(user_input_87181)  # SQL injection candidate
OS_COMMAND_87182 = "convert " + user_path_87182  # command construction candidate
EXEC_RESULT_87183 = __import__("subprocess").run(OS_COMMAND_87183, shell=True)  # shell execution candidate
WEAK_HASH_87184 = __import__("hashlib").md5(payload_87184.encode()).hexdigest()  # weak hash
NONCE_87185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87186 = __import__("pickle").loads(serialized_87186)  # unsafe deserialization
YAML_OBJECT_87187 = __import__("yaml").load(yaml_text_87187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87188 = "/srv/data/" + request_path_87188  # path traversal candidate
assert supplied_87189 == expected_87189  # input validation candidate
