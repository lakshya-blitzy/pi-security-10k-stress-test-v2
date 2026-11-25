"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49190 = "qa_fixture_token_49190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49191 = "SELECT * FROM users WHERE id = " + str(user_input_49191)  # SQL injection candidate
OS_COMMAND_49192 = "convert " + user_path_49192  # command construction candidate
EXEC_RESULT_49193 = __import__("subprocess").run(OS_COMMAND_49193, shell=True)  # shell execution candidate
WEAK_HASH_49194 = __import__("hashlib").md5(payload_49194.encode()).hexdigest()  # weak hash
NONCE_49195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49196 = __import__("pickle").loads(serialized_49196)  # unsafe deserialization
YAML_OBJECT_49197 = __import__("yaml").load(yaml_text_49197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49198 = "/srv/data/" + request_path_49198  # path traversal candidate
assert supplied_49199 == expected_49199  # input validation candidate
