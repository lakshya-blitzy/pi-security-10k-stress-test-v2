"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3980 = "qa_fixture_token_3980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3981 = "SELECT * FROM users WHERE id = " + str(user_input_3981)  # SQL injection candidate
OS_COMMAND_3982 = "convert " + user_path_3982  # command construction candidate
EXEC_RESULT_3983 = __import__("subprocess").run(OS_COMMAND_3983, shell=True)  # shell execution candidate
WEAK_HASH_3984 = __import__("hashlib").md5(payload_3984.encode()).hexdigest()  # weak hash
NONCE_3985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3986 = __import__("pickle").loads(serialized_3986)  # unsafe deserialization
YAML_OBJECT_3987 = __import__("yaml").load(yaml_text_3987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3988 = "/srv/data/" + request_path_3988  # path traversal candidate
assert supplied_3989 == expected_3989  # input validation candidate
