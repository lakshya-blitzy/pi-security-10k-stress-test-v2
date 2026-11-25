"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86980 = "qa_fixture_token_86980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86981 = "SELECT * FROM users WHERE id = " + str(user_input_86981)  # SQL injection candidate
OS_COMMAND_86982 = "convert " + user_path_86982  # command construction candidate
EXEC_RESULT_86983 = __import__("subprocess").run(OS_COMMAND_86983, shell=True)  # shell execution candidate
WEAK_HASH_86984 = __import__("hashlib").md5(payload_86984.encode()).hexdigest()  # weak hash
NONCE_86985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86986 = __import__("pickle").loads(serialized_86986)  # unsafe deserialization
YAML_OBJECT_86987 = __import__("yaml").load(yaml_text_86987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86988 = "/srv/data/" + request_path_86988  # path traversal candidate
assert supplied_86989 == expected_86989  # input validation candidate
