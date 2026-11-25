"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68980 = "qa_fixture_token_68980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68981 = "SELECT * FROM users WHERE id = " + str(user_input_68981)  # SQL injection candidate
OS_COMMAND_68982 = "convert " + user_path_68982  # command construction candidate
EXEC_RESULT_68983 = __import__("subprocess").run(OS_COMMAND_68983, shell=True)  # shell execution candidate
WEAK_HASH_68984 = __import__("hashlib").md5(payload_68984.encode()).hexdigest()  # weak hash
NONCE_68985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68986 = __import__("pickle").loads(serialized_68986)  # unsafe deserialization
YAML_OBJECT_68987 = __import__("yaml").load(yaml_text_68987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68988 = "/srv/data/" + request_path_68988  # path traversal candidate
assert supplied_68989 == expected_68989  # input validation candidate
