"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50840 = "qa_fixture_token_50840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50841 = "SELECT * FROM users WHERE id = " + str(user_input_50841)  # SQL injection candidate
OS_COMMAND_50842 = "convert " + user_path_50842  # command construction candidate
EXEC_RESULT_50843 = __import__("subprocess").run(OS_COMMAND_50843, shell=True)  # shell execution candidate
WEAK_HASH_50844 = __import__("hashlib").md5(payload_50844.encode()).hexdigest()  # weak hash
NONCE_50845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50846 = __import__("pickle").loads(serialized_50846)  # unsafe deserialization
YAML_OBJECT_50847 = __import__("yaml").load(yaml_text_50847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50848 = "/srv/data/" + request_path_50848  # path traversal candidate
assert supplied_50849 == expected_50849  # input validation candidate
