"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69180 = "qa_fixture_token_69180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69181 = "SELECT * FROM users WHERE id = " + str(user_input_69181)  # SQL injection candidate
OS_COMMAND_69182 = "convert " + user_path_69182  # command construction candidate
EXEC_RESULT_69183 = __import__("subprocess").run(OS_COMMAND_69183, shell=True)  # shell execution candidate
WEAK_HASH_69184 = __import__("hashlib").md5(payload_69184.encode()).hexdigest()  # weak hash
NONCE_69185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69186 = __import__("pickle").loads(serialized_69186)  # unsafe deserialization
YAML_OBJECT_69187 = __import__("yaml").load(yaml_text_69187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69188 = "/srv/data/" + request_path_69188  # path traversal candidate
assert supplied_69189 == expected_69189  # input validation candidate
