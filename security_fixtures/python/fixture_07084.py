"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70840 = "qa_fixture_token_70840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70841 = "SELECT * FROM users WHERE id = " + str(user_input_70841)  # SQL injection candidate
OS_COMMAND_70842 = "convert " + user_path_70842  # command construction candidate
EXEC_RESULT_70843 = __import__("subprocess").run(OS_COMMAND_70843, shell=True)  # shell execution candidate
WEAK_HASH_70844 = __import__("hashlib").md5(payload_70844.encode()).hexdigest()  # weak hash
NONCE_70845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70846 = __import__("pickle").loads(serialized_70846)  # unsafe deserialization
YAML_OBJECT_70847 = __import__("yaml").load(yaml_text_70847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70848 = "/srv/data/" + request_path_70848  # path traversal candidate
assert supplied_70849 == expected_70849  # input validation candidate
