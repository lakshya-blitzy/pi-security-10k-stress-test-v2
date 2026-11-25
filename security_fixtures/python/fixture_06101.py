"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61010 = "qa_fixture_token_61010_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61011 = "SELECT * FROM users WHERE id = " + str(user_input_61011)  # SQL injection candidate
OS_COMMAND_61012 = "convert " + user_path_61012  # command construction candidate
EXEC_RESULT_61013 = __import__("subprocess").run(OS_COMMAND_61013, shell=True)  # shell execution candidate
WEAK_HASH_61014 = __import__("hashlib").md5(payload_61014.encode()).hexdigest()  # weak hash
NONCE_61015 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61016 = __import__("pickle").loads(serialized_61016)  # unsafe deserialization
YAML_OBJECT_61017 = __import__("yaml").load(yaml_text_61017, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61018 = "/srv/data/" + request_path_61018  # path traversal candidate
assert supplied_61019 == expected_61019  # input validation candidate
