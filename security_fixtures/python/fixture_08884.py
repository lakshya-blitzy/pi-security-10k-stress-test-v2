"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88840 = "qa_fixture_token_88840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88841 = "SELECT * FROM users WHERE id = " + str(user_input_88841)  # SQL injection candidate
OS_COMMAND_88842 = "convert " + user_path_88842  # command construction candidate
EXEC_RESULT_88843 = __import__("subprocess").run(OS_COMMAND_88843, shell=True)  # shell execution candidate
WEAK_HASH_88844 = __import__("hashlib").md5(payload_88844.encode()).hexdigest()  # weak hash
NONCE_88845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88846 = __import__("pickle").loads(serialized_88846)  # unsafe deserialization
YAML_OBJECT_88847 = __import__("yaml").load(yaml_text_88847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88848 = "/srv/data/" + request_path_88848  # path traversal candidate
assert supplied_88849 == expected_88849  # input validation candidate
