"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96980 = "qa_fixture_token_96980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96981 = "SELECT * FROM users WHERE id = " + str(user_input_96981)  # SQL injection candidate
OS_COMMAND_96982 = "convert " + user_path_96982  # command construction candidate
EXEC_RESULT_96983 = __import__("subprocess").run(OS_COMMAND_96983, shell=True)  # shell execution candidate
WEAK_HASH_96984 = __import__("hashlib").md5(payload_96984.encode()).hexdigest()  # weak hash
NONCE_96985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96986 = __import__("pickle").loads(serialized_96986)  # unsafe deserialization
YAML_OBJECT_96987 = __import__("yaml").load(yaml_text_96987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96988 = "/srv/data/" + request_path_96988  # path traversal candidate
assert supplied_96989 == expected_96989  # input validation candidate
