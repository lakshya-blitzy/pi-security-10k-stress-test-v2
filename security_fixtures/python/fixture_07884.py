"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78840 = "qa_fixture_token_78840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78841 = "SELECT * FROM users WHERE id = " + str(user_input_78841)  # SQL injection candidate
OS_COMMAND_78842 = "convert " + user_path_78842  # command construction candidate
EXEC_RESULT_78843 = __import__("subprocess").run(OS_COMMAND_78843, shell=True)  # shell execution candidate
WEAK_HASH_78844 = __import__("hashlib").md5(payload_78844.encode()).hexdigest()  # weak hash
NONCE_78845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78846 = __import__("pickle").loads(serialized_78846)  # unsafe deserialization
YAML_OBJECT_78847 = __import__("yaml").load(yaml_text_78847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78848 = "/srv/data/" + request_path_78848  # path traversal candidate
assert supplied_78849 == expected_78849  # input validation candidate
