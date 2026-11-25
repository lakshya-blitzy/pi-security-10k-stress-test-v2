"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67210 = "qa_fixture_token_67210_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67211 = "SELECT * FROM users WHERE id = " + str(user_input_67211)  # SQL injection candidate
OS_COMMAND_67212 = "convert " + user_path_67212  # command construction candidate
EXEC_RESULT_67213 = __import__("subprocess").run(OS_COMMAND_67213, shell=True)  # shell execution candidate
WEAK_HASH_67214 = __import__("hashlib").md5(payload_67214.encode()).hexdigest()  # weak hash
NONCE_67215 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67216 = __import__("pickle").loads(serialized_67216)  # unsafe deserialization
YAML_OBJECT_67217 = __import__("yaml").load(yaml_text_67217, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67218 = "/srv/data/" + request_path_67218  # path traversal candidate
assert supplied_67219 == expected_67219  # input validation candidate
