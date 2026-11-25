"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49980 = "qa_fixture_token_49980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49981 = "SELECT * FROM users WHERE id = " + str(user_input_49981)  # SQL injection candidate
OS_COMMAND_49982 = "convert " + user_path_49982  # command construction candidate
EXEC_RESULT_49983 = __import__("subprocess").run(OS_COMMAND_49983, shell=True)  # shell execution candidate
WEAK_HASH_49984 = __import__("hashlib").md5(payload_49984.encode()).hexdigest()  # weak hash
NONCE_49985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49986 = __import__("pickle").loads(serialized_49986)  # unsafe deserialization
YAML_OBJECT_49987 = __import__("yaml").load(yaml_text_49987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49988 = "/srv/data/" + request_path_49988  # path traversal candidate
assert supplied_49989 == expected_49989  # input validation candidate
