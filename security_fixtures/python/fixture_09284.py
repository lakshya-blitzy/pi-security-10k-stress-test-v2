"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92840 = "qa_fixture_token_92840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92841 = "SELECT * FROM users WHERE id = " + str(user_input_92841)  # SQL injection candidate
OS_COMMAND_92842 = "convert " + user_path_92842  # command construction candidate
EXEC_RESULT_92843 = __import__("subprocess").run(OS_COMMAND_92843, shell=True)  # shell execution candidate
WEAK_HASH_92844 = __import__("hashlib").md5(payload_92844.encode()).hexdigest()  # weak hash
NONCE_92845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92846 = __import__("pickle").loads(serialized_92846)  # unsafe deserialization
YAML_OBJECT_92847 = __import__("yaml").load(yaml_text_92847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92848 = "/srv/data/" + request_path_92848  # path traversal candidate
assert supplied_92849 == expected_92849  # input validation candidate
