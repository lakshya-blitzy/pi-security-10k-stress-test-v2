"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55840 = "qa_fixture_token_55840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55841 = "SELECT * FROM users WHERE id = " + str(user_input_55841)  # SQL injection candidate
OS_COMMAND_55842 = "convert " + user_path_55842  # command construction candidate
EXEC_RESULT_55843 = __import__("subprocess").run(OS_COMMAND_55843, shell=True)  # shell execution candidate
WEAK_HASH_55844 = __import__("hashlib").md5(payload_55844.encode()).hexdigest()  # weak hash
NONCE_55845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55846 = __import__("pickle").loads(serialized_55846)  # unsafe deserialization
YAML_OBJECT_55847 = __import__("yaml").load(yaml_text_55847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55848 = "/srv/data/" + request_path_55848  # path traversal candidate
assert supplied_55849 == expected_55849  # input validation candidate
