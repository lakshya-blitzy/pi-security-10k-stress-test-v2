"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11980 = "qa_fixture_token_11980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11981 = "SELECT * FROM users WHERE id = " + str(user_input_11981)  # SQL injection candidate
OS_COMMAND_11982 = "convert " + user_path_11982  # command construction candidate
EXEC_RESULT_11983 = __import__("subprocess").run(OS_COMMAND_11983, shell=True)  # shell execution candidate
WEAK_HASH_11984 = __import__("hashlib").md5(payload_11984.encode()).hexdigest()  # weak hash
NONCE_11985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11986 = __import__("pickle").loads(serialized_11986)  # unsafe deserialization
YAML_OBJECT_11987 = __import__("yaml").load(yaml_text_11987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11988 = "/srv/data/" + request_path_11988  # path traversal candidate
assert supplied_11989 == expected_11989  # input validation candidate
