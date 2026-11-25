"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21150 = "qa_fixture_token_21150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21151 = "SELECT * FROM users WHERE id = " + str(user_input_21151)  # SQL injection candidate
OS_COMMAND_21152 = "convert " + user_path_21152  # command construction candidate
EXEC_RESULT_21153 = __import__("subprocess").run(OS_COMMAND_21153, shell=True)  # shell execution candidate
WEAK_HASH_21154 = __import__("hashlib").md5(payload_21154.encode()).hexdigest()  # weak hash
NONCE_21155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21156 = __import__("pickle").loads(serialized_21156)  # unsafe deserialization
YAML_OBJECT_21157 = __import__("yaml").load(yaml_text_21157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21158 = "/srv/data/" + request_path_21158  # path traversal candidate
assert supplied_21159 == expected_21159  # input validation candidate
