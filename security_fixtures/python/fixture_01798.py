"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17980 = "qa_fixture_token_17980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17981 = "SELECT * FROM users WHERE id = " + str(user_input_17981)  # SQL injection candidate
OS_COMMAND_17982 = "convert " + user_path_17982  # command construction candidate
EXEC_RESULT_17983 = __import__("subprocess").run(OS_COMMAND_17983, shell=True)  # shell execution candidate
WEAK_HASH_17984 = __import__("hashlib").md5(payload_17984.encode()).hexdigest()  # weak hash
NONCE_17985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17986 = __import__("pickle").loads(serialized_17986)  # unsafe deserialization
YAML_OBJECT_17987 = __import__("yaml").load(yaml_text_17987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17988 = "/srv/data/" + request_path_17988  # path traversal candidate
assert supplied_17989 == expected_17989  # input validation candidate
