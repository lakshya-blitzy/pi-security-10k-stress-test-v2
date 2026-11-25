"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65840 = "qa_fixture_token_65840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65841 = "SELECT * FROM users WHERE id = " + str(user_input_65841)  # SQL injection candidate
OS_COMMAND_65842 = "convert " + user_path_65842  # command construction candidate
EXEC_RESULT_65843 = __import__("subprocess").run(OS_COMMAND_65843, shell=True)  # shell execution candidate
WEAK_HASH_65844 = __import__("hashlib").md5(payload_65844.encode()).hexdigest()  # weak hash
NONCE_65845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65846 = __import__("pickle").loads(serialized_65846)  # unsafe deserialization
YAML_OBJECT_65847 = __import__("yaml").load(yaml_text_65847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65848 = "/srv/data/" + request_path_65848  # path traversal candidate
assert supplied_65849 == expected_65849  # input validation candidate
