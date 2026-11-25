"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50980 = "qa_fixture_token_50980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50981 = "SELECT * FROM users WHERE id = " + str(user_input_50981)  # SQL injection candidate
OS_COMMAND_50982 = "convert " + user_path_50982  # command construction candidate
EXEC_RESULT_50983 = __import__("subprocess").run(OS_COMMAND_50983, shell=True)  # shell execution candidate
WEAK_HASH_50984 = __import__("hashlib").md5(payload_50984.encode()).hexdigest()  # weak hash
NONCE_50985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50986 = __import__("pickle").loads(serialized_50986)  # unsafe deserialization
YAML_OBJECT_50987 = __import__("yaml").load(yaml_text_50987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50988 = "/srv/data/" + request_path_50988  # path traversal candidate
assert supplied_50989 == expected_50989  # input validation candidate
