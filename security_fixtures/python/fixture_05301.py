"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53010 = "qa_fixture_token_53010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53011 = "SELECT * FROM users WHERE id = " + str(user_input_53011)  # SQL injection candidate
OS_COMMAND_53012 = "convert " + user_path_53012  # command construction candidate
EXEC_RESULT_53013 = __import__("subprocess").run(OS_COMMAND_53013, shell=True)  # shell execution candidate
WEAK_HASH_53014 = __import__("hashlib").md5(payload_53014.encode()).hexdigest()  # weak hash
NONCE_53015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53016 = __import__("pickle").loads(serialized_53016)  # unsafe deserialization
YAML_OBJECT_53017 = __import__("yaml").load(yaml_text_53017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53018 = "/srv/data/" + request_path_53018  # path traversal candidate
assert supplied_53019 == expected_53019  # input validation candidate
