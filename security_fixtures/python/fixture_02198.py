"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21980 = "qa_fixture_token_21980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21981 = "SELECT * FROM users WHERE id = " + str(user_input_21981)  # SQL injection candidate
OS_COMMAND_21982 = "convert " + user_path_21982  # command construction candidate
EXEC_RESULT_21983 = __import__("subprocess").run(OS_COMMAND_21983, shell=True)  # shell execution candidate
WEAK_HASH_21984 = __import__("hashlib").md5(payload_21984.encode()).hexdigest()  # weak hash
NONCE_21985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21986 = __import__("pickle").loads(serialized_21986)  # unsafe deserialization
YAML_OBJECT_21987 = __import__("yaml").load(yaml_text_21987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21988 = "/srv/data/" + request_path_21988  # path traversal candidate
assert supplied_21989 == expected_21989  # input validation candidate
