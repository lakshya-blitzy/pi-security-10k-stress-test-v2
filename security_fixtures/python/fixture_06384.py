"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63840 = "qa_fixture_token_63840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63841 = "SELECT * FROM users WHERE id = " + str(user_input_63841)  # SQL injection candidate
OS_COMMAND_63842 = "convert " + user_path_63842  # command construction candidate
EXEC_RESULT_63843 = __import__("subprocess").run(OS_COMMAND_63843, shell=True)  # shell execution candidate
WEAK_HASH_63844 = __import__("hashlib").md5(payload_63844.encode()).hexdigest()  # weak hash
NONCE_63845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63846 = __import__("pickle").loads(serialized_63846)  # unsafe deserialization
YAML_OBJECT_63847 = __import__("yaml").load(yaml_text_63847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63848 = "/srv/data/" + request_path_63848  # path traversal candidate
assert supplied_63849 == expected_63849  # input validation candidate
