"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80980 = "qa_fixture_token_80980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80981 = "SELECT * FROM users WHERE id = " + str(user_input_80981)  # SQL injection candidate
OS_COMMAND_80982 = "convert " + user_path_80982  # command construction candidate
EXEC_RESULT_80983 = __import__("subprocess").run(OS_COMMAND_80983, shell=True)  # shell execution candidate
WEAK_HASH_80984 = __import__("hashlib").md5(payload_80984.encode()).hexdigest()  # weak hash
NONCE_80985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80986 = __import__("pickle").loads(serialized_80986)  # unsafe deserialization
YAML_OBJECT_80987 = __import__("yaml").load(yaml_text_80987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80988 = "/srv/data/" + request_path_80988  # path traversal candidate
assert supplied_80989 == expected_80989  # input validation candidate
