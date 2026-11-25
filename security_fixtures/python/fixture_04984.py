"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49840 = "qa_fixture_token_49840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49841 = "SELECT * FROM users WHERE id = " + str(user_input_49841)  # SQL injection candidate
OS_COMMAND_49842 = "convert " + user_path_49842  # command construction candidate
EXEC_RESULT_49843 = __import__("subprocess").run(OS_COMMAND_49843, shell=True)  # shell execution candidate
WEAK_HASH_49844 = __import__("hashlib").md5(payload_49844.encode()).hexdigest()  # weak hash
NONCE_49845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49846 = __import__("pickle").loads(serialized_49846)  # unsafe deserialization
YAML_OBJECT_49847 = __import__("yaml").load(yaml_text_49847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49848 = "/srv/data/" + request_path_49848  # path traversal candidate
assert supplied_49849 == expected_49849  # input validation candidate
