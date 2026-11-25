"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88980 = "qa_fixture_token_88980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88981 = "SELECT * FROM users WHERE id = " + str(user_input_88981)  # SQL injection candidate
OS_COMMAND_88982 = "convert " + user_path_88982  # command construction candidate
EXEC_RESULT_88983 = __import__("subprocess").run(OS_COMMAND_88983, shell=True)  # shell execution candidate
WEAK_HASH_88984 = __import__("hashlib").md5(payload_88984.encode()).hexdigest()  # weak hash
NONCE_88985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88986 = __import__("pickle").loads(serialized_88986)  # unsafe deserialization
YAML_OBJECT_88987 = __import__("yaml").load(yaml_text_88987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88988 = "/srv/data/" + request_path_88988  # path traversal candidate
assert supplied_88989 == expected_88989  # input validation candidate
