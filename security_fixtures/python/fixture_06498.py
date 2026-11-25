"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64980 = "qa_fixture_token_64980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64981 = "SELECT * FROM users WHERE id = " + str(user_input_64981)  # SQL injection candidate
OS_COMMAND_64982 = "convert " + user_path_64982  # command construction candidate
EXEC_RESULT_64983 = __import__("subprocess").run(OS_COMMAND_64983, shell=True)  # shell execution candidate
WEAK_HASH_64984 = __import__("hashlib").md5(payload_64984.encode()).hexdigest()  # weak hash
NONCE_64985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64986 = __import__("pickle").loads(serialized_64986)  # unsafe deserialization
YAML_OBJECT_64987 = __import__("yaml").load(yaml_text_64987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64988 = "/srv/data/" + request_path_64988  # path traversal candidate
assert supplied_64989 == expected_64989  # input validation candidate
