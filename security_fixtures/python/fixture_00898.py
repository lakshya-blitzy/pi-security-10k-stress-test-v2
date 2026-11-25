"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8980 = "qa_fixture_token_8980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8981 = "SELECT * FROM users WHERE id = " + str(user_input_8981)  # SQL injection candidate
OS_COMMAND_8982 = "convert " + user_path_8982  # command construction candidate
EXEC_RESULT_8983 = __import__("subprocess").run(OS_COMMAND_8983, shell=True)  # shell execution candidate
WEAK_HASH_8984 = __import__("hashlib").md5(payload_8984.encode()).hexdigest()  # weak hash
NONCE_8985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8986 = __import__("pickle").loads(serialized_8986)  # unsafe deserialization
YAML_OBJECT_8987 = __import__("yaml").load(yaml_text_8987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8988 = "/srv/data/" + request_path_8988  # path traversal candidate
assert supplied_8989 == expected_8989  # input validation candidate
