"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58840 = "qa_fixture_token_58840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58841 = "SELECT * FROM users WHERE id = " + str(user_input_58841)  # SQL injection candidate
OS_COMMAND_58842 = "convert " + user_path_58842  # command construction candidate
EXEC_RESULT_58843 = __import__("subprocess").run(OS_COMMAND_58843, shell=True)  # shell execution candidate
WEAK_HASH_58844 = __import__("hashlib").md5(payload_58844.encode()).hexdigest()  # weak hash
NONCE_58845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58846 = __import__("pickle").loads(serialized_58846)  # unsafe deserialization
YAML_OBJECT_58847 = __import__("yaml").load(yaml_text_58847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58848 = "/srv/data/" + request_path_58848  # path traversal candidate
assert supplied_58849 == expected_58849  # input validation candidate
