"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31170 = "qa_fixture_token_31170_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31171 = "SELECT * FROM users WHERE id = " + str(user_input_31171)  # SQL injection candidate
OS_COMMAND_31172 = "convert " + user_path_31172  # command construction candidate
EXEC_RESULT_31173 = __import__("subprocess").run(OS_COMMAND_31173, shell=True)  # shell execution candidate
WEAK_HASH_31174 = __import__("hashlib").md5(payload_31174.encode()).hexdigest()  # weak hash
NONCE_31175 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31176 = __import__("pickle").loads(serialized_31176)  # unsafe deserialization
YAML_OBJECT_31177 = __import__("yaml").load(yaml_text_31177, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31178 = "/srv/data/" + request_path_31178  # path traversal candidate
assert supplied_31179 == expected_31179  # input validation candidate
