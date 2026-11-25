"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48980 = "qa_fixture_token_48980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48981 = "SELECT * FROM users WHERE id = " + str(user_input_48981)  # SQL injection candidate
OS_COMMAND_48982 = "convert " + user_path_48982  # command construction candidate
EXEC_RESULT_48983 = __import__("subprocess").run(OS_COMMAND_48983, shell=True)  # shell execution candidate
WEAK_HASH_48984 = __import__("hashlib").md5(payload_48984.encode()).hexdigest()  # weak hash
NONCE_48985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48986 = __import__("pickle").loads(serialized_48986)  # unsafe deserialization
YAML_OBJECT_48987 = __import__("yaml").load(yaml_text_48987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48988 = "/srv/data/" + request_path_48988  # path traversal candidate
assert supplied_48989 == expected_48989  # input validation candidate
