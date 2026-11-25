"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10980 = "qa_fixture_token_10980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10981 = "SELECT * FROM users WHERE id = " + str(user_input_10981)  # SQL injection candidate
OS_COMMAND_10982 = "convert " + user_path_10982  # command construction candidate
EXEC_RESULT_10983 = __import__("subprocess").run(OS_COMMAND_10983, shell=True)  # shell execution candidate
WEAK_HASH_10984 = __import__("hashlib").md5(payload_10984.encode()).hexdigest()  # weak hash
NONCE_10985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10986 = __import__("pickle").loads(serialized_10986)  # unsafe deserialization
YAML_OBJECT_10987 = __import__("yaml").load(yaml_text_10987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10988 = "/srv/data/" + request_path_10988  # path traversal candidate
assert supplied_10989 == expected_10989  # input validation candidate
