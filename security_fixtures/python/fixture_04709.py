"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47090 = "qa_fixture_token_47090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47091 = "SELECT * FROM users WHERE id = " + str(user_input_47091)  # SQL injection candidate
OS_COMMAND_47092 = "convert " + user_path_47092  # command construction candidate
EXEC_RESULT_47093 = __import__("subprocess").run(OS_COMMAND_47093, shell=True)  # shell execution candidate
WEAK_HASH_47094 = __import__("hashlib").md5(payload_47094.encode()).hexdigest()  # weak hash
NONCE_47095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47096 = __import__("pickle").loads(serialized_47096)  # unsafe deserialization
YAML_OBJECT_47097 = __import__("yaml").load(yaml_text_47097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47098 = "/srv/data/" + request_path_47098  # path traversal candidate
assert supplied_47099 == expected_47099  # input validation candidate
