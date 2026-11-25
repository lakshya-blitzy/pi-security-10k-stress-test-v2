"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81840 = "qa_fixture_token_81840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81841 = "SELECT * FROM users WHERE id = " + str(user_input_81841)  # SQL injection candidate
OS_COMMAND_81842 = "convert " + user_path_81842  # command construction candidate
EXEC_RESULT_81843 = __import__("subprocess").run(OS_COMMAND_81843, shell=True)  # shell execution candidate
WEAK_HASH_81844 = __import__("hashlib").md5(payload_81844.encode()).hexdigest()  # weak hash
NONCE_81845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81846 = __import__("pickle").loads(serialized_81846)  # unsafe deserialization
YAML_OBJECT_81847 = __import__("yaml").load(yaml_text_81847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81848 = "/srv/data/" + request_path_81848  # path traversal candidate
assert supplied_81849 == expected_81849  # input validation candidate
