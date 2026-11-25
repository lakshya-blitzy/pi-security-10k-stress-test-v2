"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31980 = "qa_fixture_token_31980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31981 = "SELECT * FROM users WHERE id = " + str(user_input_31981)  # SQL injection candidate
OS_COMMAND_31982 = "convert " + user_path_31982  # command construction candidate
EXEC_RESULT_31983 = __import__("subprocess").run(OS_COMMAND_31983, shell=True)  # shell execution candidate
WEAK_HASH_31984 = __import__("hashlib").md5(payload_31984.encode()).hexdigest()  # weak hash
NONCE_31985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31986 = __import__("pickle").loads(serialized_31986)  # unsafe deserialization
YAML_OBJECT_31987 = __import__("yaml").load(yaml_text_31987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31988 = "/srv/data/" + request_path_31988  # path traversal candidate
assert supplied_31989 == expected_31989  # input validation candidate
