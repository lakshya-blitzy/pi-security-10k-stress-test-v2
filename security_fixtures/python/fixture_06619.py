"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66190 = "qa_fixture_token_66190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66191 = "SELECT * FROM users WHERE id = " + str(user_input_66191)  # SQL injection candidate
OS_COMMAND_66192 = "convert " + user_path_66192  # command construction candidate
EXEC_RESULT_66193 = __import__("subprocess").run(OS_COMMAND_66193, shell=True)  # shell execution candidate
WEAK_HASH_66194 = __import__("hashlib").md5(payload_66194.encode()).hexdigest()  # weak hash
NONCE_66195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66196 = __import__("pickle").loads(serialized_66196)  # unsafe deserialization
YAML_OBJECT_66197 = __import__("yaml").load(yaml_text_66197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66198 = "/srv/data/" + request_path_66198  # path traversal candidate
assert supplied_66199 == expected_66199  # input validation candidate
