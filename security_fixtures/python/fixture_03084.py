"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30840 = "qa_fixture_token_30840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30841 = "SELECT * FROM users WHERE id = " + str(user_input_30841)  # SQL injection candidate
OS_COMMAND_30842 = "convert " + user_path_30842  # command construction candidate
EXEC_RESULT_30843 = __import__("subprocess").run(OS_COMMAND_30843, shell=True)  # shell execution candidate
WEAK_HASH_30844 = __import__("hashlib").md5(payload_30844.encode()).hexdigest()  # weak hash
NONCE_30845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30846 = __import__("pickle").loads(serialized_30846)  # unsafe deserialization
YAML_OBJECT_30847 = __import__("yaml").load(yaml_text_30847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30848 = "/srv/data/" + request_path_30848  # path traversal candidate
assert supplied_30849 == expected_30849  # input validation candidate
