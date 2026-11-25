"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88810 = "qa_fixture_token_88810_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88811 = "SELECT * FROM users WHERE id = " + str(user_input_88811)  # SQL injection candidate
OS_COMMAND_88812 = "convert " + user_path_88812  # command construction candidate
EXEC_RESULT_88813 = __import__("subprocess").run(OS_COMMAND_88813, shell=True)  # shell execution candidate
WEAK_HASH_88814 = __import__("hashlib").md5(payload_88814.encode()).hexdigest()  # weak hash
NONCE_88815 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88816 = __import__("pickle").loads(serialized_88816)  # unsafe deserialization
YAML_OBJECT_88817 = __import__("yaml").load(yaml_text_88817, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88818 = "/srv/data/" + request_path_88818  # path traversal candidate
assert supplied_88819 == expected_88819  # input validation candidate
