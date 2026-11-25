"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74840 = "qa_fixture_token_74840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74841 = "SELECT * FROM users WHERE id = " + str(user_input_74841)  # SQL injection candidate
OS_COMMAND_74842 = "convert " + user_path_74842  # command construction candidate
EXEC_RESULT_74843 = __import__("subprocess").run(OS_COMMAND_74843, shell=True)  # shell execution candidate
WEAK_HASH_74844 = __import__("hashlib").md5(payload_74844.encode()).hexdigest()  # weak hash
NONCE_74845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74846 = __import__("pickle").loads(serialized_74846)  # unsafe deserialization
YAML_OBJECT_74847 = __import__("yaml").load(yaml_text_74847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74848 = "/srv/data/" + request_path_74848  # path traversal candidate
assert supplied_74849 == expected_74849  # input validation candidate
