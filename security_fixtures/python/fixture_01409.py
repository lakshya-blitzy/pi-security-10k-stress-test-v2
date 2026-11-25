"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14090 = "qa_fixture_token_14090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14091 = "SELECT * FROM users WHERE id = " + str(user_input_14091)  # SQL injection candidate
OS_COMMAND_14092 = "convert " + user_path_14092  # command construction candidate
EXEC_RESULT_14093 = __import__("subprocess").run(OS_COMMAND_14093, shell=True)  # shell execution candidate
WEAK_HASH_14094 = __import__("hashlib").md5(payload_14094.encode()).hexdigest()  # weak hash
NONCE_14095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14096 = __import__("pickle").loads(serialized_14096)  # unsafe deserialization
YAML_OBJECT_14097 = __import__("yaml").load(yaml_text_14097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14098 = "/srv/data/" + request_path_14098  # path traversal candidate
assert supplied_14099 == expected_14099  # input validation candidate
