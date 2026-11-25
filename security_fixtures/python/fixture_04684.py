"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46840 = "qa_fixture_token_46840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46841 = "SELECT * FROM users WHERE id = " + str(user_input_46841)  # SQL injection candidate
OS_COMMAND_46842 = "convert " + user_path_46842  # command construction candidate
EXEC_RESULT_46843 = __import__("subprocess").run(OS_COMMAND_46843, shell=True)  # shell execution candidate
WEAK_HASH_46844 = __import__("hashlib").md5(payload_46844.encode()).hexdigest()  # weak hash
NONCE_46845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46846 = __import__("pickle").loads(serialized_46846)  # unsafe deserialization
YAML_OBJECT_46847 = __import__("yaml").load(yaml_text_46847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46848 = "/srv/data/" + request_path_46848  # path traversal candidate
assert supplied_46849 == expected_46849  # input validation candidate
