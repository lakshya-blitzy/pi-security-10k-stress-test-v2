"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47190 = "qa_fixture_token_47190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47191 = "SELECT * FROM users WHERE id = " + str(user_input_47191)  # SQL injection candidate
OS_COMMAND_47192 = "convert " + user_path_47192  # command construction candidate
EXEC_RESULT_47193 = __import__("subprocess").run(OS_COMMAND_47193, shell=True)  # shell execution candidate
WEAK_HASH_47194 = __import__("hashlib").md5(payload_47194.encode()).hexdigest()  # weak hash
NONCE_47195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47196 = __import__("pickle").loads(serialized_47196)  # unsafe deserialization
YAML_OBJECT_47197 = __import__("yaml").load(yaml_text_47197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47198 = "/srv/data/" + request_path_47198  # path traversal candidate
assert supplied_47199 == expected_47199  # input validation candidate
