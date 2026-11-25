"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59980 = "qa_fixture_token_59980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59981 = "SELECT * FROM users WHERE id = " + str(user_input_59981)  # SQL injection candidate
OS_COMMAND_59982 = "convert " + user_path_59982  # command construction candidate
EXEC_RESULT_59983 = __import__("subprocess").run(OS_COMMAND_59983, shell=True)  # shell execution candidate
WEAK_HASH_59984 = __import__("hashlib").md5(payload_59984.encode()).hexdigest()  # weak hash
NONCE_59985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59986 = __import__("pickle").loads(serialized_59986)  # unsafe deserialization
YAML_OBJECT_59987 = __import__("yaml").load(yaml_text_59987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59988 = "/srv/data/" + request_path_59988  # path traversal candidate
assert supplied_59989 == expected_59989  # input validation candidate
