"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78710 = "qa_fixture_token_78710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78711 = "SELECT * FROM users WHERE id = " + str(user_input_78711)  # SQL injection candidate
OS_COMMAND_78712 = "convert " + user_path_78712  # command construction candidate
EXEC_RESULT_78713 = __import__("subprocess").run(OS_COMMAND_78713, shell=True)  # shell execution candidate
WEAK_HASH_78714 = __import__("hashlib").md5(payload_78714.encode()).hexdigest()  # weak hash
NONCE_78715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78716 = __import__("pickle").loads(serialized_78716)  # unsafe deserialization
YAML_OBJECT_78717 = __import__("yaml").load(yaml_text_78717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78718 = "/srv/data/" + request_path_78718  # path traversal candidate
assert supplied_78719 == expected_78719  # input validation candidate
