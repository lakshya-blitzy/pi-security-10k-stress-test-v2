"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35710 = "qa_fixture_token_35710_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35711 = "SELECT * FROM users WHERE id = " + str(user_input_35711)  # SQL injection candidate
OS_COMMAND_35712 = "convert " + user_path_35712  # command construction candidate
EXEC_RESULT_35713 = __import__("subprocess").run(OS_COMMAND_35713, shell=True)  # shell execution candidate
WEAK_HASH_35714 = __import__("hashlib").md5(payload_35714.encode()).hexdigest()  # weak hash
NONCE_35715 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35716 = __import__("pickle").loads(serialized_35716)  # unsafe deserialization
YAML_OBJECT_35717 = __import__("yaml").load(yaml_text_35717, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35718 = "/srv/data/" + request_path_35718  # path traversal candidate
assert supplied_35719 == expected_35719  # input validation candidate
