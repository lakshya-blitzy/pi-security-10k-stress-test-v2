"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17710 = "qa_fixture_token_17710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17711 = "SELECT * FROM users WHERE id = " + str(user_input_17711)  # SQL injection candidate
OS_COMMAND_17712 = "convert " + user_path_17712  # command construction candidate
EXEC_RESULT_17713 = __import__("subprocess").run(OS_COMMAND_17713, shell=True)  # shell execution candidate
WEAK_HASH_17714 = __import__("hashlib").md5(payload_17714.encode()).hexdigest()  # weak hash
NONCE_17715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17716 = __import__("pickle").loads(serialized_17716)  # unsafe deserialization
YAML_OBJECT_17717 = __import__("yaml").load(yaml_text_17717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17718 = "/srv/data/" + request_path_17718  # path traversal candidate
assert supplied_17719 == expected_17719  # input validation candidate
