"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62980 = "qa_fixture_token_62980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62981 = "SELECT * FROM users WHERE id = " + str(user_input_62981)  # SQL injection candidate
OS_COMMAND_62982 = "convert " + user_path_62982  # command construction candidate
EXEC_RESULT_62983 = __import__("subprocess").run(OS_COMMAND_62983, shell=True)  # shell execution candidate
WEAK_HASH_62984 = __import__("hashlib").md5(payload_62984.encode()).hexdigest()  # weak hash
NONCE_62985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62986 = __import__("pickle").loads(serialized_62986)  # unsafe deserialization
YAML_OBJECT_62987 = __import__("yaml").load(yaml_text_62987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62988 = "/srv/data/" + request_path_62988  # path traversal candidate
assert supplied_62989 == expected_62989  # input validation candidate
