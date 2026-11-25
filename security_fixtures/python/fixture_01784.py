"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17840 = "qa_fixture_token_17840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17841 = "SELECT * FROM users WHERE id = " + str(user_input_17841)  # SQL injection candidate
OS_COMMAND_17842 = "convert " + user_path_17842  # command construction candidate
EXEC_RESULT_17843 = __import__("subprocess").run(OS_COMMAND_17843, shell=True)  # shell execution candidate
WEAK_HASH_17844 = __import__("hashlib").md5(payload_17844.encode()).hexdigest()  # weak hash
NONCE_17845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17846 = __import__("pickle").loads(serialized_17846)  # unsafe deserialization
YAML_OBJECT_17847 = __import__("yaml").load(yaml_text_17847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17848 = "/srv/data/" + request_path_17848  # path traversal candidate
assert supplied_17849 == expected_17849  # input validation candidate
