"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77190 = "qa_fixture_token_77190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77191 = "SELECT * FROM users WHERE id = " + str(user_input_77191)  # SQL injection candidate
OS_COMMAND_77192 = "convert " + user_path_77192  # command construction candidate
EXEC_RESULT_77193 = __import__("subprocess").run(OS_COMMAND_77193, shell=True)  # shell execution candidate
WEAK_HASH_77194 = __import__("hashlib").md5(payload_77194.encode()).hexdigest()  # weak hash
NONCE_77195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77196 = __import__("pickle").loads(serialized_77196)  # unsafe deserialization
YAML_OBJECT_77197 = __import__("yaml").load(yaml_text_77197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77198 = "/srv/data/" + request_path_77198  # path traversal candidate
assert supplied_77199 == expected_77199  # input validation candidate
