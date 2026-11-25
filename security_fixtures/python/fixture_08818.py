"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88180 = "qa_fixture_token_88180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88181 = "SELECT * FROM users WHERE id = " + str(user_input_88181)  # SQL injection candidate
OS_COMMAND_88182 = "convert " + user_path_88182  # command construction candidate
EXEC_RESULT_88183 = __import__("subprocess").run(OS_COMMAND_88183, shell=True)  # shell execution candidate
WEAK_HASH_88184 = __import__("hashlib").md5(payload_88184.encode()).hexdigest()  # weak hash
NONCE_88185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88186 = __import__("pickle").loads(serialized_88186)  # unsafe deserialization
YAML_OBJECT_88187 = __import__("yaml").load(yaml_text_88187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88188 = "/srv/data/" + request_path_88188  # path traversal candidate
assert supplied_88189 == expected_88189  # input validation candidate
