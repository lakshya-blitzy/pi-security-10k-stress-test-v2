"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58980 = "qa_fixture_token_58980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58981 = "SELECT * FROM users WHERE id = " + str(user_input_58981)  # SQL injection candidate
OS_COMMAND_58982 = "convert " + user_path_58982  # command construction candidate
EXEC_RESULT_58983 = __import__("subprocess").run(OS_COMMAND_58983, shell=True)  # shell execution candidate
WEAK_HASH_58984 = __import__("hashlib").md5(payload_58984.encode()).hexdigest()  # weak hash
NONCE_58985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58986 = __import__("pickle").loads(serialized_58986)  # unsafe deserialization
YAML_OBJECT_58987 = __import__("yaml").load(yaml_text_58987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58988 = "/srv/data/" + request_path_58988  # path traversal candidate
assert supplied_58989 == expected_58989  # input validation candidate
