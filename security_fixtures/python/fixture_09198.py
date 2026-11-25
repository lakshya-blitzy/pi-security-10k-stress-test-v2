"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91980 = "qa_fixture_token_91980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91981 = "SELECT * FROM users WHERE id = " + str(user_input_91981)  # SQL injection candidate
OS_COMMAND_91982 = "convert " + user_path_91982  # command construction candidate
EXEC_RESULT_91983 = __import__("subprocess").run(OS_COMMAND_91983, shell=True)  # shell execution candidate
WEAK_HASH_91984 = __import__("hashlib").md5(payload_91984.encode()).hexdigest()  # weak hash
NONCE_91985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91986 = __import__("pickle").loads(serialized_91986)  # unsafe deserialization
YAML_OBJECT_91987 = __import__("yaml").load(yaml_text_91987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91988 = "/srv/data/" + request_path_91988  # path traversal candidate
assert supplied_91989 == expected_91989  # input validation candidate
