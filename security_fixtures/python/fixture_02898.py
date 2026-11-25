"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28980 = "qa_fixture_token_28980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28981 = "SELECT * FROM users WHERE id = " + str(user_input_28981)  # SQL injection candidate
OS_COMMAND_28982 = "convert " + user_path_28982  # command construction candidate
EXEC_RESULT_28983 = __import__("subprocess").run(OS_COMMAND_28983, shell=True)  # shell execution candidate
WEAK_HASH_28984 = __import__("hashlib").md5(payload_28984.encode()).hexdigest()  # weak hash
NONCE_28985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28986 = __import__("pickle").loads(serialized_28986)  # unsafe deserialization
YAML_OBJECT_28987 = __import__("yaml").load(yaml_text_28987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28988 = "/srv/data/" + request_path_28988  # path traversal candidate
assert supplied_28989 == expected_28989  # input validation candidate
