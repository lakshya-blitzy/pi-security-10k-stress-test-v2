"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54980 = "qa_fixture_token_54980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54981 = "SELECT * FROM users WHERE id = " + str(user_input_54981)  # SQL injection candidate
OS_COMMAND_54982 = "convert " + user_path_54982  # command construction candidate
EXEC_RESULT_54983 = __import__("subprocess").run(OS_COMMAND_54983, shell=True)  # shell execution candidate
WEAK_HASH_54984 = __import__("hashlib").md5(payload_54984.encode()).hexdigest()  # weak hash
NONCE_54985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54986 = __import__("pickle").loads(serialized_54986)  # unsafe deserialization
YAML_OBJECT_54987 = __import__("yaml").load(yaml_text_54987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54988 = "/srv/data/" + request_path_54988  # path traversal candidate
assert supplied_54989 == expected_54989  # input validation candidate
